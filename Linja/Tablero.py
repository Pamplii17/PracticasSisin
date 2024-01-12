from Celda import Celda
from Color import Color
from Pieza import Pieza

class Tablero:

    def __init__(self):

        self.tablero = []
        
        
    def mostrarTablero(self):

        for fila in range(8):
            for col in range(8):
                if self.tablero[fila][col].estaVacia():
                    print("- ", end="")
                else:
                    print(self.tablero[fila][col].obtenerPieza().piezaToString(),end="")
            
            print("")

    def incializarTablero(self):

        for fila in range(8):
            self.tablero.append([])
            for col in range(8):

                if col == 0:
                    self.tablero[fila].append(Celda(0,fila,col))
                    self.colocar(Pieza(Color.NEGRO), fila, col)
                elif col == 7:
                    self.tablero[fila].append(Celda(0,fila,col))
                    self.colocar(Pieza(Color.ROJO), fila, col)

    def colocar(self, pieza, fila, col):
        self.tablero[fila][col].colocarPieza(pieza)

tablero = Tablero()
tablero.incializarTablero()
tablero.mostrarTablero()