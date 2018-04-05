# создание искусственных точек

from random import randint, random

from base.const import *
from base.logic import inside, dist, rand
from base.point import Point
from data.position import Position

from fake.graph import graph
from base.mongo import position_collection


# ---------------------------


class Points:
    p = []  # точки

    a, b = 10, 100  # минимальная и максимальная длина траектории
    v = [0.3, 1.5, 5, 15]  # скорости перемещения (стоит, пешком, велосипед, машина)

    r = 50  # максимальная ошибка получения координат
    d = 0.01  # вероятность выброса и смены способа перемещения

    m = 10  # максимальное количество треков у человека
    t = 1000000  # ограничение по времени наблюдения

    k = 3  # количество точек притяжения
    n = 10  # сколько времени человек топчется

    # ---------------------------
    # создание случайных треков

    def make(self, k):
        for i in range(k):
            self.find(i)
        self.p.sort(key=lambda q: q.t)

        self.save()

    # ---------------------------
    # создание трека

    def track(self, t, i, q):

        # ---------------------------
        # 1. топчемся в точке притяжения

        d = 10

        for n in range(self.n):
            r = randint(1, self.r) + (random() < self.d) * self.r
            self.p.append(Position(i, q.x, q.y, t, r))

            q.x += (2 * random() - 1) * self.v[0] * d / LAT
            q.y += (2 * random() - 1) * self.v[0] * d / LON

            t += d

        # ---------------------------
        # 2. выбираем направление

        r = randint(1, self.r) + (random() < self.d) * self.r
        a = Position(i, q.x, q.y, t, r)

        s, f = graph.rand(a.s)
        v = self.v[f]

        q.prob(s)

        r = randint(1, self.r) + (random() < self.d) * self.r
        t += dist(a, q) / v

        b = Position(i, q.x, q.y, t, r)

        a.f = b.f = f
        self.p += [a, b]

        # ---------------------------
        # 3. движемся

        n = randint(self.a, self.b)

        for k in range(n):
            s = graph.prob(a.s, b.s, f)
            q.prob(s)

            r = randint(1, self.r) + (random() < self.d) * self.r
            t += dist(a, q) / v

            a, b = b, Position(i, q.x, q.y, t, r)

            b.f = f
            self.p.append(b)

            if random() < self.d:
                s, f = graph.rand(b.s)
                v = self.v[f]

                q.prob(s)

                r = randint(1, self.r) + (random() < self.d) * self.r
                t += dist(a, q) / v

                a, b = b, Position(i, q.x, q.y, t, r)

                b.f = f
                self.p.append(b)
        return t

    # ---------------------------
    # создание треков человека

    def find(self, i):
        t = NOW + randint(0, self.t)  # время первого трека
        m = randint(1, self.m)  # количество треков

        d = self.t // m  # время между треками
        self.p.clear()

        s = [Point(0, 0) for k in range(self.k)]  # точки притяжения
        for q in s: q.rand()

        for k in range(m):
            t = self.track(t, i, rand(s)) + d

    # ---------------------------
    # сохранение в базу

    def save(self):
        position_collection.drop()
        p = [q.to_dict() for q in self.p]
        position_collection.insert_many(p)

    # ---------------------------
    # создаем поток данных и применяем к точкам обработчик

    def load(self, f):
        for d in position_collection.get():
            i = int(d['i'])
            x = float(d['x'])
            y = float(d['y'])
            r = float(d['r'])
            t = int(d['t'])

            q = Position(i, x, y, t, r)
            if inside(q): f(q)
