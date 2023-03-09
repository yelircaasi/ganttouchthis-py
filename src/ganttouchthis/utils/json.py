import json
from typing import Union

from tinydb.table import Document

from ganttouchthis.structures.task import Color, Priority
from ganttouchthis.utils.date import Date


# TODO: move to scratch folder
class CustomEncoder(json.JSONEncoder):
    def default(self, obj) -> str:
        if isinstance(obj, Date):
            return str(obj)
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


def jsonify(d: Union[dict, Document]) -> dict:
    def convert(val):
        if type(val) in {str, int, list}:
            return val
        return str(val)

    return {str(k): convert(v) for k, v in d.items()}


def dejsonify(d: Union[dict, Document]) -> dict:
    if "priority" in d:
        d["priority"] = Priority[d["priority"]]
    if "color" in d:
        d["color"] = Color[d["color"]]
    if "date" in d:
        d["date"] = Date.fromisoformat(d["date"])
    if "end" in d:
        d["end"] = Date.fromisoformat(d["end"])
    if "start" in d:
        d["start"] = Date.fromisoformat(d["start"])
    d = {k: None if isinstance(v, str) and v in {"None", "null"} else v for k, v in d.items()}
    return d
