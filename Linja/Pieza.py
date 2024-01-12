from Color import Color

class Pieza:

    def __init__(self, color):
        self.color = color

    def obtenerColor(self):
        return self.color

    def piezaToString(self):
        if self.color == Color.ROJO:
            return "R"
        else:
            return "N"