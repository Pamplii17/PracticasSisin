import pygame

from const import *
from board import Board
from piece import *
from square import *

class Game:

    def __init__(self):
        self.board = Board()

    def mostrarTablero(self,surface):
        for row in range(FILAS):
            for col in range(COLUMNAS):
                if (row + col) % 2 == 0:
                    color = (235,235,200)  # verde claro
                else:
                    color = (119,154,88)   #verde oscuro

                rect = (col * SQUARESIZE, row * SQUARESIZE, SQUARESIZE, SQUARESIZE)

                pygame.draw.rect(surface,color,rect)
    
    def mostrarPiezas(self,surface):
        for row in range(FILAS):
            for col in range(COLUMNAS):
                if self.board.squares[row][col].hasPiece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img_center = col * SQUARESIZE + SQUARESIZE // 2, row * SQUARESIZE + SQUARESIZE // 2
                    piece.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img, piece.texture_rect)