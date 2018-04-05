# основные константы

from cmath import cos, pi

# ---------------------------

# MAP_X = 36.23243  # координаты левого верхнего угда карты
# MAP_Y = 57.34534

# MAP_WIDTH = 30454  # размеры карты в метрах
# MAP_HEIGHT = 41122

MAP_Y = 55.827488
MAP_X = 37.630752

MAP_WIDTH = 1460
MAP_HEIGHT = 1130

# ---------------------------

LON = 111111  # метров в одном градусе по долготе (в центре карты)
MAP_CY = MAP_Y + MAP_HEIGHT / (2 * LON)
LAT = LON * cos(pi * MAP_CY / 180)  # метров в одном градусе по широте
MAP_CX = MAP_X + MAP_WIDTH / (2 * LAT)

# ---------------------------

MAP_STEP = 100  # шаг в метрах

MAP_DX = MAP_STEP / LAT
MAP_DY = MAP_STEP / LON

MAP_ROWS = MAP_HEIGHT // MAP_STEP  # размеры карты
MAP_COLS = MAP_WIDTH // MAP_STEP

MAP_A = MAP_X + MAP_DX * MAP_COLS
MAP_B = MAP_Y + MAP_DY * MAP_ROWS

MAP_N = MAP_COLS * MAP_ROWS

# ---------------------------

NOW = 1521712471

# ---------------------------
# цвета

RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)
WHITE = (0, 0, 0)
YELLOW = (0, 0, 0)

# ---------------------------
# пути

SHOW = 'show/'
MEDIA = 'media/'

# ---------------------------
# скорости

STOP = 1.5
WALK = 5
BIKE = 15
BUS = 40
CAR = 70
