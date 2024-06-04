import pygame
from ajustes import *
from portada import toleportada
from menu import tolemenu
from fondo import FondoBase, FondoMontañas
from pajaro import Pajaro, Vuelo
from shot import Mirilla, handle_crosshair, crosshair_img
from colision import handle_collisions
from decision import toledecision
from creditos import Creditos
from rondas import RondasJuego
import sys

WHITE = (255, 255, 255)

class Juego:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # Inicializa el mixer de pygame para reproducir sonidos
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
        self.vuelo = Vuelo(0, 600)
        self.pajaro = Pajaro()  # Inicializar el objeto Pajaro
        self.moving_sprites = pygame.sprite.Group(self.vuelo)
        self.font = pygame.font.Font(None, 35)
        self.rondas_juego = RondasJuego(self.vuelo)  # Instancia de RondasJuego

        self.balas_img = pygame.image.load("imagenes/bullet.png")
        self.balas_img = pygame.transform.scale(self.balas_img, (30, 30))  # Ajustar tamaño de la imagen de las balas

    def mostrar_contadores(self):
        # Mostrar contador de balas
        for i in range(self.num_balas):
            self.screen.blit(self.balas_img, (75 + i * 40, 70))  # Dibujar cada bala en una posición diferente

        # Mostrar contador de puntaje
        score_texto = f"{self.score}"
        score_renderizado = self.font.render(score_texto, True, (255, 255, 255))
        self.screen.blit(score_renderizado, (620, 70))

    def comprobar_fin_juego(self):
        if self.start_time is not None and pygame.time.get_ticks() - self.start_time > 8000:
            self.juego_terminado = True

    def handle_shooting(self, event):
        global can_shoot, last_shot_time
        current_time = pygame.time.get_ticks()
        if self.num_balas > 0:
            if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
                can_shoot = False
                last_shot_time = current_time
                print("Disparo registrado")
                mouse_pos = event.pos
                collision_pos = None  # Inicializamos la posición de la colisión como None
                if self.num_balas > 0:  # Verificamos nuevamente si hay balas disponibles
                    self.num_balas, self.score, collision_pos = handle_collisions(self.vuelo, self.mirilla, self.num_balas, self.score, mouse_pos)
                if collision_pos is not None:
                    self.reproducir_sonido_colision()  # Reproducir el sonido de colisión
                    self.pajaro.dibujar_explosion(self.screen, collision_pos)
                    self.pajaro.alive = False  # Marcar al pájaro como no vivo
                else:
                    self.reproducir_sonido_fallido()  # Reproducir el sonido de disparo fallido
                    self.num_balas -= 1  # Disminuir el contador de balas al fallar un disparo

                self.mirilla.shoot()

        if current_time - last_shot_time > 1500:  # Intervalo de medio segundo entre disparos
            can_shoot = True



    def mostrar_imagenes(self):
        # Mostrar la imagen de la ronda actual si corresponde
        self.rondas_juego.mostrar_ronda(self.screen)
        
        # Verificar si el contador de movimientos se reinicia
        if self.vuelo.obtener_contador_movimientos() == 4:
            print("Se ha completado una ronda. Reiniciando contador.")
            self.vuelo.contador_movimientos = 0
            self.rondas_juego.verificar_reinicio_contador()

    def reiniciar_pajaro(self):
        # Reinicia el estado del pájaro para permitir nuevas rondas
        if not self.vuelo.alive:
            print("Reiniciando el pájaro para una nueva ronda")
            self.vuelo = Vuelo(0, 600)
            self.moving_sprites = pygame.sprite.Group(self.vuelo)  # Crear un nuevo grupo de sprites
            self.vuelo.alive = True
            self.pajaro.explosion_frames = 0  # Reiniciar el contador de frames de la explosión

    def reproducir_sonido_colision(self):
        pygame.mixer.Sound("sonidos/pollo.mp3").play()

    def reproducir_sonido_fallido(self):
        pygame.mixer.Sound("sonidos/disparo.mp3").play()

    def run(self):
        mostrar_portada = toleportada(2)

        if mostrar_portada:
            iniciar_juego = tolemenu()

            if iniciar_juego:
                print("sisas")
                fondo = FondoBase()
                montañas = FondoMontañas()

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
                        self.handle_shooting(event)

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
                        self.screen.blit(fondo.image,fondo.rect)

                        if self.vuelo.contador_movimientos % 6 < 3:
                            self.vuelo.volar_derecha(0.30)
                        else:
                            self.vuelo.volar_izquierda(0.30)

                        mouse_pos = pygame.mouse.get_pos()
                        handle_crosshair(self.num_balas, self.mirilla, self.screen)

                        # Verificar si el pájaro está derribado y realizar acciones correspondientes
                        if not self.vuelo.alive:
                            print("El pájaro ha sido derribado")
                            self.num_balas, self.score, collision_pos = handle_collisions(self.vuelo, self.mirilla, self.num_balas, self.score, mouse_pos)
                            if collision_pos is not None:
                                self.pajaro.dibujar_explosion(self.screen, collision_pos)  # Dibujar la explosión en la posición de la colisión

                            if self.pajaro.is_explosion_finished():
                                self.reiniciar_pajaro()  # Reiniciar el pájaro para una nueva ronda

                        # Mostrar contadores de balas y puntaje
                        self.mostrar_contadores()
                        
                        # Actualizar y dibujar los sprites
                        self.moving_sprites.draw(self.screen)
                        self.moving_sprites.update(0.30)
                        
                        # Mostrar el fondo de las montañas
                        self.screen.blit(montañas.image, montañas.rect)
                        
                        # Mostrar la primera ronda
                        self.rondas_juego.mostrar_primera_ronda(self.screen)
                        
                        # Mostrar el contador de movimientos
                        texto = f"{self.vuelo.contador_movimientos}/3"
                        texto_renderizado = self.font.render(texto, True, (255, 255, 255))
                        self.screen.blit(texto_renderizado, (365, 70))
                        
                        # Mostrar imágenes adicionales
                        self.mostrar_imagenes()

                        # Actualizar la pantalla
                        pygame.display.update()

                    self.clock.tick(60)

if __name__ == "__main__":
    juego = Juego()
    juego.run()
