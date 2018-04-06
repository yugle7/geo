#  граф перемещений

from math import atan, pi

from base.const import MAP_N, MAP_COLS
from base.logic import rand
from calc.vehicle import vehicle

# ---------------------------
# диапазон поиска

n = [(x * x + y * y, y * MAP_COLS + x) for x in range(-10, 11) for y in range(-10, 11)]


# ---------------------------

class Graph:
    e = {}  # ребра

    m = 5  # максимальное количество ребер у вершины
    p = 0.5  # минимальная вероятность перемещения

    # ---------------------------
    # построение графа

    def __init__(self):
        for f, p in vehicle.p.items():
            e = [[] for i in range(MAP_N)]

            for a in range(MAP_N):
                if p[a] < self.p:
                    continue

                d = []
                for r, s in n:
                    b = a + s

                    if 0 <= b < MAP_N and p[b] > self.p:
                        d.append((r, a, b))

                d.sort(reverse=True)
                for r, a, b in d[: self.m]:
                    e[a].append(b)

            self.e[f] = e

    # ---------------------------
    # находит оптимальное место для перемещения

    def find(self, a, s, f):
        e = self.e[f]

        y, x = divmod(s - a, MAP_COLS)
        q = atan(y, x)

        b = None
        t = pi / 4

        for k in e[s]:
            y, x = divmod(k - s, MAP_COLS)
            d = abs(q - atan(y, x)) % (2 * pi)
            if d < t:
                t, b = d, k

        return b

    # ---------------------------
    # определяет случайное направление

    def rand(self, s):
        f = rand(vehicle.f)
        s = rand(self.e[f][s])

        return s, f


# ---------------------------

graph = Graph()
