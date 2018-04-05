# прореживание точек

from base.logic import span, dist


# ---------------------------

class Prune:
    p = []  # точки траектории

    t = 10  # минимальное время между соседними точками
    d = 90  # минимальное расстояние между соседними точками

    # ---------------------------

    def __init__(self):
        self.span = lambda x, y: span(self.p[x], self.p[y])
        self.dist = lambda x, y: dist(self.p[x], self.p[y])

    def load(self, p):
        self.p = p
        for q in self.p: q.weight()

    # ---------------------------

    def make(self, p):
        self.load(p)
        self.find()

    # ---------------------------

    def find(self):

        i = 0
        while i < len(self.p) - 1:
            q = self.p[i]

            while i + 1 < len(self.p):
                if self.span(i, i + 1) > self.t or self.dist(i, i + 1) > self.d:
                    break
                q.merge(self.p.pop(i))

            self.p[i] = q
            i += 1
