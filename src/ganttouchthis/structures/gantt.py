from typing import Union

from ganttouchthis.structures.project import AdjustmentAlg, AdjustmentParams, Project
from ganttouchthis.structures.task import DayTasks, Priority, schedule_tasks
from ganttouchthis.utils.date import Date
from ganttouchthis.utils.spacer import expand_tasks

SEP = "\n  \t  \n"


class Gantt:
    def __init__(self, projects: list = []) -> None:
        self.projects = {p.name: p for p in projects}
        # self.groups

    def add_project(
        self,
        name: str,
        tasks="13",
        priority: Priority = Priority.UNDEFINED,
        groups: set = set(),
        start: Date = Date.today() + 1,
        end: Date = Date.today() + 30,
        cluster: int = 1,
        interval: Union[int, None] = None,
    ) -> None:

        self.projects.update(
            {
                name: Project(
                    name=name,
                    tasks=tasks,
                    priority=priority,
                    groups=groups,
                    start=start,
                    end=end,
                    cluster=cluster,
                    interval=interval,
                )
            }
        )

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

    def open(self, json_path):
        ...

    def save(self, json_path):
        ...

    def serialize(self, indet: Union[int, None] = None) -> str:
        # return SEP.join(['['] + list(map(lambda x: x.serialize() + ',', self.projects)) + [']'])
        pl = map(lambda x: x.serialize() + ",", self.projects.values())
        return "[" + SEP + SEP.join(pl).strip(",") + SEP + "]"

    @classmethod
    def deserialize(cls, json_str: str) -> "Gantt":
        projects = list(map(lambda x: Project.deserialize(x.strip(",")), json_str.split(SEP)[1:-1]))
        return cls(projects=projects)
