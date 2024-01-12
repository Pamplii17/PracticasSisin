class Celda:

    def __init__(self,valorCelda, fila, columna):
        self.valorCelda = valorCelda
        self.pieza = []
        self.fila = fila
        self.columna = columna

    def obtenerFila(self):
        return self.fila
    
    def obtenerColumna(self):
        return self.columna

    def obtenerPieza(self):
        return self.pieza

    def colocarPieza(self,pieza):
        self.pieza.append(pieza)

    def obtenerValorCelda(self):
        return self.valorCelda

    def numeroPiezas(self, color):
        contador = 0

        for pieza in self.pieza:
            if pieza.color is color:
                contador +=1

        return contador

    def estaVacia(self):
        if len(self.pieza) == 0:
            return True
        else:
            return False

    

import unittest
from Celda import Celda  # Asegúrate de importar la clase Celda desde tu archivo

class TestCelda(unittest.TestCase):

    def setUp(self):
        self.celda = Celda(1, 'pieza_prueba', 0, 0)

    def test_obtenerFila(self):
        self.assertEqual(self.celda.obtenerFila(), 0)

    def test_obtenerColumna(self):
        self.assertEqual(self.celda.obtenerColumna(), 0)

    def test_obtenerPieza(self):
        self.assertEqual(self.celda.obtenerPieza(), 'pieza_prueba')

    def test_colocarPieza(self):
        self.celda.colocarPieza('nueva_pieza')
        self.assertEqual(self.celda.obtenerPieza(), 'nueva_pieza')

    def test_obtenerValorCelda(self):
        self.assertEqual(self.celda.obtenerValorCelda(), 1)

if __name__ == '__main__':
    unittest.main()
