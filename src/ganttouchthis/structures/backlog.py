from dataclasses import dataclass, field


@dataclass
class BacklogItem:
    name: str
    link: str = ""
    tasks: str = "1"
    groups: set = field(default_factory=set)
