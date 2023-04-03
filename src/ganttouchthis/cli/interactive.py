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
