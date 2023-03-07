from dataclasses import dataclass
from os import environ
from pathlib import Path


@dataclass
class DBPaths:
    DB_PATH = Path.expanduser(Path(environ.get("GANTTOUCHTHIS_DB_PATH", "~/.cache/ganttouchthis/db")))
    PROJECTS_DB_PATH = DB_PATH / "projects.json"
    TASKS_DB_PATH = DB_PATH / "tasks.json"
    MAX_LOADS_DB_PATH = DB_PATH / "max_loads.json"
    BACKLOG_DB_PATH = DB_PATH / "backlog.json"
