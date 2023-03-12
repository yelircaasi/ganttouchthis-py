from enum import Enum


class Priority(Enum):
    FINISHED = -2
    UNDEFINED = -1
    WISH = 0
    LOWEST = 1
    LOWER = 2
    LOW = 3
    MEDIUM_LOW = 4
    MEDIUM = 5
    MEDIUM_HIGH = 6
    HIGH = 7
    HIGHER = 8
    CRITICAL = 9
    YESTERDAY = 10

    def __repr__(self) -> str:
        return f"{self.name} ({self.value}/10)"

    def __str__(self) -> str:
        return self.name

    def __int__(self) -> int:
        return self.value


class Color(Enum):
    NONE = -1
    BLUE = 0
    PURPLE = 1
    YELLOW = 2
    RED = 3
    GREEN = 4

    def __repr__(self) -> str:
        return f"{self.name}"

    def __str__(self) -> str:
        return self.__repr__()

    def __int__(self) -> int:
        return self.value


class Status(Enum):
    NONE = -1
    SCHEDULED = 0
    IN_PROGRESS = 1
    COMPLETED = 2

    def __repr__(self) -> str:
        return f"{self.name} ({self.value})"

    def __str__(self) -> str:
        return self.name

    def __int__(self) -> int:
        return self.value
