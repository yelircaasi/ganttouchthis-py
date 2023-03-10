from pathlib import Path
from test.utils.db import make_data, read_data

from ganttouchthis import get_gantt

# from ganttouchthis.utils.json import dejsonify

g = get_gantt()
# g.setup(start_empty=True, base_db_path="/tmp/gantt")


# TODO:
def test_save_nonexisting():
    ...


def test_save_empty():
    ...


def test_save_nonempty():
    save_path = Path(__file__).parent / "data/write_nonempty_db"
    projects, tasks, days, backlog = make_data()

    g.projects = projects
    g.tasks = tasks
    g.days = days
    g.backlog = backlog

    g.save_projects(save_path)
    g.save_tasks(save_path)
    g.save_days(save_path)
    g.save_backlog(save_path)

    projects_, tasks_, days_, backlog_ = read_data(save_path)

    for i, p in enumerate(projects):
        for k, v in p.items():
            assert p[k] == projects_[i][k]
    for i, t in enumerate(tasks):
        for k, v in t.items():
            assert t[k] == tasks_[i][k]
    for i, b in enumerate(g.backlog):
        for k, v in b.items():
            assert b[k] == backlog_[i][k]
    for i, (d, day) in enumerate(days.items()):
        for k, v in day.items():
            assert v == days_[i][k]

    # assert projects == projects_
    # assert tasks == tasks_
    # assert days == days_
    # assert backlog == backlog_
