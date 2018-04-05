# основные операции

from random import randint
from base.const import *


# ---------------------------
# определение квадрата точки

def square(q):
    x = int((q.x - MAP_X) / MAP_DX)
    y = int((q.y - MAP_Y) / MAP_DY)
    q.s = y * MAP_COLS + x
    assert 0 <= q.s < MAP_N


# ---------------------------
# проверка находится ли точка внутри карты

def inside(q):
    return MAP_X <= q.x < MAP_A and MAP_Y <= q.y < MAP_B


# ---------------------------
# возвращает случайный элемент массива

def rand(p):
    return p[randint(0, len(p) - 1)] if p else None


# ---------------------------
# работа с точками

dist = lambda a, b: ((LAT * (a.x - b.x)) ** 2 + (LON * (a.y - b.y)) ** 2) ** 0.5
span = lambda a, b: b.a - a.b
