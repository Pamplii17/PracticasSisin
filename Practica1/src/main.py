import pygame
import sys


class Main:

    def __init__(self):
        pass

    def ejecutarLinja(self):

        self.tablero = pantalla

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


main = Main()
main.ejecutarLinja()