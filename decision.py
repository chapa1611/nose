import pygame
from pygame.locals import *
from ajustes import *
import sys

class Decision(pygame.sprite.Sprite):
    def __init__(self, fondo_img, boton1_img, boton2_img):
        super().__init__()
        self.fondo_decision = pygame.image.load(fondo_img)
        self.image = self.fondo_decision
        self.rect = self.image.get_rect()

        self.boton1_img = pygame.image.load(boton1_img)
        self.boton1_rect = self.boton1_img.get_rect()
        self.boton1_rect.midtop = (self.rect.width // 2, 290)

        self.boton2_img = pygame.image.load(boton2_img)
        self.boton2_rect = self.boton2_img.get_rect()
        self.boton2_rect.midtop = (self.rect.width // 2, 450)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.boton1_img, self.boton1_rect)
        screen.blit(self.boton2_img, self.boton2_rect)

def toledecision():
    pygame.init()
    Tamaño_pantalla = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(Tamaño_pantalla)

    fondo_img = "imagenes/decisionMenu.jpg"
    boton1_img = "imagenes/keeppla.png"
    boton2_img = "imagenes/noout.png"

    decision_menu = Decision(fondo_img, boton1_img, boton2_img)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if decision_menu.boton1_rect.collidepoint(event.pos):
                    return "continuar"
                elif decision_menu.boton2_rect.collidepoint(event.pos):
                    return "creditos"

        decision_menu.draw(screen)
        pygame.display.update()
