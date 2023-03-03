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


@dataclass
class Task:
    date: Optional[Date] = Date.today()
    name: str = ""
    subtasks: list = field(default_factory=list)
    hash: str = hex(hash((name, subtasks)))
    duration: int = 30
    priority: Priority = Priority.UNDEFINED
    color: Color = Color.GRAY
    description: str = ""

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
                f"Hash:        {self.hash}"
            )
        )
        return task_str


    def as_dict(self):
        return {
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
            date=Date.fromisoformat(json_dict["date"]),
            name=json_dict["name"],
            subtasks=json_dict["subtasks"],
            duration=json_dict["duration"],
            priority=Priority(json_dict["priority"]),
            color=Color[json_dict["color"]],
            description=json_dict["description"],
        )


def schedule_tasks(
    name: str,
    task_list: list,
    start: Date,
    end: Union[Date, None] = None,
    cluster: int = 1,
    interval: Union[int, None] = 1,
    priority: Priority = Priority.UNDEFINED,
) -> dict:

    start = start if start else Date.today() + 1
    task_chunks = list(batched(task_list, cluster))
    nchunks = len(task_chunks)
    if len(task_chunks) == 1:
        return {start: Task(date=start, name=name, subtasks=task_chunks[0], priority=priority)}
    if end:
        ndays = int(end) - int(start)
        gap = int((ndays - nchunks) / (nchunks - 1))
    elif interval:
        gap = interval - 1
    else:
        raise ValueError("Invalid parameter configuration. Either `end` or `interval` must be specified.")

    def make_pair(enum_task_chunk: Tuple[int, list]) -> Tuple[Date, Task]:
        i, task_chunk = enum_task_chunk
        return (d := start + (i + i * gap), Task(date=d, name=name, subtasks=task_chunk, priority=priority))

    return dict(map(make_pair, enumerate(task_chunks)))
