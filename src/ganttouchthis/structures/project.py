from dataclasses import dataclass
from enum import Enum
from typing import Dict, Literal, TypedDict, Union

from ganttouchthis.structures.task import DayTasks, Priority, schedule_tasks
from ganttouchthis.utils.date import Date
from ganttouchthis.utils.spacer import expand_tasks

AdjustmentAlg = Literal["EVEN", "RIGID", "ROLLOVER"]


class AdjustmentParams(TypedDict):
    new_start_date: Date
    new_end_date: Date


@dataclass
class ProjectInit:
    ...


class Project:
    def __init__(
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
        """ """
        self.name = name
        self.task_list = expand_tasks(tasks)
        self.task_schedule = schedule_tasks(self.task_list, start, end, cluster, interval, name, priority)

    def __repr__(self) -> str:
        return (
            "\n\n"
            + self.name
            + "\n\n "
            + "\n ".join(map(lambda kv: f"{kv[0]}:\n{kv[1]}\n", self.task_schedule.items()))
        )

    def push_back(self, algorithm: AdjustmentAlg):
        ...

    def serialize(self) -> dict:
        proj_dict: Dict[Date, dict] = {}
        return proj_dict

    @classmethod
    def deserialize(cls, proj_dict: dict) -> "Project":
        prj = Project("")

        return prj
