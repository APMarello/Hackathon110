"""Pygame tutorial."""

import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

pygame.mouse.set_visible(False)

WHITE = (255, 255, 255)
GREEN = (86, 125, 70)
BLACK = (0, 0, 0)

SCREEN_1_BARRIER_HORIZONTAL = pygame.Rect(300, 300, 600, 20)
SCREEN_1_BARRIER_VERTICAL = pygame.Rect(300, 200, 20, 100)
hit_object = False


FPS = 60
VEL = 5
PLAYER_IMAGE = pygame.image.load(os.path.join('game_assets', 'player.png'))


def draw_window(player, PLAYER):   
    WIN.fill(GREEN)
    WIN.blit(PLAYER, (player.x, player.y))
    pygame.draw.rect(WIN, BLACK, SCREEN_1_BARRIER_HORIZONTAL)
    pygame.draw.rect(WIN, BLACK, SCREEN_1_BARRIER_VERTICAL)
    pygame.display.update()


def player_handle_movement(keys_pressed, player, rotate_angle) -> int:
    if keys_pressed[pygame.K_a] and player.x - VEL > 0 and not (player.colliderect(SCREEN_1_BARRIER_HORIZONTAL) and player.colliderect(SCREEN_1_BARRIER_VERTICAL)):  # LEFT
        player.x -= VEL
    if keys_pressed[pygame.K_d] and player.x - VEL < WIDTH - 55 and not (player.colliderect(SCREEN_1_BARRIER_HORIZONTAL) and player.colliderect(SCREEN_1_BARRIER_VERTICAL)):  # RIGHT
        player.x += VEL
    if keys_pressed[pygame.K_w] and player.y - VEL > 0 and not (player.colliderect(SCREEN_1_BARRIER_HORIZONTAL) and player.colliderect(SCREEN_1_BARRIER_VERTICAL)):  # UP
        player.y -= VEL
    if keys_pressed[pygame.K_s] and player.y - VEL < HEIGHT - 40 and not (player.colliderect(SCREEN_1_BARRIER_HORIZONTAL) and player.colliderect(SCREEN_1_BARRIER_VERTICAL)):  # DOWN
        player.y += VEL
    rotate_angle = -pygame.mouse.get_pos()[0] 
    print((player.colliderect(SCREEN_1_BARRIER_HORIZONTAL)))
    return rotate_angle


# def handle_collision(player) -> bool: 
#     if player.colliderect(SCREEN_1_BARRIER_HORIZONTAL):
#         hit_object = True
#     return hit_object

    
    
def main():
    rotate_angle = 0
    player = pygame.Rect(100, 300, 55, 40)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        PLAYER = pygame.transform.rotate(pygame.transform.scale(PLAYER_IMAGE, (55, 40)), rotate_angle)
        draw_window(player, PLAYER)
        keys_pressed = pygame.key.get_pressed()
        rotate_angle = player_handle_movement(keys_pressed, player, rotate_angle)
        # handle_collision(player)
      
    pygame.quit


if __name__ == "__main__":
    main()