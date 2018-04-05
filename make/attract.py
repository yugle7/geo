# поиск точек притяжения

from random import randint

from base.logic import span, dist
from base.mongo import active_collection, position_collection
from base.show import Show
from data.place import Place
from data.position import *
from base.const import *

from calc.vehicle import Vehicle
from calc.active import Active

# ---------------------------

active = Active()
vehicle = Vehicle()


# ---------------------------

class Attract:
    i = 0  # человек

    p = []  # положение покоя
    q = []  # сгустки
    s = []  # точки притяжения

    c = []  # номера кластеров точек
    d = 100  # минимальное расстояние между кластерами

    v = 5  # минимальная скорость в точке притяжения
    t = 5  # минимальное актуальное время

    n = 10  # минимальное количество точек в точке притяжения
    m = 5  # максимальное количество точек притяжения

    span = None
    dist = None

    # ---------------------------

    def __init__(self):
        self.span = lambda x, y: span(self.q[x], self.q[y])
        self.dist = lambda x, y: dist(self.q[x], self.q[y])

    def load(self, i):
        self.i = i

        p = position_collection.find({'i': i})
        self.p = [q for q in p if q.v < self.v and q.t > self.t]
        self.q = [Place(q) for q in self.p]

        self.c = list(range(len(self.q)))

    # ---------------------------

    def make(self, p):
        self.load(p)  # получаем точки
        self.cluster()  # кластеризуем точки

        self.find()  # берем несколько точек притяжения

    # ---------------------------
    # определяем характеристики точки

    def active(self, i):
        t = []

        for k in self.s:
            q = self.q[k]

            active.find(k, self.c, self.p, q)

            d = {'i': q.i, 'x': q.x, 'y': q.y, 'r': q.r, 'f': q.f, 'g': q.g}
            t.append(d)

        active_collection.delete_many({'i': i})
        active_collection.insert_many(t)

    # ---------------------------
    # группировка точек присутствия

    def cluster(self):
        t = []
        for i in range(len(self.q)):
            for j in range(i + 1, len(self.q)):
                t.append((self.dist(i, j), i, j))
        t.sort()

        for l, i, j in t:
            x, y = self.get(i), self.get(j)
            if x != y and self.dist(x, y) < self.d:
                self.q[x].merge(self.q[y])
                self.c[y] = x
        t.clear()

    def find(self):
        n = max(q.r for q in self.q)
        n = min(n - 1, self.n, len(self.q) // 10)  # минимум точек

        s = [(q.r, i) for i, q in enumerate(self.q) if q.r > n and self.c[i] == i]
        s.sort(reverse=True)

        self.s = [i for r, i in s[: self.m]]

    def get(self, i):
        if self.c[i] != i:
            self.c[i] = self.get(self.c[i])
        return self.c[i]

    # ---------------------------
    # создаем искусственные данные

    def take(self):
        p = []
        t = NOW

        for q in open('media/location.txt'):
            y, x, n, r = q[:-1].split('\t')
            x = float(x)
            y = float(y)
            n = int(n)
            r = int(r)

            for i in range(n):
                dx = randint(0, r) / LAT
                dy = randint(0, r) / LON

                t += randint(10, 50)
                r = randint(10, 50)

                q = Position(0, x + dx, y + dy, t, r)
                p.append(q)

        t += 1000
        a = None

        for j in range(40):
            x = MAP_X + randint(1, MAP_COLS - 1) * MAP_DX
            y = MAP_Y - randint(1, MAP_ROWS - 1) * MAP_DY

            t += randint(10, 50)
            r = randint(10, 50)

            b = Position(0, x, y, t, r)
            if a:
                t += dist(a, b) // 10

            b.t = t

            p.append(b)
            a = b

        return p

    # ---------------------------

    def demo(self):
        show = Show('n.jpg')

        p = self.take()
        self.make(p)

        for q in p:
            q.show(show, RED)

        for q in self.q:
            q.show(show, BLUE)

        show.save('attract.jpg')
        exit()
