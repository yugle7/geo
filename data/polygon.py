# присутствие внутри полигона

from cmath import atan

from base.const import GREEN, RED, BLACK, BLUE, MEDIA
from base.point import Point
from base.show import Show


# ---------------------------

class Polygon:
    p = []
    e = 0.0001

    url = MEDIA + 'area/'

    # ---------------------------
    # точка внутри полигона

    def find(self, q):
        if len(self.p) < 3:
            return False
        s = 0

        c = self.p[-1]
        b = Point(c.x - q.x, c.y - q.y)

        for c in self.p:
            a = Point(c.x - q.x, c.y - q.y)

            d = b.x * a.y - a.x * b.y
            xy = a.x * b.x + a.y * b.y

            s += atan((b.x * b.x + b.y * b.y - xy) / d)
            s += atan((a.x * a.x + a.y * a.y - xy) / d)

            b = a

        return abs(s) > self.e

    # ---------------------------

    def show(self, show):
        for q in self.p:
            show.r(q)

        show.polygon(self.p, BLACK)
        for q in self.p:
            show.point(q, BLUE)

    # ---------------------------
    # тестовое отображение

    def take(self):
        self.p = []
        for q in open(self.url + 'polygon.txt'):
            x, y = q[:-1].split('\t')
            self.p.append(Point(float(x), float(y)))

        p = []

        for q in open(self.url + 'points.txt'):
            x, y = q[:-1].split('\t')
            p.append(Point(float(x), float(y)))

        return p

    # ---------------------------

    def demo(self):
        print('polygon')

        show = Show(self.url + 'map.jpg')
        p = self.take()

        for q in p:
            t = GREEN if self.find(q) else RED
            q.show(show, t)

        self.show(show)
        show.save(self.url + 'polygon.jpg')
        exit()
