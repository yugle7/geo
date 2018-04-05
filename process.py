# основной алгоритм получения и обработки данных

from base.mongo import *
from base.logic import xy2s, span

from data.person import Person
from data.position import Position
from data.track import outlier, smooth, prune

from calc.moment import moment
from calc.velocity import velocity
from calc.vehicle import vehicle


# ----------------------------------

class Process:
    p = []  # люди
    k = 0  # номер трека

    t = 60  # максимальное время и расстояние между двумя соседними точками
    d = 1000

    n = 100000  # по сколько точек кладем в базу

    # ----------------------------------

    def __init__(self, k):
        self.p = [Person() for i in range(k)]
        temp_collection.drop()

    # ----------------------------------
    # точки притяжения человека

    def make(self, q):
        person = self.p[q.i]

        if person.p:

            if span(q, person.p) > self.t:  # трек оборвался
                self.temp2data(q.k)  # перекалдываем его

                q.k = self.k  # начинаем новый трек
                self.k += 1

            else:
                q.k = person.p.k

        else:
            q.k = self.k  # начинаем новый трек
            self.k += 1

        person.p = q
        self.temp(q)  # сохраняем позицию

    # ----------------------------------
    # обработка трека

    def track(self, p):
        for q in p: xy2s(q)  # находим квадрат

        outlier.make(p)  # удаляем выбросы
        prune.make(p)  # прореживаем
        smooth.make(p)  # сглаживаем

        moment.get(p)  # определяем момент
        velocity.find(p)  # вычисляем скорости

        vehicle.find(p)  # вычисляем способ перемещения

    # ----------------------------------

    def temp(self, q):
        d = {
            'i': q.i,
            'x': q.x,
            'y': q.y,
            't': q.t,
            'e': q.e,
            'k': q.k,
        }
        temp_collection.insert_one(d)

    # ----------------------------------
    # перекладываем трек

    def temp2data(self, i):
        p = []

        for d in temp_collection.find({'i': i}):
            q = Position(d['i'], d['x'], d['y'], d['t'], d['e'])
            p.append(q)

        self.track(p)
        data = []

        for q in p:
            d = {
                'i': q.i,
                'x': q.x,
                'y': q.y,
                't': q.t,
                'r': q.r,
                'k': q.k,
                'v': q.v,
                'm': q.m,
            }
            data.append(d)

        position_collection.insert_many(data)
        temp_collection.remove({'i': i})  # удаляем
