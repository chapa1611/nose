import pygame
from ajustes import *
from portada import *
from menu import *
from fondo import *  
from pajaro import *
from shot import *
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

    def comprobar_fin_juego(self):
        # Solo verificar el tiempo si el juego ha comenzado
        if self.start_time is not None and pygame.time.get_ticks() - self.start_time > 8000:  # 10 segundos
            self.juego_terminado = True

    def mostrar_creditos(self):
        self.screen.blit(self.creditos, (0, 0))
        pygame.display.flip()
        self.creditos_mostrados = True

    def handle_shooting(self, event):
        global can_shoot, last_shot_time
        current_time = pygame.time.get_ticks()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and can_shoot:
            # Implementar la lógica para disparar
            can_shoot = False
            last_shot_time = current_time
            print("Disparo")

        if current_time - last_shot_time > 500:  # Intervalo de medio segundo entre disparos
            can_shoot = True

    def run(self):
        mostrar_portada = toleportada(2)

        if mostrar_portada:
            iniciar_juego = tolemenu()

            if iniciar_juego:
                print("sisas")
                
                fondo = FondoBase()
                montañas = FondoMontañas()

                moving_sprites = pygame.sprite.Group()
                vuelo = Vuelo(0, 700)
                moving_sprites.add(vuelo)

                vuelo.movimiento()  # Iniciar la animación

                global can_shoot, last_shot_time
                can_shoot = True
                last_shot_time = 0

                # Inicializar el temporizador al iniciar el juego
                self.start_time = pygame.time.get_ticks()

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        self.handle_shooting(event)

                    if self.juego_terminado:
                        if not self.creditos_mostrados:
                            decision = toledecision()
                            if decision == "continuar":
                                # Reiniciar el juego
                                self.juego_terminado = False
                                self.start_time = pygame.time.get_ticks()
                            elif decision == "creditos":
                                # Mostrar los créditos
                                creditos = Creditos()
                                creditos.mostrar_creditos()
                                pygame.time.wait(5000)  # Mostrar créditos por 5 segundos
                                pygame.quit()
                                sys.exit()
                    else:
                        self.comprobar_fin_juego()
                        self.screen.fill(WHITE)
                        self.screen.blit(fondo.image, fondo.rect)

                        # Alternar entre volar_derecha y volar_izquierda basado en el contador de movimientos
                        if vuelo.contador_movimientos % 6 < 3:
                            vuelo.volar_derecha(0.30)
                            print("derecha")
                        else:
                            vuelo.volar_izquierda(0.30)
                            print("izquierda")

                        moving_sprites.draw(self.screen)
                        moving_sprites.update(0.30)
                        
                        self.screen.blit(montañas.image, montañas.rect)
                        pygame.display.update()
                    
                    self.clock.tick(60)

if __name__ == "__main__":
    juego = Juego()
    juego.run()
