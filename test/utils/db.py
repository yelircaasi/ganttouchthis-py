from pathlib import Path
from typing import Any, Dict, Tuple

from tinydb import TinyDB

from ganttouchthis import Color, Date, Priority
from ganttouchthis.structures.backlog import BacklogItem
from ganttouchthis.structures.day import DayAgenda
from ganttouchthis.structures.project import Project
from ganttouchthis.structures.task import Task
from ganttouchthis.utils.enums import Status


def make_data():

    zero_date = Date(2023, 4, 3)
    projects = {
        1: Project(
            1,
            "One Book",
            link="",
            tasks="3,A",
            priority=Priority.MEDIUM,
            start=zero_date,
            end=zero_date + 20,
            interval=None,
            cluster=1,
            duration=30,
            tags={"python"},
            description="a book to read",
        ),
        2: Project(
            2,
            "Еще книга",
            link="",
            tasks="3",
            priority=Priority.HIGH,
            start=zero_date,
            end=None,
            interval=4,
            cluster=3,
            duration=90,
            tags={"russian", "fiction"},
            description="",
        ),
        3: Project(
            3,
            "Book the Third",
            link="",
            tasks="0-2,A0-A1",
            priority=Priority.WISH,
            start=zero_date,
            end=zero_date + 20,
            interval=None,
            cluster=2,
            duration=60,
            tags={"docker", "devops"},
            description="a book on best practices with docker",
        ),
    }
    # schedule_tasks("hash", "One Book", ["1", "2", "3", "4"], zero_date, zero_date + 50, 1, None, Priority.MEDIUM, 30)
    tasks = {
        1: Task(
            1,
            1,
            "One Book",
            date=Date(2023, 4, 3),
            status=Status.IN_PROGRESS,
            link="",
            subtasks="1",
            duration=30,
            priority=Priority.MEDIUM,
            color=Color.NONE,
            tags={"python"},
            description="a book to read",
        ),
        2: Task(
            2,
            1,
            "One Book",
            date=Date(2023, 4, 9),
            status=Status.SCHEDULED,
            link="",
            subtasks="2",
            duration=30,
            priority=Priority.MEDIUM,
            color=Color.NONE,
            tags={"python"},
            description="a book to read",
        ),
        3: Task(
            3,
            1,
            "One Book",
            date=Date(2023, 4, 15),
            status=Status.SCHEDULED,
            link="",
            subtasks="3",
            duration=30,
            priority=Priority.MEDIUM,
            color=Color.NONE,
            tags={"python"},
            description="a book to read",
        ),
        4: Task(
            4,
            1,
            "One Book",
            date=Date(2023, 4, 21),
            status=Status.SCHEDULED,
            link="",
            subtasks="4",
            duration=90,
            priority=Priority.MEDIUM,
            color=Color.NONE,
            tags={"python"},
            description="a book to read",
        ),
        5: Task(
            5,
            2,
            "Еще книга",
            date=Date(2023, 4, 3),
            status=Status.SCHEDULED,
            link="",
            subtasks="1, 2, 3",
            duration=30,
            priority=Priority.HIGH,
            color=Color.NONE,
            tags={"russian", "fiction"},
            description="",
        ),
        6: Task(
            6,
            3,
            "Book the Third",
            date=Date(2023, 4, 3),
            status=Status.IN_PROGRESS,
            link="",
            subtasks="0, 1",
            duration=60,
            priority=Priority.WISH,
            color=Color.NONE,
            tags={"docker", "devops"},
            description="a book on best practices with docker",
        ),
        7: Task(
            7,
            3,
            "Book the Third",
            date=Date(2023, 4, 12),
            status=Status.SCHEDULED,
            link="",
            subtasks="2, A0",
            duration=60,
            priority=Priority.WISH,
            color=Color.NONE,
            tags={"docker", "devops"},
            description="a book on best practices with docker",
        ),
        8: Task(
            8,
            3,
            "Book the Third",
            date=Date(2023, 4, 21),
            status=Status.SCHEDULED,
            link="",
            subtasks="A1",
            duration=60,
            priority=Priority.WISH,
            color=Color.NONE,
            tags={"docker", "devops"},
            description="a book on best practices with docker",
        ),
    }
    schedules = {
        Date(2023, 4, 3): DayAgenda(Date(2023, 4, 3), max_load=240, tasks=[1, 5, 6]),
        Date(2023, 4, 4): DayAgenda(Date(2023, 4, 4), max_load=240, tasks=[]),
        Date(2023, 4, 5): DayAgenda(Date(2023, 4, 5), max_load=240, tasks=[]),
        Date(2023, 4, 6): DayAgenda(Date(2023, 4, 6), max_load=240, tasks=[]),
        Date(2023, 4, 7): DayAgenda(Date(2023, 4, 7), max_load=240, tasks=[]),
        Date(2023, 4, 8): DayAgenda(Date(2023, 4, 8), max_load=240, tasks=[]),
        Date(2023, 4, 9): DayAgenda(Date(2023, 4, 9), max_load=240, tasks=[2]),
        Date(2023, 4, 10): DayAgenda(Date(2023, 4, 10), max_load=240, tasks=[]),
        Date(2023, 4, 11): DayAgenda(Date(2023, 4, 11), max_load=240, tasks=[]),
        Date(2023, 4, 12): DayAgenda(Date(2023, 4, 12), max_load=240, tasks=[7]),
        Date(2023, 4, 13): DayAgenda(Date(2023, 4, 13), max_load=240, tasks=[]),
        Date(2023, 4, 14): DayAgenda(Date(2023, 4, 14), max_load=240, tasks=[]),
        Date(2023, 4, 15): DayAgenda(Date(2023, 4, 15), max_load=240, tasks=[3]),
        Date(2023, 4, 16): DayAgenda(Date(2023, 4, 16), max_load=240, tasks=[]),
        Date(2023, 4, 17): DayAgenda(Date(2023, 4, 17), max_load=240, tasks=[]),
        Date(2023, 4, 18): DayAgenda(Date(2023, 4, 18), max_load=240, tasks=[]),
        Date(2023, 4, 19): DayAgenda(Date(2023, 4, 19), max_load=240, tasks=[]),
        Date(2023, 4, 20): DayAgenda(Date(2023, 4, 20), max_load=240, tasks=[]),
        Date(2023, 4, 21): DayAgenda(Date(2023, 4, 21), max_load=240, tasks=[4, 8]),
    }
    backlog = {
        1: BacklogItem(
            "Pranav Rajpurkar et al.: SQuAD: 100,000+ Questions for Machine Comprehension of Text. EMNLP 2015.",
            tasks="1",
            tags={"papers"},
        ),
        2: BacklogItem(
            "Minjoon Soo et al.: Bi-Directional Attention Flow for Machine Comprehension. ICLR 2015.",
            tasks="1",
            tags={"papers"},
        ),
        3: BacklogItem("HelloChinese", tasks="1", tags={"language_study"}),
        4: BacklogItem("Автоматизация рутинных задач с помощью Python", tasks="8,A", tags={"python"}),
        5: BacklogItem("Python. Сборник упражнений", tasks="34", tags={"python"}),
    }

    return (projects, tasks, schedules, backlog)


def write_data(db_path, projects, tasks, schedules, backlog):
    db = TinyDB(db_path / "projects.json")
    db.truncate()
    for doc in projects.values():
        db.insert(doc.todict())
    db.close()
    db = TinyDB(db_path / "tasks.json")
    db.truncate()
    for doc in tasks.values():
        db.insert(doc.todict())
    db.close()
    db = TinyDB(db_path / "dayagendas.json")
    db.truncate()
    for doc in schedules.values():
        db.insert(doc.todict())
    db.close()
    db = TinyDB(db_path / "backlog.json")
    db.truncate()
    for doc in backlog.values():
        db.insert(doc.todict())
    db.close()


DictTuple = Tuple[Dict[int, Project], Dict[int, Task], Dict[Date, DayAgenda], Dict[int, BacklogItem]]


def read_data(db_path) -> DictTuple:
    db = TinyDB(db_path / "projects.json")
    projects: Dict[int, Project] = {d.id: d for d in map(Project.fromdict, db.all())}
    db.close()
    db = TinyDB(db_path / "tasks.json")
    tasks: Dict[int, Task] = {d.id: d for d in map(Task.fromdict, db.all())}
    db.close()
    db = TinyDB(db_path / "dayagendas.json")
    schedules: Dict[Date, DayAgenda] = {d.date: d for d in map(DayAgenda.fromdict, db.all())}
    db.close()
    db = TinyDB(db_path / "backlog.json")
    backlog: Dict[int, BacklogItem] = {i + 1: d for i, d in enumerate(map(BacklogItem.fromdict, db.all()))}
    db.close()
    return (projects, tasks, schedules, backlog)
