from datetime import date, timedelta


class Date:
    def __init__(self, year: int = 2023, month: int = 1, day: int = 1) -> None:
        self.__dict__.update(locals())
        self.date = date(year, month, day)

    def __repr__(self):
        return f"{self.year}-{self.month}-{self.day}"

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
