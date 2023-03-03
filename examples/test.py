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
# s = g.serialize()
# g2 = Gantt.deserialize(s)


tasks1 = g.get_day(Date.today() + 3)

# save_path = "/tmp/gantt.json"
# g.save(save_path)
# g2 = Gantt()
# g2.open(save_path)


p = Project(
    name="Python лучшие инструменты и практики",
    tasks="17,A",
    priority=Priority.MEDIUM,
    start=Date.today() + 3,
    end=Date.today() + 60,
    cluster=3,
)
p

# s = p.serialize()
# p2 = Project.deserialize(s)
