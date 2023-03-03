from datetime import date, timedelta


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

    @classmethod
    def fromisoformat(cls, iso_date: str) -> "Date":
        if iso_date == "None":
            return None
        d = date.fromisoformat(iso_date)
        return cls(d.year, d.month, d.day)
