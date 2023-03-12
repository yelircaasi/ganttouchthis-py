from ganttouchthis import Color, Date, Gantt, Priority, Project, Task

g = Gantt()
g.add_project(
    name="Python лучшие инструменты и практики",
    tasks="17,A",
    priority=Priority.MEDIUM,
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=3,
)
g.add_project(
    name="Python Programming with Design Patterns",
    tasks="13",
    priority=Priority.MEDIUM,
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=1,
)

tasks1 = g.get_day(Date.today() + 3)

p = Project(
    id_=3,
    name="Python лучшие инструменты и практики",
    tasks="17,A",
    priority=Priority.MEDIUM,
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=3,
)
