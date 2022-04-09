"""Pygame tutorial."""

import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

pygame.mouse.set_visible(False)

WHITE = (255, 255, 255)
GREEN = (86, 125, 70)

FPS = 60
VEL = 5
PLAYER_IMAGE = pygame.image.load(os.path.join('Hackathon', 'tutorial_assets', 'player.png'))


def draw_window(player, PLAYER):   
    WIN.fill(GREEN)
    WIN.blit(PLAYER, (player.x, player.y))
    pygame.display.update()


def player_handle_movement(keys_pressed, player, rotate_angle) -> int:
    if keys_pressed[pygame.K_a] and player.x - VEL > 0:  # LEFT
        player.x -= VEL
    if keys_pressed[pygame.K_d] and player.x - VEL < WIDTH - 55:  # RIGHT
        player.x += VEL
    if keys_pressed[pygame.K_w] and player.y - VEL > 0:  # UP
        player.y -= VEL
    if keys_pressed[pygame.K_s] and player.y - VEL < HEIGHT - 40:  # DOWN
        player.y += VEL
    rotate_angle = -pygame.mouse.get_pos()[0] 
    return rotate_angle
    
    
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
      
    pygame.quit


if __name__ == "__main__":
    main()