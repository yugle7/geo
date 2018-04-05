# нормализация и подготовка данных для работы с ними

from base.logic import span, dist


# ---------------------------

class Outlier:
    p = []  # точки траектории

    k = 2  # во сколько раз путь через данную точку длиннее, чем напрямик
    v = 2000  # максимальная скорость

    span = None
    dist = None

    # ---------------------------

    def __init__(self):
        self.span = lambda x, y: span(self.p[x], self.p[y])
        self.dist = lambda x, y: dist(self.p[x], self.p[y])

    def load(self, p):
        self.p = p

    # ---------------------------
    # удаление выбросов

    def make(self, p):
        self.load(p)
        self.find()

    def find(self):
        i = 1
        while i < len(self.p) - 1:
            a = self.dist(i + 1, i)
            b = self.dist(i, i - 1)
            c = self.dist(i + 1, i - 1)

            if self.k * c < max(a, b) or b > self.v * self.span(i, i - 1):
                self.p.pop(i)
            else:
                i += 1
