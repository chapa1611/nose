import pygame
import time

class Mirilla(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

    def shoot(self):
        print("Mirilla ha disparado")

WHITE = (255, 255, 255)

# Cargar la imagen de la mirilla y escalarla a un tamaño más pequeño
crosshair_img = pygame.image.load("imagenes/bullseye.png")
# Escalar la imagen a un tamaño específico, por ejemplo, la mitad de su tamaño original
new_width = crosshair_img.get_width() // 5
new_height = crosshair_img.get_height() // 5
crosshair_img = pygame.transform.scale(crosshair_img, (new_width, new_height))

can_shoot = True
last_shot_time = 0

def draw_crosshair(screen, x, y):
    screen.blit(crosshair_img, (x - crosshair_img.get_width() // 2, y - crosshair_img.get_height() // 2))

def handle_shooting(event, screen):
    global can_shoot, last_shot_time

    if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
        print("Disparo registrado")
        can_shoot = False
        last_shot_time = time.time()
        mouse_x, mouse_y = event.pos
        draw_crosshair(screen, mouse_x, mouse_y)
        pygame.display.flip()
    
    if not can_shoot and time.time() - last_shot_time >= 3:
        can_shoot = True

def handle_crosshair(num_balas, mirilla, pantalla):
    # Obtener la posición del cursor del mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Actualizar la posición de la mirilla
    mirilla.rect.center = (mouse_x, mouse_y)

    # Dibujar la mirilla en la pantalla
    pantalla.blit(mirilla.image, mirilla.rect)

    # Verificar si se ha hecho clic para disparar
    global can_shoot, last_shot_time
    if pygame.mouse.get_pressed()[0] and can_shoot:
        print("Disparo registrado")
        can_shoot = False
        last_shot_time = time.time()
        draw_crosshair(pantalla, mouse_x, mouse_y)
        pygame.display.flip()

    # Verificar el tiempo transcurrido desde el último disparo
    if not can_shoot and time.time() - last_shot_time >= 3:
        can_shoot = True
