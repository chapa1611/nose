import pygame
import time

WHITE = (255, 255, 255)

# Cargar la imagen de la mirilla
crosshair_img = pygame.image.load("imagenes/bullseye.png")

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