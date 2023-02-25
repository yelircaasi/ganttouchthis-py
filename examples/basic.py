from ganttouchthis import Date, Gantt, Priority, Project, Task
from ganttouchthis.structures.gantt import *
from ganttouchthis.structures.project import *
from ganttouchthis.structures.task import *

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

save_path = "/tmp/gantt.json"
g.save(save_path)
g2 = Gantt()
g2.open(save_path)


p = Project(
    name="Python лучшие инструменты и практики",
    tasks="17,A",
    priority=Priority.MEDIUM,
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=3,
)
p
