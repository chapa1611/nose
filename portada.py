import pygame
from ajustes import *
from pygame.locals import *

class Portada(pygame.sprite.Sprite):
    def __init__(self, fondo_img):
        super().__init__()
        self.fondo_portada = pygame.image.load("imagenes/portada.jpg")  # Carga la imagen de fondo
        self.image = self.fondo_portada
        self.rect = self.image.get_rect()

def toleportada(tiempo_portada):
    pygame.init()
    Tamaño_pantalla = (WIDTH, HEIGHT)  
    screen = pygame.display.set_mode(Tamaño_pantalla)

    fondo_img = pygame.image.load("imagenes/portada.jpg")

    # crea una instancia del menú con la imagen de fondo
    portada_inicio = Portada(fondo_img)

    tiempo_inicio = pygame.time.get_ticks()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(portada_inicio.image, portada_inicio.rect)
        pygame.display.update()
        
        # Verifica si ha pasado el tiempo de la portada
        if pygame.time.get_ticks() - tiempo_inicio > tiempo_portada * 1000:
            return True

        tecla = pygame.key.get_pressed()
        if tecla [K_RETURN]: 
            return True

if __name__ == "__main__":
    toleportada(2)