from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Union

from more_itertools import batched

from ganttouchthis.utils.date import Date
from ganttouchthis.utils.task_segment_expansion import expand_task_segments


def schedule_tasks(
    start: Date,
    end: Optional[Date] = None,
    interval: Optional[int] = None,
    cluster: Optional[int] = None,
    tasks: Optional[str] = None,
) -> Dict[Date, Any]:
    tasks = tasks if tasks else "1"
    task_list = expand_task_segments(tasks)
    start = start if start else Date.today() + 1
    task_chunks = list(batched(task_list, cluster if cluster else 1))
    nchunks = len(task_chunks)
    if len(task_chunks) == 1:
        return {start: task_list[0]}
    elif end:
        ndays = int(end) - int(start)
        gap = int((ndays - nchunks) / (nchunks - 1))
    elif interval:
        gap = interval - 1
    else:
        raise ValueError("Invalid parameter configuration. Either `end` or `interval` must be specified.")

    return {start + (i + i * gap): task_chunk for i, task_chunk in enumerate(task_chunks)}
