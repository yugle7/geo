# актуализация данных


# ---------------------------

class Actual:
    t = 0  # минимальное время

    # ---------------------------

    def find(self, points):
        return [q for q in points if q.t > self.t]
