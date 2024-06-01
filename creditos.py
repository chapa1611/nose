import pygame
from ajustes import *

class Creditos:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.creditos_mostrados = False

    def mostrar_creditos(self):
        creditos = pygame.image.load('imagenes/creditos.jpg')
        self.screen.blit(creditos, (0, 0))
        pygame.display.flip()
        self.creditos_mostrados = True