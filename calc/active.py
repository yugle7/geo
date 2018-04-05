# определение характеристик точек притяжения

from base.const import *

from base.mongo import active_collection
from base.point import Point
from base.show import Show


# ----------------------------------

# 1. парк
# 2. дорога
# 3. дома
# 4. двор

# 1. работа
# 2. проживание
# 3. посещение
# 4. перемещение

# ----------------------------------

class Active:
    s = {}  # вероятность места и активности

    a = {}  # если позиция в точке притяжения
    b = {}  # в другом месте

    f = []  # типы местности
    g = []  # типы активности

    url = MEDIA + 'active/'

    # ----------------------------------

    def __init__(self):
        self.f = ['home', 'yard', 'road', 'park']
        self.g = ['work', 'live', 'walk']

    # ----------------------------------
    # берем распределение вероятности типов мест

    def take(self):
        for q in self.f + self.g:
            show = Show(self.url + q + '.jpg')

            pix = show.image.load()
            d = 256 * 3

            p = [0] * MAP_N
            n = [0] * MAP_N

            for i in range(show.width):
                for j in range(show.height):
                    a = pix[i, j][0]
                    b = pix[i, j][1]
                    c = pix[i, j][2]

                    x = int(MAP_COLS * i / show.width)
                    y = int(MAP_ROWS * j / show.height)
                    s = y * MAP_COLS + x

                    p[s] += 1 - (a + b + c) / d
                    n[s] += 1

            self.s[q] = [a / b for a, b in zip(p, n)]

            show.save(None)

    # ----------------------------------
    # определяем место точки притяжения

    def find(self, i, c, p, place):
        s, place.f = max((self.s[f][place.s], f) for f in self.f)

        t = []


        for g in self.g:
            x = y = 0

            for j, d in enumerate(p):
                if c[j] == i:
                    x += self.d[d.m].x
                else:
                    y += self.d[d.m].y

            t.append((x - y, g))

        s, place.g = max(t)

    # ----------------------------------
    # отображение

    def show(self):
        for f in self.f:
            show = Show('n.jpg')
            pix = show.image.load()

            for i in range(show.width):
                for j in range(show.height):
                    a = pix[i, j][0]
                    b = pix[i, j][1]
                    c = pix[i, j][2]

                    x = int(MAP_COLS * i / show.width)
                    y = int(MAP_ROWS * j / show.height)
                    s = y * MAP_COLS + x

                    q = 1 - self.s[f][s]

                    a = a * q
                    b = b * q
                    c = c * q

                    show.draw.point((i, j), (int(a), int(b), int(c)))

            show.save(self.url + f + '.png')

    # ----------------------------------

    def save(self):
        for q in self.f + self.g:
            dst = open(self.url + q + '.csv', mode='w')
            dst.write('\t'.join(map(str, self.s[q])))
            dst.close()

        for g in self.g:
            active_collection[g].drop()
            d = [{'x': q.x, 'y': q.y} for q in self.d]
            active_collection[g].insert_many(d)

    def load(self):
        for q in self.f + self.g:
            src = open(self.url + q + '.csv')
            self.s[q] = list(map(float, src.read().split('\t')))
            src.close()

        for g in self.g:
            self.d = [Point(d['x'], d['y']) for d in active_collection[g].find()]

    # ----------------------------------

    def demo(self):
        self.take()
        self.save()
        self.load()
        self.show()


# ----------------------------------

active = Active()
