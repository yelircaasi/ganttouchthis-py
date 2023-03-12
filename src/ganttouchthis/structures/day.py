from typing import Any, Dict

from ganttouchthis.utils.date import Date
from ganttouchthis.utils.repr import multibox


class Day:
    def __init__(
        self,
        date: Date,
        max_load: int = 240,
        tasks: list = [],
    ) -> None:
        self.date = date
        self.max_load = max_load
        self.tasks = tasks

    def __repr__(self) -> str:
        tasks = ", ".join(map(str, self.tasks))
        return "\n" + multibox(list(map(str, (self.date, self.max_load, tasks))))

    def detailed(self) -> None:
        print(
            "\n".join(
                (
                    "" f"Date:          {str(self.date)}",
                    f"  Max Load:    {self.max_load} min",
                    f"  Tasks:       {', '.join(self.tasks)}",
                )
            )
        )

    def todict(self) -> dict:
        return {
            "date": str(self.date),
            "max_load": self.max_load,
            "tasks": self.tasks,
        }

    @classmethod
    def fromdict(cls, json_dict: Dict[str, Any]) -> "Day":
        return cls(
            date=Date.fromisoformat(json_dict["date"]) or Date.today() - 100,
            max_load=json_dict["max_load"],
            tasks=json_dict["tasks"],
        )
