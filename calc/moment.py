# момент времени

from datetime import date, datetime


# ---------------------------

class Moment:
    holiday = []
    n = 8 * 24

    # ---------------------------

    def __init__(self):
        self.load()

    def load(self):
        self.holiday = [
            date(2018, 3, 8),
            date(2018, 3, 9),
            date(2018, 2, 23),
            date(2018, 2, 24),
            date(2017, 7, 14),
        ]

    # ---------------------------
    # определяет момент времени

    def get(self, q):
        t = datetime.fromtimestamp(q.t)

        d = t.date()  # определяем тип дня
        k = 7 if d in self.holiday else d.weekday()
        q.m = k * 24 + t.hour


# ---------------------------

moment = Moment()
