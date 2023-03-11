import json
from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Union

from more_itertools import batched

from ganttouchthis.utils.date import Date
from ganttouchthis.utils.enums import Color, Priority


# TODO: rework interface to work well with Gantt
class Task:
    def __init__(
        self,
        project_hash: str,
        date: Optional[Date] = Date.today(),
        name: str = "",
        subtasks: list = ["1"],
        duration: int = 30,
        priority: Priority = Priority.UNDEFINED,
        color: Color = Color.NONE,
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
