# сглаживание трека

from base.const import *
from data.position import Position


# ---------------------------

class Smooth:
    k = 7

    # ---------------------------

    def make(self, p):
        t = s = [Position(q.i, q.x * LAT, q.y * LON, q.t, q.e) for q in p]

        for k in range(self.k):
            d = list(zip(t, s[1:], t[2:]))
            t = s[:]

            for i, (a, b, c) in enumerate(d, 1):
                x = a.x + (b.t - a.t) * (c.x - a.x) / (c.t - a.t)
                y = a.y + (b.t - a.t) * (c.y - a.y) / (c.t - a.t)

                t[i].x = b.x + (x - b.x) * b.r / (abs(a.x - c.x) + b.r) / self.k
                t[i].y = b.y + (y - b.y) * b.r / (abs(a.y - c.y) + b.r) / self.k

        for u, v in zip(t, p):
            v.x = u.x / LAT
            v.y = u.y / LON
