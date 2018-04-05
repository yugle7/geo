# трек человека

from base.const import GREEN, BLACK
from base.show import Show
from calc.moment import moment
from calc.vehicle import vehicle
from calc.active import active
from calc.velocity import velocity
from data.position import Position

from make.outlier import Outlier
from make.prune import Prune
from make.smooth import Smooth

# ---------------------------


smooth = Smooth()
prune = Prune()
outlier = Outlier()


# ---------------------------

class Track:
    p = []  # последовательность точек

    # ---------------------------

    def make(self):
        outlier.make(self.p)  # удаляем выбросы
        prune.make(self.p)  # прореживаем

        smooth.make(self.p)  # сглаживаем

        velocity.get(self.p)  # находим скорость в точках
        moment.get(self.p)  # определяем момент времени

        active.get(self.p)  # определяем тип места
        vehicle.get(self.p)  # определяем способ перемещения

    # ---------------------------

    def show(self, show):
        show.line(self.p, BLACK)
        for q in self.p:
            q.show(show)

    # ---------------------------

    def take(self):
        self.p = []

        for q in open('media/track.txt'):
            y, x, t, r = q[:-1].split('\t')
            x, y = float(x), float(y)
            t = int(t)
            r = float(r)
            self.p.append(Position(0, x, y, t, r))

    # ---------------------------
    # отображение траектории и результата ее обработки

    def demo(self):
        print('track')

        self.take()
        show = Show('n.jpg')

        self.show(show)
        self.make()

        show.line(self.p, GREEN)
        for q in self.p:
            show.point(q, BLACK)

        show.save('track.jpg')
        exit()
