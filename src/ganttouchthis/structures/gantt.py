import os
from pathlib import Path
from typing import Any, Callable, Dict, List, Literal, Optional, Union

from tinydb import Query, TinyDB

from ganttouchthis.structures.backlog import BacklogItem
from ganttouchthis.structures.day import Day
from ganttouchthis.structures.project import Project
from ganttouchthis.structures.task import Task
from ganttouchthis.utils.date import Date, date_range
from ganttouchthis.utils.db import DBPaths
from ganttouchthis.utils.enums import Adjustment, Color, Priority, Status
from ganttouchthis.utils.input import date_input, option_input, validated_input
from ganttouchthis.utils.repr import box, multibox
from ganttouchthis.utils.temporal import schedule_tasks

DEFAULT_MAX_LOAD: int = 240
TODAY = Date.today()


class Gantt:
    def __init__(self) -> None:
        self.db_paths = DBPaths()
        self.query = Query()
        self.default_max_load = DEFAULT_MAX_LOAD
        self.projects: Dict[int, Project] = {}
        self.tasks: Dict[int, Task] = {}
        self.backlog: Dict[int, BacklogItem] = {}
        self.done: Dict[int, Task] = {}
        self.days: Dict[Date, Day] = {}
        self.project_keys = {
            "id",
            "name",
            "link",
            "tasks",
            "priority",
            "start",
            "end",
            "interval",
            "cluster",
            "duration",
            "tags",
            "description",
        }
        self.task_keys = {
            "id",
            "project",
            "date",
            "status",
            "name",
            "link",
            "subtasks",
            "duration",
            "priority",
            "color",
            "tags",
            "description",
        }
        self.day_keys = {"date", "max_load", "tasks"}
        self.backlog_keys = {"name", "link", "tasks", "tags", "description"}
        backlog_path = self.db_paths.DB_PATH / "backlog.json"
        if not backlog_path.exists():
            backlog_path.touch()
        self.backlog_db = TinyDB(backlog_path)

    def show_today(self) -> None:
        self.ensure_day(TODAY)
        tasks = sorted(
            [self.tasks[t] for t in self.days[TODAY].tasks], key=lambda task: (task.priority.value, task.duration)
        )
        for task in tasks:
            print(task)

    # def adjust(self) -> None:
    #     algorithm = Adjustment[option_input(["manual", "rollover", "rigid", "balance"]).upper()]
    #     start = date_input(prompt_start="Start date")
    #     end = date_input(prompt_start="End date")
    #     n: Optional[int] = None
    #     if algorithm == Adjustment.RIGID:
    #         n = int(input("Shift (number of days):\n "))
    #     self.adjust_loads(start=start, end=end, algorithm=algorithm, n=n)

    # def vp(self, limit: int = 50) -> None:
    #     print("".join((str(v) for v in list(self.projects.values())[:limit])))

    # def vt(self, limit: int = 50) -> None:
    #     print("".join((str(v) for v in list(self.tasks.values())[:limit])))

    # def vd(self, limit: int = 50) -> None:
    #     print("".join((str(v) for v in list(self.days.values())[:limit])))

    # def vb(self, limit: int = 50) -> None:
    #     print("".join((str(v) for v in list(self.backlog.values())[:limit])))

    # def dayloads(self, start: Date = TODAY, end: Date = TODAY + 7) -> None:
    #     loads: Dict[Date, int] = self.get_loads_by_day(start=start, end=end)
    #     for day, total in loads.items():
    #         print(f"{str(day)}: {total: >4} min")

    # def showday(self, day: Date = TODAY, key: Optional[Callable] = lambda x: -x.priority.value) -> None:
    #     self.ensure_day(day)
    #     tasks = [self.tasks[i] for i in self.days[day].tasks]
    #     if key:
    #         tasks.sort(key=key)
    #     print("".join(map(str, tasks)))

    def setup(
        self,
        start_empty: bool = False,
        base_db_path: Union[None, str, Path] = None,
        default_max_load: Union[None, int] = DEFAULT_MAX_LOAD,
    ) -> None:
        if base_db_path:
            self.db_paths = DBPaths(base_db_path)
        self.default_max_load = default_max_load or self.default_max_load
        self.projects = self.open_projects() if not start_empty else self.projects
        self.tasks = self.open_tasks() if not start_empty else self.tasks
        self.days = self.open_days() if not start_empty else self.get_days()
        self.backlog = self.open_backlog() if not start_empty else self.backlog
        self.backlog_db = TinyDB(self.db_paths.DB_PATH / "backlog.json")

    def open_projects(self) -> dict:
        projects_db = TinyDB(self.db_paths.PROJECTS_DB_PATH)
        projects = {p.id: p for p in map(Project.fromdict, projects_db.all())}
        projects_db.close()
        return projects

    def open_tasks(self) -> dict:
        tasks_db = TinyDB(self.db_paths.TASKS_DB_PATH)
        tasks = {t.id: t for t in map(Task.fromdict, tasks_db.all())}
        tasks_db.close()
        return tasks

    def open_days(self) -> dict:
        days_db = TinyDB(self.db_paths.DAYS_DB_PATH)
        days = map(Day.fromdict, days_db.all())
        days_db.close()
        return {d.date: d for d in days}

    def open_backlog(self) -> dict:
        backlog_db = TinyDB(self.db_paths.BACKLOG_DB_PATH)
        backlog = map(BacklogItem.fromdict, backlog_db.all())
        backlog_db.close()
        return {i + 1: d for i, d in enumerate(backlog)}

    def ensure_day(self, day: Date) -> None:
        if not day in self.days:
            self.days.update({day: Day(day, max_load=self.default_max_load, tasks=[])})

    def get_loads_by_day(self, start: Date = TODAY, end: Date = TODAY + 7) -> Dict[Date, int]:
        day_loads = {}
        for day in date_range(start, end):
            self.ensure_day(day)
            total = sum(map(lambda t: self.tasks[t].duration, self.days[day].tasks))
            day_loads.update({day: total})
        return day_loads

    def back_up_databases(self) -> None:
        # TODO
        ...

    def save_all(self, save_dir: Union[Path, str] = "") -> None:
        self.save_projects(save_dir)
        print("Projects saved.")
        self.save_tasks(save_dir)
        print("Tasks saved.")
        self.save_days(save_dir)
        print("Days saved.")
        self.save_done(save_dir)
        print("Done tasks saved.")

    def save_projects(self, save_dir: Union[Path, str] = "") -> None:
        if not save_dir:
            save_dir = self.db_paths.DB_PATH
        save_dir = Path(save_dir)
        if not save_dir.exists():
            save_dir.mkdir()
        save_path = save_dir / "projects.json"
        os.rename(save_path, "/tmp/projects.json")
        save_path.touch()
        db = TinyDB(save_path)
        db.truncate()
        for doc in self.projects.values():
            db.insert(doc.todict())
        db.close()

    def save_tasks(self, save_dir: Union[Path, str] = "") -> None:
        if not save_dir:
            save_dir = self.db_paths.DB_PATH
        save_dir = Path(save_dir)
        if not save_dir.exists():
            save_dir.mkdir()
        save_path = save_dir / "tasks.json"
        os.rename(save_path, "/tmp/tasks.json")
        save_path.touch()
        db = TinyDB(save_path)
        db.truncate()
        for doc in self.tasks.values():
            db.insert(doc.todict())
        db.close()

    def save_days(self, save_dir: Union[Path, str] = "") -> None:
        self.days = dict(sorted([(k, v) for k, v in self.days.items()]))
        if not save_dir:
            save_dir = self.db_paths.DB_PATH
        save_dir = Path(save_dir)
        if not save_dir.exists():
            save_dir.mkdir()
        save_path = save_dir / "days.json"
        os.rename(save_path, "/tmp/days.json")
        save_path.touch()
        db = TinyDB(save_path)
        db.truncate()
        for doc in self.days.values():
            db.insert(doc.todict())
        db.close()

    def save_done(self, save_dir: Union[Path, str] = "") -> None:
        if not save_dir:
            save_dir = self.db_paths.DB_PATH
        save_dir = Path(save_dir)
        if not save_dir.exists():
            save_dir.mkdir()
        save_path = save_dir / "done.json"
        save_path.touch()
        os.rename(save_path, "/tmp/done.json")
        save_path.touch()
        db = TinyDB(save_path)
        db.truncate()
        for doc in self.done.values():
            db.insert(doc.todict())
        db.close()

    def edit_project(self, project_id: int, key: str, value: Any) -> None:
        if key in {"name", "link", "priority", "duration", "tags", "description"}:
            if key == "tags":
                self.projects[project_id].tags.add(value)
            else:
                self.projects[project_id].__dict__[key] = value
            task_ids = self.tasks_from_project(project_id)
            for task in task_ids:
                self._edit_task_from_project(task, key, value)
        elif key in {"start", "end", "interval", "cluster", "tasks"}:
            print("Requested edit not possible: '{key}' -> {value}. Use the method 'reschedule_tasks' instead.")
        else:
            print("Requested edit not possible: '{key}' -> {value}.")

    def edit_task(self, task_id: int, key: str, value: Any) -> None:
        if (key == "status") and (value == Status.COMPLETED):
            task = Task.fromdict(self.tasks[task_id].todict())
            self.done.update({task_id: task})
            del self.tasks[task_id]
            self.days[task.date].tasks.remove(task_id)
        elif key in {"duration", "priority", "color", "status"}:
            self.tasks[task_id].__dict__[key] = value
        elif key == "date":
            old_date = Date.fromordinal(self.tasks[task_id].__dict__[key].toordinal())
            self.tasks[task_id].__dict__[key] = value
            self.days[old_date].tasks.remove(task_id)
            self.days[value].tasks.append(task_id)
            self.days[value].tasks.sort()
            # * could add check for sequential consistency, but I prefer the flexibility -> warning?
        elif key == "subtasks":
            print("Warning! Be sure to edit other tasks affected by the change in subtask partitioning.")
            self.tasks[task_id].__dict__[key] = value
            # * could implement this in a more sophisticated manner
        elif key in {"name", "link", "tags", "description"}:
            print("Requested edit not possible: '{key}' -> {value}. Edit via project.")
        else:
            print("Requested edit not possible: '{key}' -> {value}.")

    def _edit_task_from_project(self, task_id: int, key: str, value: Any) -> None:
        if key == "tags":
            self.tasks[task_id].tags.add(value)
        elif key in {"name", "link", "priority", "duration", "description"}:
            self.tasks[task_id].__dict__[key] = value
        else:
            print("Requested edit not possible: '{key}' -> {value}.")

    def edit_day(self, date: Date, key: str, value: int):
        if key == "tasks":
            print("Requested edit not possible: '{key}' -> {value}. Edit via tasks.")
        elif key == "max_load":
            self.days[date].__dict__[key] = value
        else:
            print("Requested edit not possible: '{key}' -> {value}.")

    def edit_backlog(self, item_id: int, key: str, value: str):
        if key in {"name", "tasks"}:
            self.backlog[item_id].__dict__[key] = value
        elif key == "tags":
            self.backlog[item_id].__dict__[key].tags.add(value)
        else:
            print("Requested edit not possible: '{key}' -> {value}.")

    def tasks_from_project(self, project_id: int) -> List[int]:
        return [k for k, v in self.tasks.items() if v.project == project_id]

    def reschedule_tasks(
        self,
        project_id: int,
        start: Optional[Date] = None,
        end: Optional[Date] = None,
        interval: Optional[int] = None,
        cluster: Optional[int] = None,
        tasks: Optional[str] = None,
    ) -> None:
        ...

    def _check_object_consistency(self) -> bool:

        ...
        is_consistent = True
        return is_consistent

    def _check_database_consistency(self) -> bool:

        ...
        is_consistent = True
        return is_consistent

    def add_project(
        self,
        name: str,
        link: str = "",
        tasks="1",
        priority: Priority = Priority.UNDEFINED,
        start: Date = TODAY + 1,
        end: Union[Date, None] = None,
        interval: Union[int, None] = None,
        cluster: int = 1,
        duration: int = 30,
        tags: set = set(),
        description: str = "",
    ) -> None:
        project_id = 1 if not self.projects else max(self.projects) + 1
        proj = Project(
            project_id,
            name,
            link=link,
            tasks=tasks,
            priority=priority,
            start=start,
            end=end,
            interval=interval,
            cluster=cluster,
            duration=duration,
            tags=tags,
            description=description,
        )
        self.projects.update({project_id: proj})
        schedule = schedule_tasks(
            start=start,
            end=end,
            interval=interval,
            cluster=cluster,
            tasks=tasks,
        )
        for d, subtasks in schedule.items():
            task_id = 1 if not self.tasks else max(self.tasks) + 1
            self.tasks.update(
                {
                    task_id: Task(
                        task_id,
                        project_id,
                        name,
                        date=d,
                        status=Status.SCHEDULED,
                        link=link,
                        subtasks=subtasks,
                        duration=duration,  # duration applies to full task/cluster, not single item
                        priority=priority,
                        color=Color.NONE,
                        tags=tags,
                        description=description,
                    )
                }
            )
            self.ensure_day(d)
            self.days[d].tasks.append(task_id)
        self.days = dict(sorted([(k, v) for k, v in self.days.items()]))
        print("\nProject added:")
        print(proj)

    def add_backlog_item(
        self,
        name: str,
        link: str = "",
        tasks: str = "",
        priority: Priority = Priority.WISH,
        tags: set = set(),
        cluster: int = 1,
        duration: int = 30,
        description: str = "",
    ) -> None:
        item = BacklogItem(
            name=name,
            link=link,
            tasks=tasks,
            priority=priority,
            tags=tags,
            cluster=cluster,
            duration=duration,
            description=description,
        )
        self.backlog_db.insert(item.todict())
        print(item)

    def set_max_loads(self) -> None:

        ...

    def show_detailed(self) -> None:

        ...

    def __repr__(
        self,
    ) -> str:
        return ""  # TODO:

    def show_day(self, date: Date) -> None:
        print(date)

    def adjust_loads(
        self,
        start: Date = TODAY,
        end: Date = TODAY + 7,
        algorithm: Adjustment = Adjustment.MANUAL,
        n: Optional[int] = None,
    ) -> None:
        if algorithm == Adjustment.ROLLOVER:
            self.adjust_loads_rollover(start, end)
        elif algorithm == Adjustment.RIGID:
            self.adjust_loads_rigid(start, end, n=n or 1)
        elif algorithm == Adjustment.BALANCE:
            self.adjust_loads_balance(start, end)
        elif algorithm == Adjustment.MANUAL:
            self.adjust_loads_manual()
        else:
            raise ValueError("Invalid adjustment algorithm type.")

    def adjust_loads_rollover(self, start: Date, end: Date) -> None:
        d = Date.fromordinal(start.toordinal())
        while d <= end:
            self.ensure_day(d)
            day_tasks = [self.tasks[i] for i in self.days[d].tasks]
            day_tasks.sort(key=lambda t: t.priority.value, reverse=True)
            print(30 * "=" + "\n" + str(d) + "\n" + 30 * "=")  #!!
            max_load = self.days[d].max_load
            total_load = sum(map(lambda t: t.duration, day_tasks))
            while total_load > max_load:
                print(total_load)  #!!
                task_to_move = day_tasks.pop()
                id_to_move = task_to_move.id
                self.edit_task(id_to_move, "date", d + 1)
                total_load -= task_to_move.duration
            d += 1
        self.sort_days()

    def adjust_loads_rigid(self, start: Date, end: Date, n: int = 1) -> None:
        for t in self.tasks:
            if start <= self.tasks[t].date <= end:
                self.tasks[t].date += n
        for d in date_range(end, start):
            tasks = self.days[d].tasks
            self.days[d + n].tasks.extend(tasks)
            self.days[d].tasks = []
        for p in self.projects:
            if self.projects[p].start <= end:
                self.projects[p].start += n
                if self.projects[p].end:
                    self.projects[p].end += n
        self.sort_days()

    def adjust_loads_balance(self, start: Date, end: Date) -> None:
        loads: Dict[Date, int] = self.get_loads_by_day(start=start, end=end)
        mean_load = int(sum(loads.values()) / len(loads)) + 1
        d = Date.fromordinal(start.toordinal())
        self.ensure_day(d)
        while d <= end:
            self.ensure_day(d + 1)
            print(30 * "=" + "\n" + str(d) + "\n" + 30 * "=")  #!!
            day_tasks = [self.tasks[i] for i in self.days[d].tasks]
            day_tasks.sort(key=lambda t: t.priority.value, reverse=True)
            next_day_tasks = [self.tasks[i] for i in self.days[d + 1].tasks]
            next_day_tasks.sort(key=lambda t: t.priority.value, reverse=True)
            max_load = mean_load + 30
            total_load = sum(map(lambda t: t.duration, day_tasks))
            while abs(total_load - max_load) > 31:
                if total_load > max_load:
                    print(total_load)  #!!
                    task_to_move = day_tasks.pop()
                    id_to_move = task_to_move.id
                    self.edit_task(id_to_move, "date", d + 1)
                    total_load -= task_to_move.duration
                    if (max_load - total_load) > 31:
                        continue
                elif total_load < max_load:
                    print(total_load)  #!!
                    task_to_move = next_day_tasks.pop()
                    id_to_move = task_to_move.id
                    self.edit_task(id_to_move, "date", d + 1)
                    total_load += task_to_move.duration
                    if (total_load - max_load) > 31:
                        continue
            d += 1
        self.sort_days()

    def adjust_loads_manual(self) -> None:

        self.sort_days()

    def sort_days(self) -> None:
        self.days = dict(sorted([(k, v) for k, v in self.days.items()]))


_g = Gantt()


def get_gantt():
    return _g
