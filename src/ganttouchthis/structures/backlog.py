from typing import Any, Dict

from ganttouchthis.utils.repr import multibox


class BacklogItem:
    def __init__(
        self,
        name: str,
        link: str = "",
        tasks: str = "",
        groups: set = set(),
        description: str = "",
    ) -> None:
        self.name = name
        self.link = link
        self.tasks = tasks
        self.groups = groups
        self.description = description

    def __repr__(self) -> str:
        return multibox((self.name, self.tasks, ", ".join(self.groups)))

    def detailed(self) -> None:
        print(
            "\n".join(
                (
                    "" f"Name:          {self.name}",
                    f"  Link:        {self.link}",
                    f"  Tasks:       {self.tasks}",
                    f"  Groups:      {self.groups}",
                    f"  Description: {self.description}",
                )
            )
        )

    def todict(self) -> dict:
        return {
            "name": self.name,
            "link": self.link,
            "tasks": self.tasks,
            "groups": list(self.groups),
            "description": self.description,
        }

    @classmethod
    def fromdict(cls, json_dict: Dict[str, Any]) -> "BacklogItem":
        return cls(
            name=json_dict["name"],
            link=json_dict["link"],
            tasks=json_dict["tasks"],
            groups=set(json_dict["groups"]),
            description=json_dict["description"],
        )
