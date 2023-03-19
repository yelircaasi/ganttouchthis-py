from typing import Any, Dict

from ganttouchthis.utils.enums import Priority
from ganttouchthis.utils.repr import multibox


class BacklogItem:
    def __init__(
        self,
        name: str,
        link: str = "",
        tasks: str = "",
        priority: Priority = Priority.WISH,
        cluster: int = 1,
        duration: int = 30,
        tags: set = set(),
        description: str = "",
    ) -> None:
        self.name = name
        self.link = link
        self.tasks = tasks
        self.priority = priority
        self.cluster = cluster
        self.duration = duration
        self.tags = tags
        self.description = description

    def __repr__(self) -> str:
        return multibox(
            (
                str(self.name),
                str(self.tasks),
                str(self.priority),
                ", ".join(self.tags),
                f"Cluster: {self.cluster}",
                f"{self.duration} min",
            )
        )

    def detailed(self) -> None:
        print(
            "\n".join(
                (
                    "",
                    f"Name:          {self.name}",
                    f"  Link:        {self.link}",
                    f"  Tasks:       {self.tasks}",
                    f"  Priority:    {self.priority}",
                    f"  Cluster:     {self.cluster}",
                    f"  Duration:    {self.duration}",
                    f"  Tags:        {self.tags}",
                    f"  Description: {self.description}",
                )
            )
        )

    def todict(self) -> dict:
        return {
            "name": str(self.name),
            "link": str(self.link),
            "tasks": str(self.tasks),
            "priority": str(self.priority.name),
            "cluster": int(self.cluster),
            "duration": int(self.duration),
            "tags": list(self.tags),
            "description": str(self.description),
        }

    @classmethod
    def fromdict(cls, json_dict: Dict[str, Any]) -> "BacklogItem":
        return cls(
            name=json_dict["name"],
            link=json_dict["link"],
            tasks=json_dict["tasks"],
            priority=Priority[json_dict["priority"]],
            cluster=int(json_dict["cluster"]),
            duration=int(json_dict["duration"]),
            tags=set(json_dict["tags"]),
            description=json_dict["description"],
        )
