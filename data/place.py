# точка притяжения


# ---------------------------

class Place:
    p = []  # точки вокруг

    i = 0  # человек
    f = 0  # тип места
    g = 0  # что делает

    x = y = 0  # координаты
    r = 0  # радиус

    # ---------------------------

    def __init__(self, q):
        self.i = q.i

        self.x, self.y = q.x, q.y
        self.r = 1

    # ---------------------------
    # объединение двух точек притяжения в одну

    def merge(self, p):
        r = self.r + p.r

        self.x = (self.r * self.x + p.r * p.x) / r
        self.y = (self.r * self.y + p.r * p.y) / r

        self.r = r

    # ---------------------------
    # отображение данных

    def show(self, show, color):
        show.circle(self, color)
        show.point(self, color)
