from pathlib import Path

from ganttouchthis import Task, get_gantt

from .utils.db import make_data, read_data

g = get_gantt()


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
    g.save_done(save_path)

    projects_, tasks_, days_, backlog_ = read_data(save_path)

    for i, p in projects.items():
        for k, v in p.todict().items():
            assert p.__dict__[k] == projects_[i].__dict__[k]
    for i, t in tasks.items():
        for k, v in t.todict().items():
            assert t.__dict__[k] == tasks_[i].__dict__[k]
    for d, day in days.items():
        for k, v in day.todict().items():
            assert day.__dict__[k] == days_[d].__dict__[k]
    for i, b in g.backlog.items():
        for k, v in b.todict().items():
            assert b.__dict__[k] == backlog_[i].__dict__[k]
