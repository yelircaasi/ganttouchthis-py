from ganttouchthis import get_gantt

g = get_gantt()
g.setup(start_empty=True, base_db_path="/tmp/gantt")


# TODO:
def test_save_example_projects_db():
    ...


def test_save_example_tasks_db():
    ...


def test_save_example_max_loads_db():
    ...


def test_save_example_backlog_db():
    ...


def test_save_projects_db_if_exists():
    ...


def test_save_tasks_db_if_exists():
    ...


def test_save_max_loads_db_if_exists():
    ...


def test_save_backlog_db_if_exists():
    ...