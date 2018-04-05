# скорости

from base.const import *
from base.logic import span, dist


# ---------------------------

class Velocity:
    speed = []
    n = 0

    # ---------------------------

    def __init__(self):
        self.load()

    def load(self):
        self.speed = list(enumerate([STOP, WALK, BIKE, BUS, CAR]))
        self.n = len(self.speed) + 1

    # ---------------------------

    def get(self, q):
        for i, v in self.speed:
            if q.v < v: return i
        return len(self.speed)

    # ---------------------------
    # вычисляем скорость точек трека

    def find(self, track):
        for i in range(len(track) - 1):
            d = dist(track[i], track[i + 1])
            s = span(track[i], track[i + 1])
            track[i].v = d / s


# ---------------------------

velocity = Velocity()
