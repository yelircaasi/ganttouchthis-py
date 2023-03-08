import json

from .date import Date


# TODO: move to scratch folder
class CustomEncoder(json.JSONEncoder):
    def default(self, obj) -> str:
        if isinstance(obj, Date):
            return str(obj)
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
