import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Literal, TypedDict, Union

from ganttouchthis.structures.task import DayTasks, Priority, Task, schedule_tasks
from ganttouchthis.utils.date import Date
from ganttouchthis.utils.json import CustomEncoder
from ganttouchthis.utils.spacer import expand_tasks

AdjustmentAlg = Literal["EVEN", "RIGID", "ROLLOVER"]
TASK_SEP = "\n        \n"
KV_SEP = "     \n"


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
        end: Union[Date, None] = Date.today() + 30,
        interval: Union[int, None] = None,
        cluster: int = 1,
    ) -> None:
        """ """
        self.name = name
        self.link = link
        self.task_list = expand_tasks(tasks)
        self.task_schedule = schedule_tasks(self.name, self.task_list, start, end, cluster, interval, name, priority)

    def __repr__(self) -> str:
        return (
            "\n\n"
            + self.name
            + "\n\n "
            + "\n ".join(map(lambda kv: f"{kv[0]}:\n{kv[1]}\n", self.task_schedule.items()))
        )

    def serialize(self, indent: Union[int, None] = None) -> str:
        ind = lambda x: "" if indent is None else "\n" + x * indent
        task_list = json.dumps(self.task_list, indent=indent)
        head = f'{{{ind(1)}"name": "{self.name}", {ind(1)}"link": "{self.link}", {ind(1)}"task_list": {task_list}, {ind(1)}"task_schedule": {{{TASK_SEP}'
        body = TASK_SEP.join(
            map(lambda kv: '"' + str(kv[0]) + KV_SEP + kv[1].serialize(indent=None) + ",", self.task_schedule.items())
        ).strip(",")
        tail = TASK_SEP + r"}}"
        return head + body + tail

    @classmethod
    def deserialize(cls, json_str) -> "Project":
        segments = json_str.split(TASK_SEP)
        _dict = json.loads(segments[0] + segments[-1])
        date_task_pairs = map(lambda x: x.split(KV_SEP), segments[1:-1])
        task_schedule = dict(
            map(lambda x: (Date.fromisoformat(x[0].strip('"')), Task.deserialize(x[1].strip(","))), date_task_pairs)
        )
        _dict["task_schedule"].update(task_schedule)
        proj = cls(name=_dict["name"], link=_dict["link"])
        proj.task_list = _dict["task_list"]
        proj.task_schedule = _dict["task_schedule"]
        return proj

    def push_back(self, algorithm: AdjustmentAlg):
        ...
