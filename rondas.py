# archivo rondas.py
import pygame

class RondasJuego:
    def __init__(self, vuelo):
        self.vuelo = vuelo
        self.imagenes_rondas = [pygame.image.load(f"imagenes/ronda{i}.png").convert_alpha() for i in range(1, 4)]
        self.imagen_actual = 0
        self.mostrar_imagen = True
        self.tiempo_inicio = pygame.time.get_ticks()
        self.mostrar_primera_imagen = True

    def verificar_reinicio_contador(self):
        if self.vuelo.obtener_contador_movimientos() == 0:
            self.mostrar_imagen = True
            self.tiempo_inicio = pygame.time.get_ticks()
            self.imagen_actual = min(self.imagen_actual + 1, len(self.imagenes_rondas) - 1)

    def mostrar_ronda(self, screen):
        if self.mostrar_imagen:
            screen.blit(self.imagenes_rondas[self.imagen_actual], (250, 205))
            if pygame.time.get_ticks() - self.tiempo_inicio > 2000:  # Mostrar la imagen por 2 segundos
                self.mostrar_imagen = False

    def mostrar_primera_ronda(self, screen):
        if self.mostrar_primera_imagen:
            screen.blit(self.imagenes_rondas[0], (250, 205))
            if pygame.time.get_ticks() - self.tiempo_inicio > 2000:  # Mostrar la imagen por 2 segundos
                self.mostrar_primera_imagen = False
