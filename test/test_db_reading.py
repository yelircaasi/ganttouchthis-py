import os
from pathlib import Path
from test.utils.db import make_data, write_data

from tinydb import TinyDB

from ganttouchthis import Date, Priority, get_gantt

g = get_gantt()


def test_configure_paths_start_empty():

    test_data_path = Path(__file__).parent / "data/empty_db"
    g.setup(start_empty=True, base_db_path=test_data_path)

    assert str(g.db_paths.PROJECTS_DB_PATH).endswith("/test/data/empty_db/projects.json")
    assert str(g.db_paths.TASKS_DB_PATH).endswith("/test/data/empty_db/tasks.json")
    assert str(g.db_paths.DAYS_DB_PATH).endswith("/test/data/empty_db/days.json")
    assert str(g.db_paths.BACKLOG_DB_PATH).endswith("/test/data/empty_db/backlog.json")

    assert g.projects == []
    assert g.tasks == []
    assert g.days == {}
    assert g.backlog == []


def test_open_nonexistent_db():
    def rmdir(dir):
        dir = Path(dir)
        if os.path.exists(dir):
            [os.remove(dir / x) for x in os.listdir(dir)]
            os.rmdir(dir)

    nonexistent_db = Path(__file__).parent / "data/nonexistent_db"
    rmdir(nonexistent_db)

    g = get_gantt()
    g.setup(base_db_path=nonexistent_db)

    assert str(g.db_paths.PROJECTS_DB_PATH).endswith("/test/data/nonexistent_db/projects.json")
    assert str(g.db_paths.TASKS_DB_PATH).endswith("/test/data/nonexistent_db/tasks.json")
    assert str(g.db_paths.DAYS_DB_PATH).endswith("/test/data/nonexistent_db/days.json")
    assert str(g.db_paths.BACKLOG_DB_PATH).endswith("/test/data/nonexistent_db/backlog.json")

    assert g.projects == []
    assert g.tasks == []
    assert g.days == {}
    assert g.backlog == []

    rmdir(nonexistent_db)


def test_open_empty():
    test_data_path = Path(__file__).parent / "data/read_empty_db"
    g.setup(base_db_path=test_data_path)

    assert g.projects == []
    assert g.tasks == []
    assert g.days == {}
    assert g.backlog == []


def test_open_nonempty():
    test_data_path = Path(__file__).parent / "data/read_nonempty_db"
    projects, tasks, days, backlog = make_data()
    write_data(test_data_path, projects, tasks, days, backlog)
    g.setup(base_db_path=test_data_path)

    for i, p in enumerate(g.projects):
        for k, v in p.items():
            assert p[k] == projects[i][k]
    for i, t in enumerate(g.tasks):
        for k, v in t.items():
            assert t[k] == tasks[i][k]
    for i, b in enumerate(g.backlog):
        for k, v in b.items():
            assert b[k] == backlog[i][k]
    for d, day in g.days.items():
        for k, v in day.items():
            assert v == days[d][k]
    # assert g.projects == projects
    # assert g.tasks == tasks
    # assert g.days == days
    # assert g.backlog == backlog
