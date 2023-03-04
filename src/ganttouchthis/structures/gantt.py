from collections import defaultdict
from operator import itemgetter
from typing import Any, Callable, Iterable, Optional, Union

from ganttouchthis.structures.backlog import BacklogItem
from ganttouchthis.structures.project import AdjustmentAlg, AdjustmentParams, Project
from ganttouchthis.structures.task import Priority, schedule_tasks
from ganttouchthis.structures.temporal import DayLoads, DayTasks
from ganttouchthis.utils.date import Date, date_range
from ganttouchthis.utils.db import (
    Query,
    backlog_db,
    max_loads_db,
    projects_db,
    tasks_db,
)
from ganttouchthis.utils.spacer import expand_tasks


class Gantt:
    def __init__(self, projects: list = [], backlog: Iterable[BacklogItem] = [], default_max_load: int = 240) -> None:
        self.projects_db = projects_db
        self.tasks_db = tasks_db
        self.max_loads_db = max_loads_db
        self.projects = {hex(hash((p.name, tuple(p.tasks)))): p for p in projects}
        self.projects.update(dict(map(lambda p: (p["hash"], Project.from_dict(p)), self.projects_db.all())))
        self.backlog = list(backlog)

        self.query = Query()
        self.default_max_load = default_max_load
        self.max_loads = defaultdict(lambda: 240)

    def add_project(
        self,
        name: str,
        link: str = "",
        tasks="1",
        priority: Priority = Priority.UNDEFINED,
        groups: set = set(),
        start: Date = Date.today() + 1,
        end: Union[Date, None] = Date.today() + 30,
        interval: Union[int, None] = None,
        cluster: int = 1,
        duration: int = 30,
    ) -> None:

        proj = Project(
            name=name,
            link=link,
            tasks=tasks,
            priority=priority,
            groups=groups,
            start=start,
            end=end,
            interval=interval,
            cluster=cluster,
        )
        hash = proj.hash
        self.projects.update({hash: proj})
        self.projects_db.insert(self.projects[hash].as_dict())
        for task in self.projects[hash].task_schedule.values():
            self.tasks_db.insert(task.as_dict())

    def adjust(self, algorithm: AdjustmentAlg, adj_params: AdjustmentParams, projects: list):
        ...

    def get_day(self, day: Date = Date.today(), sort_key=None):
        task_list = list(map(lambda x: x.task_schedule.get(day), self.projects))
        if sort_key:
            task_list.sort(key=sort_key)
        return DayTasks(task_list)

    def show(self, days: int, groups: list = []):
        for proj in self.projects:
            if (not groups) or proj.group in groups:
                print(proj)

    def __repr__(
        self,
    ) -> str:
        return "TODO"

    def get_tasks(self, day: Date, sort_key: Optional[Callable] = None, reverse: bool = True):  # -> DayTasks:
        tasks = self.tasks_db.search(self.query.date == str(day))
        if sort_key:
            tasks.sort(key=sort_key, reverse=reverse)
        return tasks

    def get_day_loads(self, start_day: Date, end_day: Date) -> DayLoads:
        days = date_range(start_day, end_day)
        loads = []
        for day in days:
            tasks = self.get_tasks(day)
            total = sum([task["duration"] for task in tasks])
            print(total)
            loads.append(total)
        return DayLoads(days, loads)

    def set_max_loads(self) -> None:
        # print("Please set the max load (in minutes) for each day.")
        # print(f"Entering no value will leave it at the default of {self.default_max_load} minutes.\n")
        # for day in date_range(start_day, end_day):
        #     self.max_loads.update({day: input(f"Max load for {str(day)} ({day.english() + '):':<11} ")})
        date_string = "x"
        while date_string:
            date_string = input("Date (yyyy-mm-dd):  ")
            if not date_string:
                continue
            day = Date.fromisoformat(date_string)
            load = int(input("Max load (minutes): "))
            self.max_loads.update({day: load})
        print()

    def adjust_loads(self, start_day: Date, end_day: Date) -> None:
        """Redistribute tasks to respect the maximum amount of time available a given day."""
        day = start_day
        while day < end_day:
            print(30 * "=" + "\n" + str(day) + "\n" + 30 * "=")
            tasks = self.get_tasks(day, sort_key=lambda t: (t.priority.value, t.duration))
            total = sum(map(lambda t: t.duration, tasks))
            while total > self.max_loads[day]:
                print(30 * "=" + "\n" + str(total) + "\n" + 30 * "=")
                task_to_move = tasks.pop()
                self.edit_task(task_to_move.hash, "date", str(task_to_move.date + 1))
                total = sum(map(lambda t: t.duration, tasks))

    # TODO: enforce consitency by editing all subtasks when I edit a project
    # def edit_project(self, hash: str, key: str, value: Any) -> None:

    #     self.projects[hash].__dict__.update({key: value})
    #     self.project_db.update(self.projects[hash].as_dict(), self.query.hash == hash)

    def edit_task(self, hash: str, key: str, value: Any) -> None:

        task = self.tasks_db.search(self.query.hash == hash)[0]
        project_hash = task["project_hash"]
        day = Date.fromisoformat(task["date"])
        self.projects[project_hash].task_schedule[day].__dict__.update({key: value})
        update = self.projects[project_hash].task_schedule[day].as_dict()
        self.tasks_db.update(update, self.query.hash == hash)

    def search_projects(
        self,
        key1: str,
        value1: Union[str, list],
        key2: Optional[str] = None,
        value2: Optional[Union[str, list]] = None,
        key3: Optional[str] = None,
        value3: Optional[Union[str, list]] = None,
    ) -> list:

        if key3 and value3:
            return self.projects_db.search((self.query[key1] == value1))
        elif key2 and value2:
            return self.projects_db.search((self.query[key1] == value1) & (self.query[key2] == value2))
        else:
            return self.projects_db.search(
                (self.query[key1] == value1) & (self.query[key2] == value2) & (self.query[key3] == value3)
            )

    def search_tasks(
        self,
        key1: str,
        value1: Union[str, list],
        key2: Optional[str] = None,
        value2: Optional[Union[str, list]] = None,
        key3: Optional[str] = None,
        value3: Optional[Union[str, list]] = None,
    ) -> list:

        if key3 and value3:
            return self.tasks_db.search((self.query[key1] == value1))
        elif key2 and value2:
            return self.tasks_db.search((self.query[key1] == value1) & (self.query[key2] == value2))
        else:
            return self.tasks_db.search(
                (self.query[key1] == value1) & (self.query[key2] == value2) & (self.query[key3] == value3)
            )
