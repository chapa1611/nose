def handle_collisions(vuelo, mirilla, num_balas, score, mouse_pos):
    # Verificar si el pájaro está dentro del área de la mirilla
    if vuelo.get_hitbox().collidepoint(mouse_pos):
        # Incrementar el puntaje si hay una colisión exitosa
        score += 50
        # Marcar al pájaro como derribado
        vuelo.alive = False
        print("¡Pájaro derribado!")
        # Obtener la posición actual del pájaro
        collision_pos = vuelo.rect.topleft
        return num_balas, score, collision_pos

    # Si no hubo colisión, devolver los valores originales sin restar balas
    return num_balas, score, None
