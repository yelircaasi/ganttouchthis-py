from datetime import date, timedelta
from typing import Union


class Date:
    def __init__(self, year: int = 2023, month: int = 1, day: int = 1) -> None:
        self.__dict__.update(locals())
        self.date = date(year, month, day)

    def __repr__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    def __str__(self) -> str:
        return self.__repr__()

    def __add__(self, x: int) -> "Date":
        return Date.fromordinal(self.date.toordinal() + x)

    def __sub__(self, x: int) -> "Date":
        return Date.fromordinal(self.date.toordinal() - x)

    def __int__(self):
        return self.date.toordinal() - 738577  # = datetime.date(2023, 2, 26).toordinal()

    def rel(self):
        return self.date.toordinal() - self.date.today().toordinal()

    @classmethod
    def fromordinal(cls, x: int) -> "Date":
        d = date.fromordinal(x)
        return cls(d.year, d.month, d.day)

    def toordinal(self):
        return self.date.toordinal()
    
    def english(self):
        return {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }[self.date.isoweekday()]

    @classmethod
    def today(cls):
        d = date.today()
        return cls(d.year, d.month, d.day)

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Date):
            return NotImplemented
        return self.__repr__() == __o.__repr__()

    def __le__(self, __o: object) -> bool:
        if not isinstance(__o, Date):
            return NotImplemented
        return self.toordinal() <= __o.toordinal()

    def __ge__(self, __o: object) -> bool:
        if not isinstance(__o, Date):
            return NotImplemented
        return self.toordinal() >= __o.toordinal()

    def __lt__(self, __o: object) -> bool:
        if not isinstance(__o, Date):
            return NotImplemented
        return self.toordinal() < __o.toordinal()

    def __gt__(self, __o: object) -> bool:
        if not isinstance(__o, Date):
            return NotImplemented
        return self.toordinal() > __o.toordinal()

    @classmethod
    def fromisoformat(cls, iso_date: str) -> Union["Date", None]:
        if iso_date == "None":
            return None
        d = date.fromisoformat(iso_date)
        return cls(d.year, d.month, d.day)


def date_range(date1: Date, date2: Date, inclusive: bool = True) -> list:
    if not inclusive:
        date2 -= 1

    date_i = date1
    dates = [date_i]

    while date_i < date2:
        dates.append(date_i := date_i + 1)

    return dates
