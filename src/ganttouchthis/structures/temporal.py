from dataclasses import dataclass
from typing import List

from ganttouchthis.utils.date import Date

from .task import Task


@dataclass
class DayTasks:
    tasks: List[Task]

    def __repr__(self) -> str:
        return "\n\n".join(map(str, self.tasks))

    def __str__(self) -> str:
        return self.__repr__()


class DayLoads:
    def __init__(self, dates: List[Date], loads: List[int]):
        self.dict = dict(zip(dates, loads))

    def __repr__(self) -> str:
        return "\nDay loads:\n----------------\n" + "\n".join(
            [f"{str(k)}: {v:>4}" for k, v in self.dict.items()]
        )
