import json
from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Union

from more_itertools import batched

from ganttouchthis.utils.date import Date
from ganttouchthis.utils.enums import Color, Priority, Status
from ganttouchthis.utils.repr import box, multibox


class Task:
    def __init__(
        self,
        id_: int,
        project: int,
        name: str,
        date: Optional[Date] = Date.today(),
        status: Status = Status.SCHEDULED,
        link: str = "",
        subtasks: list = ["1"],
        duration: int = 30,
        priority: Priority = Priority.UNDEFINED,
        color: Color = Color.NONE,
        tags: set = set(),
        description: str = "",
    ) -> None:

        self.id = id_
        self.project = project
        self.name = name
        self.date = date
        self.status = status
        self.link = link
        self.subtasks = subtasks
        self.duration = duration
        self.priority = priority
        self.color = color
        self.tags = tags
        self.description = description

        self.keys = {
            "id",
            "project",
            "date",
            "status",
            "name",
            "link",
            "subtasks",
            "duration",
            "priority",
            "color",
            "tags",
            "description",
        }

    def __repr__(self) -> str:
        return "\n" + multibox((str(self.date), self.name, ", ".join(self.subtasks), f"T{self.id} P{self.project}"))

    def detailed(self):
        task_str = "\n    ".join(
            (
                "",
                f"ID:          {self.id}",
                f"Project:     {self.project}",
                f"Name:        {self.name}",
                f"Date:        {str(self.date)}",
                f"Status:      {str(self.status)}",
                f"Subtasks:    {', '.join(self.subtasks)}",
                f"Duration:    {str(self.duration)} min",
                f"Priority:    {str(self.priority)}",
                f"Color:       {str(self.color)}",
                f"Groups:      {', '.join(self.tags)}",
                f"Description: {self.description}",
                "",
            )
        )
        print(task_str)

    def todict(self):
        return {
            "id": self.id,
            "project": self.project,
            "name": self.name,
            "date": str(self.date),
            "status": str(self.status),
            "link": self.link,
            "subtasks": self.subtasks,
            "duration": self.duration,
            "priority": str(self.priority),
            "color": str(self.color),
            "tags": list(self.tags),
            "description": self.description,
        }

    @classmethod
    def fromdict(cls, json_dict):
        return cls(
            json_dict["id"],
            json_dict["project"],
            json_dict["name"],
            date=Date.fromisoformat(json_dict["date"]),
            status=Status[json_dict["status"]],
            link=json_dict["link"],
            subtasks=json_dict["subtasks"],
            duration=json_dict["duration"],
            priority=Priority[json_dict["priority"]],
            color=Color[json_dict["color"]],
            tags=set(json_dict["tags"]),
            description=json_dict["description"],
        )
