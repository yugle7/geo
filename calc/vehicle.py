# задание карт с характеристиками перемещения

from base.const import *

from base.show import Show


# ----------------------------------

# 1. парковка
# 2. остановка
# 3. вестибюль

# 1. велосипед
# 2. транспорт
# 3. машина
# 4. пешком


# ----------------------------------


class Vehicle:
    s = {}  # вероятность способа перемещения
    q = 0.2  # минимальная вероятность перемещения

    f = []  # способы перемещения
    g = []  # места пересадок

    url = MEDIA + 'moves/'

    # ----------------------------------

    def __init__(self):
        self.f = ['car', 'bus', 'walk', 'bike']
        self.g = ['park', 'stop', 'metro']

    def take(self):
        for q in self.f + self.g:
            show = Show('moves/' + q + '.jpg')

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
    # вероятность

    def walk(self, p, i):
        if not i and any(q.v > V_WALK for q in p): return False
        for q in p: q.f = 'walk'

    def bike(self, p, i):
        if not i and any(q.v > V_BIKE for q in p): return False
        s = self.s['bike']

        n = len(p)
        while i < n and p[i].v < V_WALK:
            p[i].f = 'walk'
            i += 1
        j = i
        while j < n and (p[j] > V_WALK or s[p[j].s] > self.q):
            p[j].f = 'bike'
            j += 1

        return j == n or self.bus(p, j)

    def bus(self, p, i):
        if not i and any(q.v > V_BUS for q in p): return False
        s = self.s['bus']

        n = len(p)
        while i < n and p[i].v < V_WALK:
            p[i].f = 'walk'
            i += 1
        j = i
        while j < n and (p[j] > V_WALK or s[p[j].s] > self.q):
            p[j].f = 'bus'
            j += 1

        return j == n or self.bus(p, j)

    def car(self, p, i):
        s = self.s['car']

        n = len(p)
        while i < n and p[i].v < V_WALK:
            p[i].f = 'walk'
            i += 1
        j = i
        while j < n and (p[j] > V_WALK or s[p[j].s] > self.q):
            p[j].f = 'car'
            j += 1

        return j == n or self.car(p, j)

    # ----------------------------------
    # определяем способ перемещения

    def find(self, p):
        return self.walk(p, 0) or self.bike(p, 0) or self.bus(p, 0) or self.car(p, 0)

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

            show.save('moves/' + f + '.png')

    # ----------------------------------

    def save(self):
        for q in self.f + self.g:
            dst = open(self.url + q + '.csv', mode='w')
            dst.write('\t'.join(map(str, self.s[q])))
            dst.close()

    def load(self):
        for q in self.f + self.g:
            src = open(self.url + q + '.csv')
            self.s[q] = list(map(float, src.read().split('\t')))
            src.close()


# ----------------------------------

def demo(self):
    self.take()
    self.save()
    self.load()
    self.show()


# ----------------------------------

vehicle = Vehicle()
