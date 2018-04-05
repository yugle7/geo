# область поиска в форме круга

from base.const import BLUE, BLACK, GREEN, RED
from base.logic import dist
from base.point import Point
from base.show import Show


# ---------------------------

class Circle:
    x = y = 0  # координаты
    r = 0  # радиус

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
        self.r = 200
        self.y, self.x = 55.821098, 37.640564

        p = []

        for q in open('media/points.txt'):
            x, y = q[:-1].split('\t')
            p.append(Point(float(x), float(y)))

        return p

    def demo(self):
        print('circle')

        show = Show('n.jpg')
        p = self.take()

        for q in p:
            t = GREEN if self.find(q) else RED
            q.show(show, t, None)

        self.show(show)
        show.save('area/circle.jpg')
