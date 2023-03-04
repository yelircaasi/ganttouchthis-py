from os import environ
from pathlib import Path

from tinydb import Query, TinyDB

DB_PATH = Path.expanduser(Path(environ.get("GANTTOUCHTHIS_DB_PATH", "~/.cache/ganttouchthis/db")))
projects_db = TinyDB(DB_PATH / "projects.json")
tasks_db = TinyDB(DB_PATH / "tasks.json")
max_loads_db = TinyDB(DB_PATH / "max_loads.json")
backlog_db = TinyDB(DB_PATH / "backlog.json")
