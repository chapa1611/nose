import pygame
from ajustes import *
from pygame.locals import *

class Menu(pygame.sprite.Sprite):
    def __init__(self, fondo_img, boton_img):
        super().__init__()
        self.fondo_menu = pygame.image.load(fondo_img)  
        self.image = self.fondo_menu
        self.rect = self.image.get_rect()

        self.boton_img = pygame.image.load(boton_img)
        self.boton_rect = self.boton_img.get_rect()
        self.boton_rect.midtop = (self.rect.width // 2, 80) 

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.boton_img, self.boton_rect)

def tolemenu():
    pygame.init()
    Tamaño_pantalla = (WIDTH, HEIGHT) 
    screen = pygame.display.set_mode(Tamaño_pantalla)

    fondo_img = "imagenes/menu.jpg"
    boton_img = "imagenes/boton.jpg"

    
    menu_inicio = Menu(fondo_img, boton_img)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
                if menu_inicio.boton_rect.collidepoint(event.pos): 
                    return True  

        menu_inicio.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    tolemenu()