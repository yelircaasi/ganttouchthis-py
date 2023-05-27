import os
from pathlib import Path
from typing import Union


class DBPaths:
    def __init__(self, base_db_path: Union[str, Path] = "~/.cache/ganttouchthis/db"):
        self.DB_PATH = Path.expanduser(Path(os.environ.get("GANTTOUCHTHIS_DB_PATH", base_db_path)))
        self.PROJECTS_DB_PATH = self.DB_PATH / "projects.json"
        self.TASKS_DB_PATH = self.DB_PATH / "tasks.json"
        self.DAYS_DB_PATH = self.DB_PATH / "dayagendas.json"
        self.BACKLOG_DB_PATH = self.DB_PATH / "backlog.json"

        if not self.DB_PATH.exists():
            self.DB_PATH.mkdir()
        for path_ in (self.PROJECTS_DB_PATH, self.TASKS_DB_PATH, self.DAYS_DB_PATH, self.BACKLOG_DB_PATH):
            if not path_.exists():
                path_.touch()
                print(f"{path_} exists.")

    def __repr__(self) -> str:
        return "\n".join(
            (
                "DBPaths",
                "-------",
                f"DB_PATH:           {str(self.DB_PATH)}",
                f"PROJECTS_DB_PATH:  {str(self.PROJECTS_DB_PATH)}",
                f"TASKS_DB_PATH:     {str(self.TASKS_DB_PATH)}",
                f"DAYS_DB_PATH:      {str(self.DAYS_DB_PATH)}",
                f"BACKLOG_DB_PATH:   {str(self.BACKLOG_DB_PATH)}",
            )
        )
