# присутствие в области

from base.const import *
from base.point import Point
from data.square import Square
from base.mongo import position_collection


# ---------------------------

class Present:
    p = set()

    # ---------------------------

    def make(self, area, time):
        p = self.cover(area)
        self.find(p, time)

    # ---------------------------
    # покрытие площади квадратными участками

    def cover(self, area):
        p = []

        dx = MAP_X + MAP_DX / 2
        dy = MAP_Y - MAP_DY / 2

        q = Point(dx, dy)
        for s in range(MAP_N):
            i, j = divmod(s, MAP_COLS)
            q.x = dx + j * MAP_DX
            q.y = dy - i * MAP_DY
            if area.get(q): p.append(s)

        return p

    # ---------------------------
    # поиск в базе по множеству квадратных участков

    def find(self, p, q):
        query = {'s': {'$in': p}}
        self.p.clear()

        for d in position_collection.get(query):
            if not q or q.a < d['t'] < q.b:
                self.p.add(d['i'])
