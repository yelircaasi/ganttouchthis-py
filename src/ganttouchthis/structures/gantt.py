import os
from collections import defaultdict
from operator import itemgetter
from pathlib import Path
from typing import Any, Callable, ClassVar, Iterable, List, Optional, Union

from tinydb import Query, TinyDB

from ganttouchthis.structures.backlog import BacklogItem
from ganttouchthis.structures.project import AdjustmentAlg, Project
from ganttouchthis.structures.task import Priority, Task, schedule_tasks
from ganttouchthis.structures.temporal import DayLoads, DayTasks
from ganttouchthis.utils.date import Date, date_range
from ganttouchthis.utils.db import DBPaths
from ganttouchthis.utils.json import dejsonify, jsonify

# TODO: clean up imports
# from ganttouchthis.utils.dotdict import dotdict, as_dotdict
# from ganttouchthis.utils.task_segment_expansion import expand_task_segments

DEFAULT_MAX_LOAD: int = 240


class Gantt:
    def __init__(self) -> None:
        self.db_paths = DBPaths()
        self.query = Query()
        self.default_max_load = DEFAULT_MAX_LOAD
        self.projects: dict = {}
        self.tasks: dict = {}
        self.backlog: dict = {}
        self.days: dict = {}
        self.project_keys = {
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
            "groups",
            "description",
        }
        self.task_keys = {
            "id",
            "project",
            "date",
            "name",
            "link",
            "subtasks",
            "duration",
            "priority",
            "color",
            "groups",
            "description",
        }
        self.day_keys = {"date", "max_load", "tasks"}
        self.backlog_keys = {"name", "tasks", "groups"}

    def setup(
        self,
        start_empty: bool = False,
        base_db_path: Union[None, str, Path] = None,
        default_max_load: Union[None, int] = DEFAULT_MAX_LOAD,
    ) -> None:
        if base_db_path:
            self.db_paths = DBPaths(base_db_path)
        self.default_max_load = default_max_load or self.default_max_load
        self.projects = self.open_projects() if not start_empty else self.projects
        self.tasks = self.open_tasks() if not start_empty else self.tasks
        self.days = self.open_days() if not start_empty else self.get_days()
        self.backlog = self.open_backlog() if not start_empty else self.backlog

    def open_projects(self) -> list:
        projects_db = TinyDB(self.db_paths.PROJECTS_DB_PATH)
        num_projects = len(projects_db)
        projects = dict(map(lambda i: (i + 1, dejsonify(projects_db.get(doc_id=i + 1))), range(num_projects)))
        projects_db.close()
        for k in projects:
            projects[k].update({"id": k})
        return projects

    def open_tasks(self) -> list:
        tasks_db = TinyDB(self.db_paths.TASKS_DB_PATH)
        num_tasks = len(tasks_db)
        tasks = dict(map(lambda i: (i + 1, dejsonify(tasks_db.get(doc_id=i + 1))), range(num_tasks)))
        tasks_db.close()
        for k in tasks:
            tasks[k].update({"id": k})
        return tasks

    def open_days(self) -> dict:
        days_db = TinyDB(self.db_paths.DAYS_DB_PATH)
        days = map(dejsonify, days_db.all())
        days_db.close()
        return {d["date"]: d for d in days}

    def open_backlog(self) -> list:
        backlog_db = TinyDB(self.db_paths.BACKLOG_DB_PATH)
        num_tasks = len(backlog_db)
        backlog = dict(map(lambda i: (i + 1, dejsonify(backlog_db.get(doc_id=i + 1))), range(num_tasks)))
        backlog_db.close()
        # for k in backlog:
        #     backlog[k].update({"id": k})
        return backlog

    def get_day(self, day: Date) -> List[Task]:
        day_tasks: List[Task] = []  # TODO:

        return day_tasks

    def get_days(self) -> dict:
        days: dict = {}  # TODO:

        return days

    def back_up_databases(self) -> None:  # TODO:

        ...

    def save_projects(self, save_dir: Union[Path, str] = "") -> None:
        if not save_dir:
            save_dir = self.db_paths.DB_PATH
        save_dir = Path(save_dir)
        if not save_dir.exists():
            save_dir.mkdir()
        save_path = save_dir / "projects.json"
        os.rename(save_path, "/tmp/projects.json")
        save_path.touch()
        db = TinyDB(save_path)
        db.truncate()
        for doc in self.projects.values():
            db.insert(jsonify(doc))
        db.close()

    def save_tasks(self, save_dir: Union[Path, str] = "") -> None:
        if not save_dir:
            save_dir = self.db_paths.DB_PATH
        save_dir = Path(save_dir)
        if not save_dir.exists():
            save_dir.mkdir()
        save_path = save_dir / "tasks.json"
        os.rename(save_path, "/tmp/tasks.json")
        save_path.touch()
        db = TinyDB(save_path)
        db.truncate()
        for doc in self.tasks.values():
            db.insert(jsonify(doc))
        db.close()

    def save_days(self, save_dir: Union[Path, str] = "") -> None:
        if not save_dir:
            save_dir = self.db_paths.DB_PATH
        save_dir = Path(save_dir)
        if not save_dir.exists():
            save_dir.mkdir()
        save_path = save_dir / "days.json"
        os.rename(save_path, "/tmp/days.json")
        save_path.touch()
        db = TinyDB(save_path)
        db.truncate()
        for doc in self.days.values():
            db.insert(jsonify(doc))
        db.close()

    def save_backlog(self, save_dir: Union[Path, str] = "") -> None:
        if not save_dir:
            save_dir = self.db_paths.DB_PATH
        save_dir = Path(save_dir)
        if not save_dir.exists():
            save_dir.mkdir()
        save_path = save_dir / "backlog.json"
        os.rename(save_path, "/tmp/backlog.json")
        save_path.touch()
        db = TinyDB(save_path)
        db.truncate()
        for doc in self.backlog.values():
            db.insert(jsonify(doc))
        db.close()

    def edit_project(self, project_index: int, key: str, value: Any) -> None:
        self.projects[project_index][key] = value
        if key == "start":
            ...
        elif key == "end":
            ...
        elif key == "interval":
            ...
        elif key in self.task_keys:
            ...
        self.tasks[project_index].update({key: value})

    def edit_task(self, task_index: int, key: str, value: Any) -> None:

        self.tasks[task_index].update({key: value})

    def edit_day(self, date, key, value):
        ...

    def edit_backlog(self, item_index: int, key: str, value: Any):
        ...

    def _check_object_consistency(self) -> bool:  # TODO:

        ...
        is_consistent = True
        return is_consistent

    def _check_database_consistency(self) -> bool:  # TODO:

        ...
        is_consistent = True
        return is_consistent

    def add_project(  # TODO:
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
        ...

    def add_task(self) -> None:  # TODO:

        ...

    def set_max_loads(self) -> None:  # TODO:

        ...

    def show_detailed(self) -> None:  # TODO:

        ...

    def __repr__(
        self,
    ) -> str:
        return ""  # TODO:

    # change to get_ and return object?# TODO:
    def show_day(self, date: Date) -> None:

        ...

    # change to get_ and return object?# TODO:
    def show_project(self, proj_id) -> None:

        ...

    # change to get_ and return object?# TODO:
    def show_task(self, task_id) -> None:

        ...

    def search_projects(self) -> None:  # TODO:

        ...

    def search_tasks(self) -> None:  # TODO:

        ...

    def adjust_loads(self) -> None:  # TODO:

        ...

    def change_task_date(self, task_index: int) -> None:  # TODO: decide whether redundant

        ...
        # change date of self.tasks[task_id]
        # update self.days
        # update self.projects if necessary

    # ---------------------------------------------------------------------------------

    def add_project_interactive(self) -> None:  # TODO:

        ...

    def add_task_interactive(self) -> None:  # TODO:

        ...

    def set_max_loads_interactive(self) -> None:  # TODO:

        ...

    def search_projects_interactive(self) -> None:  # TODO:

        ...

    def search_tasks_interactive(self) -> None:  # TODO:

        ...

    def edit_project_interactive(self) -> None:  # TODO:

        ...

    def edit_task_interactive(self) -> None:  # TODO:

        ...

    def edit_day_interactive(self) -> None:  # TODO:

        ...

    def edit_backlog_interactive(self) -> None:  # TODO:

        ...

    def adjust_loads_interactive(self) -> None:  # TODO:

        ...


_g = Gantt()


def get_gantt():
    return _g


#############################################################################################################3
# TODO: incorporate, harvest all useful ideas, then delete

# """
#     def add_project(
#         self,
#         name: str,
#         link: str = "",
#         tasks="1",
#         priority: Priority = Priority.UNDEFINED,
#         groups: set = set(),
#         start: Date = Date.today() + 1,
#         end: Union[Date, None] = Date.today() + 30,
#         interval: Union[int, None] = None,
#         cluster: int = 1,
#         duration: int = 30,
#     ) -> None:

#         proj = Project(
#             name=name,
#             link=link,
#             tasks=tasks,
#             priority=priority,
#             groups=groups,
#             start=start,
#             end=end,
#             interval=interval,
#             cluster=cluster,
#             duration=duration,
#         )
#         ...

#     def get_day(self, day: Date = Date.today(), sort_key=None):
#         # task_list = list(map(lambda x: x.task_schedule.get(day), self.projects))
#         # if sort_key:
#         #     task_list.sort(key=sort_key)
#         # return DayTasks(task_list)
#         ...


#     # def show(self, days: int, groups: list = []):
#     #     for proj in self.projects:
#     #         if (not groups) or proj.group in groups:
#     #             print(proj)


#     def get_tasks(self, day: Date, sort_key: Optional[Callable] = None, reverse: bool = True):  # -> DayTasks:
#         # tasks = self.tasks_db.search(self.query.date == str(day))
#         # if sort_key:
#         #     tasks.sort(key=sort_key, reverse=reverse)
#         # return tasks
#         ...

#     def get_day_loads(self, start_day: Date, end_day: Date) -> DayLoads:
#         # days = date_range(start_day, end_day)
#         # loads = []
#         # for day in days:
#         #     tasks = self.get_tasks(day)
#         #     total = sum([task["duration"] for task in tasks])
#         #     print(total)
#         #     loads.append(total)
#         # return DayLoads(days, loads)
#         ...

#     def set_max_loads(self) -> None:
#         # date_string = "x"
#         # while date_string:
#         #     date_string = input("Date (yyyy-mm-dd):  ")
#         #     if not date_string:
#         #         continue
#         #     day = Date.fromisoformat(date_string)
#         #     load = int(input("Max load (minutes): "))
#         #     self.max_loads.update({day: load})
#         # print()
#         ...

#     def adjust_loads(self, start_day: Date, end_day: Date) -> None:
#         #""Redistribute tasks to respect the maximum amount of time available a given day.""#
#         ...
#         # day = start_day
#         # while day < end_day:
#         #     print(30 * "=" + "\n" + str(day) + "\n" + 30 * "=")
#         #     tasks = self.get_tasks(day, sort_key=lambda t: (t["priority"], t["duration"]))
#         #     total = sum(map(lambda t: t["duration"], tasks))
#         #     while total > self.max_loads[day]:
#         #         print(30 * "=" + "\n" + str(total) + "\n" + 30 * "=")
#         #         task_to_move = tasks.pop()
#         #         print(task_to_move)
#         #         self.edit_task(task_to_move["hash"], "date", str(Date.fromisoformat(task_to_move["date"]) + 1))
#         #         total = sum(map(lambda t: t["duration"], tasks))
#         #     day += 1

#     # TODO: enforce consistency by editing all subtasks when I edit a project
#     # def edit_project(self, hash: str, key: str, value: Any) -> None:

#     #     self.projects[hash].__dict__.update({key: value})
#     #     self.project_db.update(self.projects[hash].as_dict(), self.query.hash == hash)

#     def edit_task(self, hash: str, key: str, value: Any) -> None:
#         ...
#         # task = self.tasks_db.search(self.query.hash == hash)[0]
#         # project_hash = task["project_hash"]
#         # day = Date.fromisoformat(task["date"])
#         # if key == "date":
#         #     new_day = Date.fromisoformat(value)
#         #     if not new_day in self.projects[project_hash].task_schedule:
#         #         self.projects[project_hash].task_schedule.update({new_day: XXX})
#         #     # TODO: unfinished -> rewrite data model to use doc IDs and pointers: example: g.projects_db.get(doc_id=4); also db.update, db.insert, db.upsert
#         #     # TODO: also add task Status enum to all instances

#         # else:
#         #     self.projects[project_hash].task_schedule[day].__dict__.update({key: value})
#         #     update = self.projects[project_hash].task_schedule[day].as_dict()
#         # self.tasks_db.update(update, self.query.hash == hash)

#     def search_projects(
#         self,
#         key1: str,
#         value1: Union[str, list],
#         key2: Optional[str] = None,
#         value2: Optional[Union[str, list]] = None,
#         key3: Optional[str] = None,
#         value3: Optional[Union[str, list]] = None,
#     ) -> list:

#         if key3 and value3:
#             # return self.projects_db.search(
#             #     (self.query[key1] == value1) & (self.query[key2] == value2) & (self.query[key3] == value3)
#             # )
#             ...
#         elif key2 and value2:
#             # return self.projects_db.search((self.query[key1] == value1) & (self.query[key2] == value2))
#             ...
#         else:
#             # return self.projects_db.search((self.query[key1] == value1))
#             ...

#     def search_tasks(
#         self,
#         key1: str,
#         value1: Union[str, list],
#         key2: Optional[str] = None,
#         value2: Optional[Union[str, list]] = None,
#         key3: Optional[str] = None,
#         value3: Optional[Union[str, list]] = None,
#     ) -> list:

#         if key3 and value3:
#             # return self.tasks_db.search(
#             #     (self.query[key1] == value1) & (self.query[key2] == value2) & (self.query[key3] == value3)
#             # )
#             ...
#         elif key2 and value2:
#             # return self.tasks_db.search((self.query[key1] == value1) & (self.query[key2] == value2))
#             ...
#         else:
#             # return self.tasks_db.search((self.query[key1] == value1))
#             ...
# """
