from pathlib import Path

from tinydb import TinyDB

from ganttouchthis import Color, Date, Priority
from ganttouchthis.utils.json import dejsonify, jsonify


def make_data(db_path):

    zero_date = Date(2023, 4, 3)
    projects = [
        {
            "id": 1,
            "name": "One Book",
            "link": "",
            "tasks": "3,A",
            "priority": Priority.MEDIUM,
            "start": zero_date,
            "end": zero_date + 20,
            "interval": None,
            "cluster": 1,
            "duration": 30,
            "groups": ["python"],
            "description": "a book to read",
        },
        {
            "id": 2,
            "name": "Еще книга",
            "link": "",
            "tasks": "3",
            "priority": Priority.HIGH,
            "start": zero_date,
            "end": None,
            "interval": 4,
            "cluster": 3,
            "duration": 90,
            "groups": ["russian", "fiction"],
            "description": "",
        },
        {
            "id": 3,
            "name": "Book the Third",
            "link": "",
            "tasks": "0-2,A0-A1",
            "priority": Priority.WISH,
            "start": zero_date,
            "end": zero_date + 20,
            "interval": None,
            "cluster": 2,
            "duration": 60,
            "groups": ["docker", "devops"],
            "description": "a book on best practices with docker",
        },
    ]
    # schedule_tasks("hash", "One Book", ["1", "2", "3", "4"], zero_date, zero_date + 50, 1, None, Priority.MEDIUM, 30)
    tasks = [
        {
            "id": 1,
            "project": 1,
            "date": Date(2023, 4, 3),
            "name": "One Book",
            "link": "",
            "subtasks": "1",
            "duration": 30,
            "priority": Priority.MEDIUM,
            "color": Color.NONE,
            "groups": ["python"],
            "description": "a book to read",
        },
        {
            "id": 2,
            "project": 1,
            "date": Date(2023, 4, 9),
            "name": "One Book",
            "link": "",
            "subtasks": "2",
            "duration": 30,
            "priority": Priority.MEDIUM,
            "color": Color.NONE,
            "groups": ["python"],
            "description": "a book to read",
        },
        {
            "id": 3,
            "project": 1,
            "date": Date(2023, 4, 15),
            "name": "One Book",
            "link": "",
            "subtasks": "3",
            "duration": 30,
            "priority": Priority.MEDIUM,
            "color": Color.NONE,
            "groups": ["python"],
            "description": "a book to read",
        },
        {
            "id": 4,
            "project": 1,
            "date": Date(2023, 4, 21),
            "name": "One Book",
            "link": "",
            "subtasks": "4",
            "duration": 90,
            "priority": Priority.MEDIUM,
            "color": Color.NONE,
            "groups": ["python"],
            "description": "a book to read",
        },
        {
            "id": 5,
            "project": 2,
            "date": Date(2023, 4, 3),
            "name": "Еще книга",
            "link": "",
            "subtasks": "1, 2, 3",
            "duration": 30,
            "priority": Priority.HIGH,
            "color": Color.NONE,
            "groups": ["russian", "fiction"],
            "description": "",
        },
        {
            "id": 6,
            "project": 3,
            "date": Date(2023, 4, 3),
            "name": "Book the Third",
            "link": "",
            "subtasks": "0, 1",
            "duration": 60,
            "priority": Priority.WISH,
            "color": Color.NONE,
            "groups": ["docker", "devops"],
            "description": "a book on best practices with docker",
        },
        {
            "id": 7,
            "project": 3,
            "date": Date(2023, 4, 12),
            "name": "Book the Third",
            "link": "",
            "subtasks": "2, A0",
            "duration": 60,
            "priority": Priority.WISH,
            "color": Color.NONE,
            "groups": ["docker", "devops"],
            "description": "a book on best practices with docker",
        },
        {
            "id": 8,
            "project": 3,
            "date": Date(2023, 4, 21),
            "name": "Book the Third",
            "link": "",
            "subtasks": "A1",
            "duration": 60,
            "priority": Priority.WISH,
            "color": Color.NONE,
            "groups": ["docker", "devops"],
            "description": "a book on best practices with docker",
        },
    ]
    days = {
        Date(2023, 4, 3): {"date": Date(2023, 4, 3), "max_load": 240, "tasks": [1, 5, 6]},
        Date(2023, 4, 4): {"date": Date(2023, 4, 4), "max_load": 240, "tasks": []},
        Date(2023, 4, 5): {"date": Date(2023, 4, 5), "max_load": 240, "tasks": []},
        Date(2023, 4, 6): {"date": Date(2023, 4, 6), "max_load": 240, "tasks": []},
        Date(2023, 4, 7): {"date": Date(2023, 4, 7), "max_load": 240, "tasks": []},
        Date(2023, 4, 8): {"date": Date(2023, 4, 8), "max_load": 240, "tasks": []},
        Date(2023, 4, 9): {"date": Date(2023, 4, 9), "max_load": 240, "tasks": [2]},
        Date(2023, 4, 10): {"date": Date(2023, 4, 10), "max_load": 240, "tasks": []},
        Date(2023, 4, 11): {"date": Date(2023, 4, 11), "max_load": 240, "tasks": []},
        Date(2023, 4, 12): {"date": Date(2023, 4, 12), "max_load": 240, "tasks": [7]},
        Date(2023, 4, 13): {"date": Date(2023, 4, 13), "max_load": 240, "tasks": []},
        Date(2023, 4, 14): {"date": Date(2023, 4, 14), "max_load": 240, "tasks": []},
        Date(2023, 4, 15): {"date": Date(2023, 4, 15), "max_load": 240, "tasks": [3]},
        Date(2023, 4, 16): {"date": Date(2023, 4, 16), "max_load": 240, "tasks": []},
        Date(2023, 4, 17): {"date": Date(2023, 4, 17), "max_load": 240, "tasks": []},
        Date(2023, 4, 18): {"date": Date(2023, 4, 18), "max_load": 240, "tasks": []},
        Date(2023, 4, 19): {"date": Date(2023, 4, 19), "max_load": 240, "tasks": []},
        Date(2023, 4, 20): {"date": Date(2023, 4, 20), "max_load": 240, "tasks": []},
        Date(2023, 4, 21): {"date": Date(2023, 4, 21), "max_load": 240, "tasks": [4, 8]},
    }
    backlog = [
        {
            "name": "Pranav Rajpurkar et al.: SQuAD: 100,000+ Questions for Machine Comprehension of Text. EMNLP 2015.",
            "tasks": "1",
            "groups": ["papers"],
        },
        {
            "name": "Minjoon Soo et al.: Bi-Directional Attention Flow for Machine Comprehension. ICLR 2015.",
            "tasks": "1",
            "groups": ["papers"],
        },
        {"name": "HelloChinese", "tasks": "1", "groups": ["language_study"]},
        {"name": "Автоматизация рутинных задач с помощью Python", "tasks": "8,A", "groups": ["python"]},
        {"name": "Python. Сборник упражнений", "tasks": "34", "groups": ["python"]},
    ]

    db = TinyDB(db_path / "projects.json")
    db.truncate()
    for doc in projects:
        db.insert(jsonify(doc))
    db.close()
    db = TinyDB(db_path / "tasks.json")
    db.truncate()
    for doc in tasks:
        db.insert(jsonify(doc))
    db.close()
    db = TinyDB(db_path / "days.json")
    db.truncate()
    for doc in days.values():
        db.insert(jsonify(doc))
    db.close()
    db = TinyDB(db_path / "backlog.json")
    db.truncate()
    for doc in backlog:
        db.insert(jsonify(doc))
    db.close()

    return (projects, tasks, days, backlog)


def get_data(db_path):
    projects = []
    tasks = []
    days = []
    backlog = []
    return (projects, tasks, days, backlog)
