import os
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Literal, Optional, Union

from tinydb import Query, TinyDB

from ganttouchthis.structures.backlog import BacklogItem
from ganttouchthis.structures.day import Day
from ganttouchthis.structures.gantt import Gantt
from ganttouchthis.structures.project import Project
from ganttouchthis.structures.task import Task
from ganttouchthis.utils.date import Date, date_range
from ganttouchthis.utils.db import DBPaths
from ganttouchthis.utils.enums import Adjustment, Color, Priority, Status
from ganttouchthis.utils.input import date_input, option_input, validated_input
from ganttouchthis.utils.repr import box, multibox
from ganttouchthis.utils.temporal import schedule_tasks

DEFAULT_MAX_LOAD: int = 240
TODAY = Date.today()


class InteractiveGantt(Gantt):
    def interactive_show_upcoming_tasks(self) -> None:
        num_days = validated_input("Number of days to show", int)
        for day in date_range(TODAY, TODAY + num_days):
            self.ensure_day(day)
            print()
            print(box(str(day)))
            for t in self.days[day].tasks:
                print(self.tasks[t])

    def interactive_show_upcoming_loads(self) -> None:
        num_days = validated_input("Number of days to show", int)
        for day in date_range(TODAY, TODAY + num_days):
            self.ensure_day(day)
            print(multibox((str(day), str(sum((self.tasks[t].duration for t in self.days[day].tasks))))))

    def interactive_show_current_projects(self) -> None:
        num_days = validated_input("How far into the future to look", int)
        for project in self.projects.values():
            if project.start <= TODAY + num_days:
                print(project)

    def interactive_edit(self) -> None:
        toedit = option_input(["Project", "Task", "Day"]).lower()
        self.clear_output()
        if toedit == "project":
            self.interactive_edit_project()
        elif toedit == "task":
            self.interactive_edit_task()
        elif toedit == "day":
            self.interactive_edit_day()

    def interactive_search(self) -> None:
        tosearch = option_input(["Project", "Task", "Day", "Backlog", "Completed"]).lower()
        self.clear_output()
        if tosearch == "project":
            self.interactive_search_project()
        elif tosearch == "task":
            self.interactive_search_task()
        elif tosearch == "day":
            self.interactive_search_day()
        elif tosearch == "backlog":
            self.interactive_search_backlog()
        elif tosearch == "completed":
            self.interactive_search_completed()

    def interactive_adjust(self) -> None:
        algorithm = Adjustment[option_input(["manual", "rollover", "rigid", "balance"]).upper()]
        if algorithm == Adjustment.MANUAL:
            self.adjust_loads_manual()
        else:
            n = None
            if algorithm == Adjustment.RIGID:
                n = validated_input("Number of days to shift back by", int)
            start = date_input(prompt_start="Start date")
            end = date_input(prompt_start="End date")
            self.adjust_loads(start=start, end=end, algorithm=algorithm, n=n)

    def interactive_add_project(self) -> None:
        name = validated_input("Name")
        link = validated_input("Link", default="")
        tasks = validated_input("Tasks (string)")
        priority = validated_input("Priority", lambda x: Priority[x.upper().replace(" ", "_")])
        start = validated_input("Start date (offset from today)", lambda x: TODAY + int(x))
        end = validated_input("End date (offset from today)", lambda x: TODAY + int(x))
        interval = validated_input("Interval", int)
        cluster = validated_input("Cluster", int, default=1)
        duration = validated_input("Duration", int, default=30)
        tags = validated_input("Tags (comma-separated)", default="").split(",")
        description = validated_input("Description", default="")
        self.add_project(
            name,
            link,
            tasks,
            priority,
            start,
            end,
            interval,
            cluster,
            duration,
            tags,
            description,
        )

    def interactive_set_maxes(self) -> None:
        start = date_input(prompt_start="Start date")
        end = date_input(prompt_start="End date")
        for day in date_range(start, end):
            new_load = validated_input(f"Duration for {str(day)}", int)
            self.days[day].max_load = new_load

    def interactive_save_all(self) -> None:
        save_dir = input("Directory in which to save db .json files:\n ")
        self.save_all(save_dir)

    def interactive_search_project(self) -> None:
        key = option_input(
            (
                "id",
                "name",
                "link",
                "tasks",
                "priority",
                "start",
                "end",
                "interval",
                "cluster",
                "duration",
                "tags",
                "description",
            )
        )
        print(key)
        if key == "name":
            value = validated_input(
                "Name",
            )

            def search_condition(x):
                return value.lower() in x.lower()

        elif key == "link":
            value = validated_input(
                "Link",
            )

            def search_condition(x):
                return value.lower() in x.lower()

        elif key == "tasks":
            value = validated_input(
                "Tasks (string)",
            )

            def search_condition(x):
                return value.lower() in x.lower()

        elif key == "priority":
            value = validated_input("Priority", lambda x: Priority[x])

            def search_condition(x):
                return value == x

        elif key == "start":
            value = validated_input("Start date", lambda x: Date.fromisoformat(x))

            def search_condition(x):
                return value == x

        elif key == "end":
            value = validated_input("End date", lambda x: Date.fromisoformat(x))

            def search_condition(x):
                return value == x

        elif key == "interval":
            value = validated_input("Interval", int)

            def search_condition(x):
                return value == x

        elif key == "cluster":
            value = validated_input("Cluster", int)

            def search_condition(x):
                return value == x

        elif key == "duration":
            value = validated_input("Duration", int)

            def search_condition(x):
                return value == x

        elif key == "tags":
            value = validated_input("Tags (comma-separated)", lambda x: list(map(lambda y: y.strip(), x.split(","))))

            def search_condition(x):
                return bool(value.intersection(x))

        elif key == "description":
            value = validated_input("Description", str)

            def search_condition(x):
                return value in x

        for project in self.projects.values():
            if search_condition(project.__dict__[key]):
                print(project)

    def interactive_search_task(self) -> None:
        key = option_input(
            (
                "id",
                "project",
                "name",
                "date",
                "status",
                "link",
                "subtasks",
                "duration",
                "priority",
                "color",
                "tags",
                "description",
            )
        )
        if key == "id":
            value = validated_input("Task ID", int)
            print(self.projects[key])
            return
        elif key == "project":
            value = validated_input("Project ID", str)

            def search_condition(x):
                return value == x

        elif key == "name":
            value = validated_input("Name", str)

            def search_condition(x):
                return value.lower() in x.lower()

        elif key == "date":
            value = validated_input("Date", lambda x: Date.fromisoformat(x))

            def search_condition(x):
                return value == x

        elif key == "status":
            value = validated_input("Status", lambda x: Status[x])

            def search_condition(x):
                return value == x

        elif key == "link":
            value = validated_input("Link", str)

            def search_condition(x):
                return value.lower() in x.lower()

        elif key == "subtasks":
            value = validated_input(
                "Subtasks (comma-separated)", lambda x: list(map(lambda y: y.strip(), x.split(",")))
            )

            def search_condition(x):
                return bool(value.intersection(x))

        elif key == "duration":
            value = validated_input("Duration", int)

            def search_condition(x):
                return value == x

        elif key == "priority":
            value = validated_input("Priority", lambda x: Priority[x])

            def search_condition(x):
                return value == x

        elif key == "color":
            value = validated_input("Color", lambda x: Color[x])

            def search_condition(x):
                return value == x

        elif key == "tags":
            value = validated_input("Tags (comma-separated)", lambda x: list(map(lambda y: y.strip(), x.split(","))))

            def search_condition(x):
                return bool(value.intersection(x))

        elif key == "description":
            value = validated_input("Description", str)

            def search_condition(x):
                return value.lower() in x.lower()

        else:
            print("Problem with key:", key)
        for task in self.tasks.values():
            if search_condition(task.__dict__[key]):
                print(task)

    def interactive_search_day(self) -> None:
        key = option_input(("date", "max_load", "tasks"))
        if key == "date":
            value = validated_input("Date", lambda x: Date.fromisoformat(x))
            print(self.days[value])
            return
        elif key == "max_load":
            value = validated_input("Max load", int)

            def search_condition(x):
                return value == x

        elif key == "tasks":
            value = validated_input("Task", int)

            def search_condition(x):
                return value in x

        else:
            print("Problem with key:", key)
        for day in self.days.values():
            if search_condition(day.__dict__[key]):
                print(day)

    def interactive_search_backlog(self) -> None:
        key = option_input(("name", "link", "tasks", "priority", "cluster", "duration", "tags", "description"))

        if key == "name":
            value = validated_input("Name", str)
            matches = self.backlog_db.search(self.query.name.search(value, re.IGNORECASE))

        elif key == "link":
            value = validated_input("Link", str)
            matches = self.backlog_db.search(self.query.link.search(value, re.IGNORECASE))

        elif key == "tasks":
            value = validated_input("Tasks (str)", str)
            matches = self.backlog_db.search(self.query.tasks.search(value, re.IGNORECASE))

        elif key == "priority":
            value = validated_input("Priority", lambda x: str(Priority[x]))
            matches = self.backlog_db.search(self.query.priority == value)

        elif key == "cluster":
            value = validated_input("Cluster", int)
            matches = self.backlog_db.search(self.query.cluster == value)

        elif key == "duration":
            value = validated_input("Duration", int)
            matches = self.backlog_db.search(self.query.duration == value)

        elif key == "tags":
            value = validated_input("Tags (comma-separated)", lambda x: set(map(lambda y: y.strip(), x.split(","))))

            def test_func(tag_set):
                return bool(value.intersection(tag_set))

            matches = self.backlog_db.search(self.query.tags.test(test_func))

        elif key == "description":
            value = validated_input("Description", str)
            matches = self.backlog_db.search(self.query.description.search(value, re.IGNORECASE))

        else:
            print("Problem with key:", key)

        # for item in self.backlog.values():
        #     if search_condition(item.__dict__[key]):
        #         print(item)
        for completed_task in matches:
            print(Task.fromdict(completed_task))

    def interactive_search_completed(self) -> None:
        key = option_input(
            (
                "id",
                "project",
                "name",
                "date",
                "status",
                "link",
                "subtasks",
                "duration",
                "priority",
                "color",
                "tags",
                "description",
            )
        )
        matches = []
        if key == "name":
            value = validated_input("Name")
            matches = self.backlog_db.search(self.query.name.search(value, re.IGNORECASE))

        elif key == "link":
            value = validated_input("Link")
            matches = self.backlog_db.search(self.query.link.search(value, re.IGNORECASE))

        elif key == "tasks":
            value = validated_input("Tasks (string)")
            matches = self.backlog_db.search(self.query.tasks.search(value, re.IGNORECASE))

        elif key == "priority":
            value = validated_input("Priority", lambda x: str(Priority[x]))
            matches = self.backlog_db.search(self.query.priority == value)

        elif key == "interval":
            value = validated_input("Interval", int)
            matches = self.backlog_db.search(self.query.interval == value)

        elif key == "cluster":
            value = validated_input("Cluster", int)
            matches = self.backlog_db.search(self.query.cluster == value)

        elif key == "duration":
            value = validated_input("Duration", int)
            matches = self.backlog_db.search(self.query.duration == value)

        elif key == "tags":
            value = validated_input("Tags (comma-separated)", lambda x: set(map(lambda y: y.strip(), x.split(","))))

            def test_func(tag_set):
                return bool(value.intersection(tag_set))

            matches = self.backlog_db.search(self.query.tags.test(test_func))

        elif key == "description":
            value = validated_input("Description", str)
            matches = self.backlog_db.search(self.query.description.search(value, re.IGNORECASE))

        else:
            print("Problem with key:", key)

        for completed_task in matches:
            print(BacklogItem.fromdict(completed_task))

    def interactive_edit_project(self) -> None:
        id_ = int(input("Project ID:\n "))
        # key = input("Attribute to edit (name|link|priority|duration|tags|description):\n ")
        key = option_input(("name", "link", "priority", "duration", "tags", "description"))
        value = {
            "duration": lambda x: int(x),
            "priority": lambda x: Priority[x.upper()],
            "tags": lambda x: int(x),
        }.get(key, lambda x: str(x))(input("New value:\n "))
        self.edit_project(id_, key, value)

    def interactive_edit_task(self) -> None:
        id_ = int(input("Task ID:\n "))
        # key = input("Attribute to edit (duration|priority|color|status|date|subtasks):\n ")
        key = option_input(("duration", "priority", "color", "status", "date", "subtasks"))
        value = {
            "duration": lambda x: int(x),
            "priority": lambda x: Priority[x.upper()],
            "color": lambda x: Color[x.upper()],
            "status": lambda x: Status[x.upper()],
            "date": lambda x: Date.fromisoformat(x),
            "subtasks": lambda x: eval(x),
        }.get(key, str)(input("New value:\n "))
        self.edit_task(id_, key, value)

    def interactive_edit_day(self) -> None:
        id_ = Date.fromisoformat(input("Date (yyyy-mm-dd):\n ")) or TODAY - 50  # just for typing
        print("Attribute to edit:\n max_load")
        value = int(input("New value:\n "))
        self.edit_day(id_, "max_load", value)

    def interactive_edit_backlog(self) -> None:
        id_ = int(input("Project ID:\n "))
        key = input("Attribute to edit: ")
        value = input("New value:\n ")
        self.edit_backlog(id_, key, value)

    def clear_output(self) -> None:
        os.system("clear")


_ig = InteractiveGantt()


def get_interactive_gantt():
    return _ig
