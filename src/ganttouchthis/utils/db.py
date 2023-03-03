from pathlib import Path

from tinydb import Query, TinyDB

DB_PATH = Path.expanduser(Path("~/.cache/ganttouchthis/db"))
projects_db = TinyDB(DB_PATH / "projects.json")
tasks_db = TinyDB(DB_PATH / "tasks.json")
