import pygame
from ajustes import *

class FondoBase(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fondo = pygame.image.load("imagenes/2.png")  #imagen fondo base
        self.image = self.fondo
        self.rect = self.image.get_rect()

class FondoMontañas(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.montañas = pygame.image.load("imagenes/montañas.png")  #imagen fondo base
        self.image = self.montañas
        self.rect = self.image.get_rect()

def mostrar_fondo():
    pygame.init()
    Tamaño_pantalla = (WIDTH, HEIGHT)  
    screen = pygame.display.set_mode(Tamaño_pantalla)

    # crea una instancia del fondo estático
    fondo = FondoBase()
    montañas = FondoMontañas()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(fondo.image, fondo.rect)
        screen.blit(montañas.image, montañas.rect)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    mostrar_fondo()