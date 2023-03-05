import json
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Tuple, Union

from more_itertools import batched

from ganttouchthis.utils.date import Date


class Priority(Enum):
    FINISHED = -2
    UNDEFINED = -1
    WISH = 0
    LOWEST = 1
    LOWER = 2
    LOW = 3
    MEDIUM_LOW = 4
    MEDIUM = 5
    MEDIUM_HIGH = 6
    HIGH = 7
    HIGHER = 8
    CRITICAL = 9
    YESTERDAY = 10

    def __repr__(self) -> str:
        return f"{self.name} ({self.value}/10)"

    def __str__(self) -> str:
        return self.__repr__()


class Color(Enum):
    GRAY = -1
    BLUE = 0
    PURPLE = 1
    YELLOW = 2
    RED = 3
    GREEN = 4

    def __repr__(self) -> str:
        return f"{self.name}"

    def __str__(self) -> str:
        return self.__repr__()


class Task:
    def __init__(
        self,
        project_hash: str,
        date: Optional[Date] = Date.today(),
        name: str = "",
        subtasks: list = ["1"],
        duration: int = 30,
        priority: Priority = Priority.UNDEFINED,
        color: Color = Color.GRAY,
        description: str = "",
    ) -> None:

        self.project_hash = project_hash
        self.date = date
        self.name = name
        self.subtasks = subtasks
        self.hash = hex(hash((name, tuple(subtasks))))
        self.duration = duration
        self.priority = priority
        self.color = color
        self.description = description

    def __repr__(self) -> str:
        task_str = "\n    ".join(
            (
                f"    Date:        {str(self.date)}",
                f"Name:        {self.name}",
                f"Subtasks:    {', '.join(self.subtasks)}",
                f"Duration:    {str(self.duration)} min",
                f"Priority:    {str(self.priority)}",
                f"Color:       {str(self.color)}",
                f"Description: {self.description}",
                f"Hash:        {self.hash}",
                f"Project Hash: {self.project_hash}",
            )
        )
        return task_str

    def as_dict(self):
        return {
            "project_hash": self.project_hash,
            "hash": self.hash,
            "date": str(self.date),
            "name": self.name,
            "subtasks": self.subtasks,
            "duration": self.duration,
            "priority": self.priority.value,
            "color": self.color.name,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, json_dict):
        return cls(
            project_hash=json_dict["project_hash"],
            date=Date.fromisoformat(json_dict["date"]),
            name=json_dict["name"],
            subtasks=json_dict["subtasks"],
            duration=json_dict["duration"],
            priority=Priority(json_dict["priority"]),
            color=Color[json_dict["color"]],
            description=json_dict["description"],
        )


def schedule_tasks(
    project_hash: str,
    name: str,
    task_list: list,
    start: Date,
    end: Union[Date, None] = None,
    cluster: int = 1,
    interval: Union[int, None] = 1,
    priority: Priority = Priority.UNDEFINED,
    duration: int = 30,
) -> dict:

    start = start if start else Date.today() + 1
    task_chunks = list(batched(task_list, cluster))
    nchunks = len(task_chunks)
    if len(task_chunks) == 1:
        return {
            start: Task(
                project_hash, date=start, name=name, subtasks=task_chunks[0], priority=priority, duration=duration
            )
        }
    if end:
        ndays = int(end) - int(start)
        gap = int((ndays - nchunks) / (nchunks - 1))
    elif interval:
        gap = interval - 1
    else:
        raise ValueError("Invalid parameter configuration. Either `end` or `interval` must be specified.")

    def make_pair(enum_task_chunk: Tuple[int, list]) -> Tuple[Date, Task]:
        i, task_chunk = enum_task_chunk
        return (
            d := start + (i + i * gap),
            Task(project_hash, date=d, name=name, subtasks=task_chunk, priority=priority, duration=duration),
        )

    return dict(map(make_pair, enumerate(task_chunks)))
