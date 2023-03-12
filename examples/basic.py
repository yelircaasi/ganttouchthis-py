from ganttouchthis import TODAY, Date, Priority, Project, Task, get_gantt

g = get_gantt()
g.setup()

g.add_project(
    name="Python лучшие инструменты и практики",
    tasks="17,A",
    priority=Priority.MEDIUM,
    start=Date.today(),
    end=Date.today() + 60,
    cluster=3,
    duration=90,
)
g.add_project(
    name="Python Programming with Design Patterns",
    tasks="13",
    priority=Priority.MEDIUM,
    start=Date.today(),
    end=Date.today() + 60,
    cluster=1,
    duration=40,
)
g.add_project(
    name="Alice's Adventures in Wonderland",
    tasks="25",
    priority=Priority.MEDIUM,
    start=Date.today(),
    end=Date.today() + 60,
    cluster=4,
    duration=80,
)

g.get_tasks(day=Date.today())
g.get_day_loads(Date.today(), Date.today() + 60)
g.set_max_loads()
g.edit_task("-0x6ccc65b57da62f4f", "priority", Priority.HIGH)

# g.edit_project(...)
# g.edit_task(...)
g.adjust_loads(Date.today(), Date.today() + 20)


g.tasks_db.truncate()
g.projects_db.truncate()
