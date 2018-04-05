# точка с координатами

from base.logic import square


# ---------------------------

class Position:
    x = y = 0  # координаты

    t = 0  # время получения
    a = b = 0  # как долго стоял

    i = 0  # человек
    s = 0  # квадрат

    r = 0  # ошибка
    w = 1  # вес точки

    k = 0  # номер трека
    f = 0  # способ перемещения

    v = 0  # скорость
    m = 0  # момент времени

    def __init__(self, i, x, y, t, r):
        self.i = i
        self.x = x
        self.y = y
        self.t = self.a = self.b = t
        self.r = r

        square(self)

    # ---------------------------

    def to_dict(self):
        return {
            'i': self.i,
            'x': self.x,
            'y': self.y,
            't': self.t,
            'r': self.r,
        }

    # ---------------------------

    def weight(self):
        self.w = 10 / (10 + self.r)

    # ---------------------------
    # объединение двух точек в одну

    def merge(self, p):
        w = self.w + p.w

        self.x = (self.w * self.x + p.w * p.x) / w
        self.y = (self.w * self.y + p.w * p.y) / w
        self.t = (self.w * self.t + p.w * p.t) / w

        self.b = p.t

        self.r = self.r * p.r / (self.r + p.r)
        self.w = w

    # ---------------------------

    def show(self, show, color):
        show.point(self, color)
        show.circle(self, color)
