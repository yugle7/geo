# точка с координатами

from random import randint, random
from base.const import *


# ---------------------------

class Point:
    x = y = 0  # координаты

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # ---------------------------
    # нарисовать на карте

    def show(self, show, color):
        show.point(self, color)

    # ---------------------------
    # случайная точка на карте

    def rand(self):
        self.x = MAP_X + (randint(0, MAP_COLS) + random()) * MAP_DX
        self.y = MAP_Y + (randint(0, MAP_ROWS) + random()) * MAP_DY

    # ---------------------------
    # случайная точка в квадрате

    def prob(self, s):
        y, x = divmod(s, MAP_N)

        self.x = MAP_X + MAP_DX * (x + random())
        self.y = MAP_Y + MAP_DY * (y + random())
