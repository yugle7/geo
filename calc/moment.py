# момент времени

from datetime import date, datetime
from base.const import MEDIA


# ---------------------------

class Moment:
    holiday = set()
    n = 8 * 24

    url = MEDIA + 'moment/'

    # ---------------------------

    def __init__(self):
        self.load()

    def load(self):
        p = open(self.url + 'holiday.txt').read().split()
        self.holiday.clear()

        for q in p:
            year, month, day = q.split('-')
            self.holiday.add(date(int(year), int(month), int(day)))

    # ---------------------------
    # определяет момент времени

    def get(self, q):
        t = datetime.fromtimestamp(q.t)

        d = t.date()  # определяем тип дня
        k = 7 if d in self.holiday else d.weekday()
        q.m = k * 24 + t.hour


# ---------------------------

moment = Moment()
