from ganttouchthis import Date, Gantt, Priority, Project, Task

g = Gantt()

g.add_project(
    name="Python лучшие инструменты и практики",
    tasks="17,A",
    priority=Priority.MEDIUM,
    start=Date.today() + 3,
    end=Date.today(),
    cluster=3,
)
g.add_project(
    name="Python Programming with Design Patterns",
    tasks="13",
    priority=Priority.MEDIUM,
    start=Date.today(),
    end=Date.today() + 60,
    cluster=1,
)

g.get_tasks(day=Date.today())
g.get_day_loads(Date.today(), Date.today() + 14)
g.set_max_loads(Date.today(), Date.today() + 14)
# g.shift_load()
# g.edit_project(...)
# g.edit_task(...)

g.tasks_db.truncate()
g.projects_db.truncate()
