# обертка над изображением

from PIL import Image, ImageDraw
from base.const import *


# ---------------------------


class Show:
    image = None
    draw = None

    # ---------------------------

    def __init__(self, src):
        self.image = Image.open(SHOW + src)
        self.draw = ImageDraw.Draw(self.image)

        self.width = self.image.size[0]
        self.height = self.image.size[1]

    def save(self, dst):
        if dst: self.image.save(SHOW + dst, "JPEG")

        del self.image
        del self.draw

    # ---------------------------
    # отображение координат на картинку

    def r(self, q):
        return int(self.height * q.r / MAP_HEIGHT)

    def xy(self, q):
        x = int(self.width * (q.x - MAP_X) * LAT / MAP_WIDTH)
        y = int(self.height * (MAP_Y - q.y) * LON / MAP_HEIGHT)

        return x, y

    # ---------------------------
    # отображение фигур на картинке

    def circle(self, q, color):
        x, y = self.xy(q)
        r = self.r(q)

        p = [(x - r, y - r), (x + r, y + r)]
        self.draw.ellipse(p, outline=color)

    def point(self, q, color):
        x, y = self.xy(q)

        p = [(x - 2, y - 2), (x + 2, y + 2)]
        self.draw.ellipse(p, fill=color)

    def polygon(self, p, color):
        p = [self.xy(q) for q in p]
        self.draw.polygon(p, color)

    def line(self, p, color):
        p = [self.xy(q) for q in p]
        self.draw.line(p, color)
