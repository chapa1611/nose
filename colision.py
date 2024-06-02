import pygame

def handle_collisions(pajaro, moving_sprites, mirilla, num_balas, score, mouse_pos):
    if pajaro.get_hitbox().collidepoint(mouse_pos):
        pajaro.alive = False
        num_balas -= 1
        score += 1
    return num_balas, score

class Colision:
    def __init__(self, pajaro):
        self.pajaro = pajaro

    def check_collision(self, mouse_pos):
        if self.pajaro.get_hitbox().collidepoint(mouse_pos):
            self.pajaro.alive = False
