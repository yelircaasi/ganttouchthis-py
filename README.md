# ganttouchthis

Tool for creating and managing Gantt charts, both as a CLI and a Python API.

By default, data will be stored in `~/.cache/ganttouchthis/db/`, but a different
path can be set with the environment variable `GANTTOUCHTHIS_DB_PATH`.

## Roadmap

[x] look at [GanTTY](https://github.com/timeopochin/GanTTY)

[x] change Gantt class to write completed tasks to db

[x] change Gantt class to not open backlog.json and keep it in memory

[ ] clean up code, remove junk comments, refactor long methods

[ ] write methods (basic and interactive) to create project from backlog

[ ] write test for basic functionality

[ ] write tests for interactive functionality

[ ] refine CLI (using typer?)

[ ] create TUI in the style of GanTTY

[ ] look at [python-gantt](https://xael.org/pages/python-gantt-en.html)

[ ] look at [plotly gantt charts](https://plotly.com/python/gantt/)

[ ] look at [matplotlib gantt charts](https://towardsdatascience.com/gantt-charts-with-pythons-matplotlib-395b7af72d72)

[ ] add support for interfacing with TaskWarrior (and Timewarrior?) and Notion -> taskw Python package

[ ] look into interfacing additionally with taskwarrior-tui and vit
