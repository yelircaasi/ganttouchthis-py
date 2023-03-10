from pathlib import Path

from ganttouchthis import get_gantt

from .utils.db import make_data, read_data

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

    for i, p in projects.items():
        for k, v in p.items():
            assert p[k] == projects_[i][k]
    for i, t in tasks.items():
        for k, v in t.items():
            assert t[k] == tasks_[i][k]
    for d, day in days.items():
        for k, v in day.items():
            assert v == days_[d][k]
    for i, b in g.backlog.items():
        for k, v in b.items():
            assert b[k] == backlog_[i][k]

    # assert projects == projects_
    # assert tasks == tasks_
    # assert days == days_
    # assert backlog == backlog_
