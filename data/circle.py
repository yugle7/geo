# область поиска в форме круга

from base.const import BLUE, BLACK, GREEN, RED, MEDIA
from base.logic import dist
from base.point import Point
from base.show import Show


# ---------------------------

class Circle:
    x = y = 0  # координаты
    r = 0  # радиус

    url = MEDIA + 'area/'

    # ---------------------------

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    # ---------------------------
    # точка внутри окружности

    def find(self, q):
        return dist(q, self) < self.r

    # ---------------------------
    # нарисовать на карте

    def show(self, show):
        show.circle(self, BLUE)
        show.point(self, BLACK)

    # ---------------------------
    # тестовое отображение

    def take(self):
        x, y, r = open(self.url + 'circle.txt').readline().split()
        self.x, self.y, self.r = float(x), float(y), int(r)

        p = []

        for q in open(self.url + 'points.txt'):
            x, y = q[:-1].split('\t')
            p.append(Point(float(x), float(y)))

        return p

    # ---------------------------

    def demo(self):
        print('circle')

        show = Show(self.url + 'map.jpg')
        p = self.take()

        for q in p:
            t = GREEN if self.find(q) else RED
            q.show(show, t, None)

        self.show(show)
        show.save(self.url + 'circle.jpg')
        exit()
