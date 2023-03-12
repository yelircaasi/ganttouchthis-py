import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Literal, Optional, TypedDict, Union

from ganttouchthis.structures.task import Task
from ganttouchthis.utils.date import Date
from ganttouchthis.utils.enums import Color, Priority
from ganttouchthis.utils.repr import multibox
from ganttouchthis.utils.task_segment_expansion import expand_task_segments
from ganttouchthis.utils.temporal import schedule_tasks

AdjustmentAlg = Literal["EVEN", "RIGID", "ROLLOVER"]


class Project:
    def __init__(
        self,
        id_: int,
        name: str,
        link: str = "",
        tasks: str = "1",
        priority: Priority = Priority.UNDEFINED,
        start: Date = Date.today() + 1,
        end: Optional[Date] = Date.today() + 30,
        interval: Union[int, None] = None,
        cluster: int = 1,
        duration: int = 30,
        tags: set = set(),
        description: str = "",
    ) -> None:
        """ """
        self.id = id_
        self.name = name
        self.link = link
        self.tasks = tasks
        self.priority = priority
        self.start = start
        self.end = end
        self.interval = interval
        self.cluster = cluster
        self.duration = duration
        self.tags = tags
        self.description = description
        self.keys = {
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
        }

    def todict(self):
        return {
            "id": self.id,
            "name": self.name,
            "link": self.link,
            "tasks": self.tasks,
            "start": str(self.start),
            "end": str(self.end),
            "priority": self.priority.value,
            "interval": self.interval,
            "cluster": self.cluster,
            "duration": self.duration,
            "tags": list(self.tags),
            "description": self.description,
        }

    @classmethod
    def fromdict(cls, proj_dict) -> "Project":
        return cls(
            proj_dict["id"],
            proj_dict["name"],
            link=proj_dict["link"],
            tasks=proj_dict["tasks"],
            priority=Priority(proj_dict["priority"]),
            start=Date.fromisoformat(proj_dict["start"]) or Date.today(),
            end=Date.fromisoformat(proj_dict["end"]),
            interval=proj_dict["interval"],
            cluster=proj_dict["cluster"],
            duration=proj_dict["duration"],
            tags=set(proj_dict["tags"]),
            description=proj_dict["description"],
            # task_list=proj_dict["task_list"],
        )

    def __repr__(self) -> str:
        return "\n".join(
            ("", multibox((self.name, self.tasks, f"{str(self.start)} ─ {str(self.end)}", f"ID: {self.id}")), "")
        )

    def detailed(self) -> None:
        print(
            f"\n\n{self.name} ({self.id})"
            + "\n ".join(
                (
                    "" f"Link:        {self.link}",
                    f"Tasks:       {self.tasks}",
                    f"Priority:    {self.priority.name}",
                    f"Start:       {str(self.start)}",
                    f"End:         {str(self.end)}",
                    f"Interval:    {str(self.interval)}",
                    f"Cluster:     {str(self.cluster)}",
                    f"Duration:    {self.duration} min",
                    f"Groups:      {', '.join(self.tags)}",
                    f"Description: {self.description}",
                )
            )
        )
