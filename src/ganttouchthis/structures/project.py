import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Literal, Optional, TypedDict, Union

from ganttouchthis.structures.task import Priority, Task, schedule_tasks
from ganttouchthis.structures.temporal import DayLoads, DayTasks
from ganttouchthis.utils.date import Date
from ganttouchthis.utils.json import CustomEncoder
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
        name: str = "Unnamed Project",
        link: str = "",
        tasks: str = "",
        priority: Priority = Priority.UNDEFINED,
        groups: set = set(),
        start: Date = Date.today() + 1,
        end: Optional[Date] = Date.today() + 30,
        interval: Union[int, None] = None,
        cluster: int = 1,
        duration: int = 30,
        task_list: list = [],
    ) -> None:
        """ """
        self.name = name
        self.link = link
        self.task_list = task_list or expand_tasks(tasks)
        self.tasks = tasks
        self.start = start
        self.end = end
        self.priority = priority
        self.interval = interval
        self.cluster = cluster
        self.groups = groups
        self.hash = hex(hash((self.name, tuple(self.task_list))))
        self.duration = duration
        self.task_schedule = schedule_tasks(
            self.hash,
            self.name,
            self.task_list,
            start or Date.today(),
            end=end,
            cluster=cluster,
            interval=interval,
            priority=self.priority,
        )

    def as_dict(self):
        return {
            "hash": self.hash,
            "name": self.name,
            "link": self.link,
            "tasks": self.tasks,
            "task_list": self.task_list,
            "start": str(self.start),
            "end": str(self.end),
            "priority": self.priority.value,
            "groups": list(self.groups),
            "interval": self.interval,
            "cluster": self.cluster,
            "duration": self.duration,
        }

    @classmethod
    def from_dict(cls, proj_dict) -> "Project":
        return cls(
            name=proj_dict["name"],
            link=proj_dict["link"],
            tasks=proj_dict["tasks"],
            priority=Priority(proj_dict["priority"]),
            groups=set(proj_dict["groups"]),
            start=Date.fromisoformat(proj_dict["start"]) or Date.today(),
            end=Date.fromisoformat(proj_dict["end"]),
            interval=proj_dict["interval"],
            cluster=proj_dict["cluster"],
            duration=proj_dict["duration"],
            task_list=proj_dict["task_list"],
        )

    def __repr__(self) -> str:
        return f"\n\n{self.name} ({self.hash})\n\n" + "\n ".join(
            map(lambda kv: f"{kv[0]}:\n{kv[1]}\n", self.task_schedule.items())
        )
