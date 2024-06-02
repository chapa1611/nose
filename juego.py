import pygame
from ajustes import *
from portada import *
from menu import *
from fondo import *
from pajaro import *
from shot import *
from colision import *
from decision import toledecision
from creditos import Creditos
import sys

class Juego:
    def __init__(self):
        pygame.init()
        self.Tamaño_pantalla = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.Tamaño_pantalla)
        pygame.display.set_caption(titulo)
        self.clock = pygame.time.Clock()
        self.juego_terminado = False
        self.creditos_mostrados = False
        self.start_time = None
        self.num_balas = 3
        self.score = 0
        self.mirilla = None
        self.vuelo = None
        self.moving_sprites = None

    def comprobar_fin_juego(self):
        if self.start_time is not None and pygame.time.get_ticks() - self.start_time > 8000:
            self.juego_terminado = True

    def mostrar_creditos(self):
        self.screen.blit(self.creditos, (0, 0))
        pygame.display.flip()
        self.creditos_mostrados = True

    def handle_shooting(self, event, mirilla):
        global can_shoot, last_shot_time
        current_time = pygame.time.get_ticks()
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            can_shoot = False
            last_shot_time = current_time
            print("Disparo registrado")
            mouse_pos = event.pos
            self.num_balas, self.score = handle_collisions(self.vuelo, self.moving_sprites, mirilla, self.num_balas, self.score, mouse_pos)
            mirilla.shoot()

        if current_time - last_shot_time > 500:  # Intervalo de medio segundo entre disparos
            can_shoot = True

    def run(self):
        mostrar_portada = toleportada(2)

        if mostrar_portada:
            iniciar_juego = tolemenu()

            if iniciar_juego:
                fondo = FondoBase()
                montañas = FondoMontañas()

                self.moving_sprites = pygame.sprite.Group()
                self.vuelo = Vuelo(0, 700)
                self.moving_sprites.add(self.vuelo)

                self.mirilla = Mirilla(crosshair_img)
                self.vuelo.movimiento()

                global can_shoot, last_shot_time
                can_shoot = True
                last_shot_time = 0

                self.start_time = pygame.time.get_ticks()

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        self.handle_shooting(event, self.mirilla)

                    if self.juego_terminado:
                        if not self.creditos_mostrados:
                            decision = toledecision()
                            if decision == "continuar":
                                self.juego_terminado = False
                                self.start_time = pygame.time.get_ticks()
                            elif decision == "creditos":
                                creditos = Creditos()
                                creditos.mostrar_creditos()
                                pygame.time.wait(5000)
                                pygame.quit()
                                sys.exit()
                    else:
                        self.comprobar_fin_juego()
                        self.screen.fill(WHITE)
                        self.screen.blit(fondo.image, fondo.rect)

                        if self.vuelo.contador_movimientos % 6 < 3:
                            self.vuelo.volar_derecha(0.30)
                        else:
                            self.vuelo.volar_izquierda(0.30)

                        # Obtener la posición del mouse
                        mouse_pos = pygame.mouse.get_pos()
                        handle_crosshair(self.num_balas, self.mirilla, self.screen)

                        if not self.vuelo.alive:
                            print("El pájaro ha sido derribado")
                            self.vuelo.caer()  # Hacer que el pájaro caiga

                        self.moving_sprites.draw(self.screen)
                        self.moving_sprites.update(0.30)

                        self.screen.blit(montañas.image, montañas.rect)
                        pygame.display.update()

                    self.clock.tick(60)

if __name__ == "__main__":
    juego = Juego()
    juego.run()
