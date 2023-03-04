from typing import Callable, Iterable, Optional, Union

from ganttouchthis.structures.backlog import BacklogItem
from ganttouchthis.structures.project import AdjustmentAlg, AdjustmentParams, Project
from ganttouchthis.structures.task import Priority, schedule_tasks
from ganttouchthis.structures.temporal import DayLoads, DayTasks
from ganttouchthis.utils.date import Date, date_range
from ganttouchthis.utils.db import Query, projects_db, tasks_db
from ganttouchthis.utils.spacer import expand_tasks


class Gantt:
    def __init__(self, projects: list = [], backlog: Iterable[BacklogItem] = []) -> None:
        self.projects = {p.name: p for p in projects}
        self.backlog = list(backlog)
        self.projects_db = projects_db
        self.tasks_db = tasks_db
        self.query = Query()
        # self.groups

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

    def get_tasks(self, day: Date, sort_key: Optional[Callable] = None):  # -> DayTasks:
        tasks = self.tasks_db.search(self.query.date == str(day))
        if sort_key:
            tasks.sort(key=sort_key)
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

    def set_max_loads(self, start_day: Date, end_day: Date) -> None:
        self.max_loads = {}
        print("Please set the max load (in minutes) for each day:\n")
        for day in date_range(start_day, end_day):
            self.max_loads.update({day: input(f"Max load for {str(day)} ({day.english() + '):':<11} ")})
        print()

    def shift_load(self) -> None:
        ...

    def edit_project(self, project_hash: str, key: str, value: Any) -> None:
        # db_projects = self.projects_db.search(self.query.hash == project_hash)[0]
        # if not projects:
        #     raise ValueError
        # else:
        #     db_project = projects[-1]
        self.project_db.update({key: value}, self.query.hash == project_hash)
        # obj_project = self.projects[project_hash]
        self.projects[hash].__dict__.update({key, value})

    def edit_task(self, project_hash: str, key: str, value: Any) -> None:
        self.project_db.update({key: value}, self.query.hash == project_hash)
        self.projects[hash].__dict__.update({key, value})

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
