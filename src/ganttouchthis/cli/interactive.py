import os
from pathlib import Path
from typing import Callable

from ganttouchthis import TODAY, Date, Priority, Project, Task
from ganttouchthis.cli.interactive_gantt import get_interactive_gantt
from ganttouchthis.utils.input import option_input, validated_input


def wrap(func: Callable) -> Callable:
    def inner():
        return_val = func()  # accepts only argumentless functions by design
        message = ""  # "\nPress 'enter' to continue, 'c' to clear and continue.\n"
        inp = input(message)
        if inp == "c":
            os.system("clear")

    return inner


def run_interactive():

    g = get_interactive_gantt()
    db_path = validated_input("Database base path", Path, default=Path.expanduser(Path("~/.cache/ganttouchthis/db")))
    if not db_path.exists():
        db_path.mkdir()
    g.setup(base_db_path=db_path)

    zero_date = TODAY
    # g.add_project(
    #     name="Cleaning",
    #     tasks="kitchen - basic,den - basic,living room - basic,bathroom - basic,kitchen - deep,den - deep,extra room - basic,bathroom - deep,bedroom - deep,living room - deep,extra room - deep",
    #     priority=Priority.YESTERDAY,
    #     tags={"python"},
    #     start=zero_date,
    #     interval=1,
    #     cluster=3,
    #     duration=60,
    # )
    # g.add_project(
    #     name="The Well-Grounded Python Developer",
    #     tasks="12",
    #     priority=Priority.CRITICAL,
    #     tags={"python"},
    #     start=zero_date,
    #     end=zero_date + 2,
    #     cluster=2,
    #     duration=20,
    # )
    # g.add_project(
    #     name="Python Testing with pytest",
    #     tasks="16,A2",
    #     priority=Priority.CRITICAL,
    #     tags={"python"},
    #     start=zero_date,
    #     end=zero_date + 15,
    #     cluster=3,
    #     duration=30,
    # )
    # g.add_project(
    #     name="Python лучшие инструменты и практики",
    #     tasks="17,A",
    #     priority=Priority.CRITICAL,
    #     tags={"python"},
    #     start=zero_date,
    #     end=zero_date + 2,
    #     cluster=2,
    #     duration=30,
    # )
    # g.add_project(
    #     name="Effective Python",
    #     tasks="10",
    #     priority=Priority.CRITICAL,
    #     tags={"python"},
    #     start=zero_date + 3,
    #     end=zero_date + 40,
    #     cluster=1,
    #     duration=40,
    # )
    # g.add_project(
    #     name="Профессиональная разработка на Python",
    #     tasks="12",
    #     priority=Priority.CRITICAL,
    #     tags={"python"},
    #     start=zero_date + 1,
    #     end=zero_date + 40,
    #     cluster=1,
    #     duration=30,
    # )
    # g.add_project(
    #     name="Fluent Python (2e)",
    #     tasks="24",
    #     priority=Priority.CRITICAL,
    #     tags={"python"},
    #     start=zero_date + 2,
    #     end=zero_date + 90,
    #     cluster=1,
    #     duration=45,
    # )
    # g.add_project(
    #     name="Robust Python",
    #     tasks="24",
    #     priority=Priority.CRITICAL,
    #     tags={"python"},
    #     start=zero_date + 3,
    #     end=zero_date + 90,
    #     cluster=1,
    #     duration=30,
    # )
    # g.add_project(
    #     name="Exploring CPython's Internals - Python Developer's Guide",
    #     tasks="10",
    #     priority=Priority.HIGHER,
    #     tags={"python", "python_low_level"},
    #     start=zero_date + 1,
    #     end=zero_date + 30,
    #     cluster=1,
    #     duration=30,
    # )

    exit_ = False
    while not exit_:
        option_dict = {
            "show today's tasks": wrap(g.show_today),
            "show upcoming tasks": wrap(g.interactive_show_upcoming_tasks),
            "show upcoming loads": wrap(g.interactive_show_upcoming_loads),
            "show current projects": wrap(g.interactive_show_current_projects),
            "edit": wrap(g.interactive_edit),
            "search": wrap(g.interactive_search),
            "adjust tasks": wrap(g.interactive_adjust),
            "add project": wrap(g.interactive_add_project),
            "set daily maximum loads": wrap(g.interactive_set_maxes),
            "save": wrap(g.interactive_save_all),
            "clear output": wrap(g.clear_output),
            "exit": wrap(exit),
        }
        print()
        option = option_input(option_dict.keys())
        print(option)
        option_dict[option]()
