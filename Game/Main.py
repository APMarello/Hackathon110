"""Main Python file."""

from re import L
from turtle import width
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



BLACK = (0, 0, 0)

SCREEN_BARRIER_1 = pygame.Rect(0, 0, 0, 0)
SCREEN_BARRIER_2 = pygame.Rect(0, 0, 0, 0)
SCREEN_BARRIER_3 = pygame.Rect(0, 0, 0, 0)
SCREEN_BARRIER_4 = pygame.Rect(0, 0, 0, 0)
SCREEN_BARRIER_5 = pygame.Rect(0, 0, 0, 0)
SCREEN_BARRIER_6 = pygame.Rect(0, 0, 0, 0)

FPS = 60
VEL = 5
PLAYER_IMAGE = pygame.image.load(os.path.join('game_assets', 'player.png'))

CASTLE_IMAGE = pygame.image.load(os.path.join('game_assets', 'Castle.png'))
CASTLE = pygame.transform.scale(CASTLE_IMAGE, (488, 323))

        
def handle_screen(player, screen_num) -> int:
    if player.x > WIDTH and screen_num == 1:
        player.x = 0
        screen_num = 2
        return screen_num
    elif player.x < 0 and screen_num == 2:
        player.x = WIDTH
        screen_num = 1
        return screen_num
    elif player.x > WIDTH and screen_num == 2:
        player.x = 0
        screen_num = 3
        return screen_num
    elif player.x < 0 and screen_num == 3:
        player.x = WIDTH
        screen_num = 2
        return screen_num
    elif player.y > HEIGHT and screen_num == 1:
        player.y = 0
        screen_num = 4
        return screen_num
    elif player.y < 0 and screen_num == 4:
        player.y = HEIGHT
        screen_num = 1
        return screen_num
    elif player.y > HEIGHT and screen_num == 2:
        player.y = 0
        screen_num = 5
        return screen_num
    elif player.y < 0 and screen_num == 5:
        player.y = HEIGHT
        screen_num = 2
        return screen_num
    elif player.y > HEIGHT and screen_num == 3:
        player.y = 0
        screen_num = 6
        return screen_num
    elif player.y < 0 and screen_num == 6:
        player.y = HEIGHT
        screen_num = 3
        return screen_num
    elif player.x > WIDTH and screen_num == 4:
        player.x = 0
        screen_num = 5
        return screen_num
    elif player.x < 0 and screen_num == 5:
        player.x = WIDTH
        screen_num = 4
        return screen_num
    elif player.x > WIDTH and screen_num == 5:
        player.x = 0
        screen_num = 6
        return screen_num
    elif player.x < 0 and screen_num == 6:
        player.x = WIDTH
        screen_num = 5
        return screen_num
    elif player.y > HEIGHT and screen_num == 4:
        player.y = 0
        screen_num = 7
        return screen_num
    elif player.y < 0 and screen_num == 7:
        player.y = HEIGHT
        screen_num = 4
        return screen_num
    elif player.y > HEIGHT and screen_num == 5:
        player.y = 0
        screen_num = 8
        return screen_num
    elif player.y < 0 and screen_num == 8:
        player.y = HEIGHT
        screen_num = 5
        return screen_num
    elif player.y > HEIGHT and screen_num == 6:
        player.y = 0
        screen_num = 9
        return screen_num
    elif player.y < 0 and screen_num == 9:
        player.y = HEIGHT
        screen_num = 6
        return screen_num
    elif player.x > WIDTH and screen_num == 7:
        player.x = 0
        screen_num = 8
        return screen_num
    elif player.x < 0 and screen_num == 8:
        player.x = WIDTH
        screen_num = 8
        return screen_num
    elif player.x > WIDTH and screen_num == 8:
        player.x = 0
        screen_num = 9
        return screen_num
    elif player.x < 0 and screen_num == 9:
        player.x = WIDTH
        screen_num = 8
        return screen_num
    
    
    return screen_num

def draw_window(player, PLAYER, screen_num):   
    WIN.fill(GREEN)
    WIN.blit(PLAYER, (player.x, player.y))
    pygame.draw.rect(WIN, BLACK, SCREEN_BARRIER_1)
    pygame.draw.rect(WIN, BLACK, SCREEN_BARRIER_2)
    pygame.draw.rect(WIN, BLACK, SCREEN_BARRIER_3)
    pygame.draw.rect(WIN, BLACK, SCREEN_BARRIER_4)
    pygame.draw.rect(WIN, BLACK, SCREEN_BARRIER_5)
    pygame.draw.rect(WIN, BLACK, SCREEN_BARRIER_6)
    if screen_num == 1:
        screen_1()
    elif screen_num == 2:
        screen_2()
    elif screen_num == 3:
        screen_3()
    elif screen_num == 4:
        screen_4()
    elif screen_num == 5:
        screen_5()
    elif screen_num == 6:
        screen_6()
    elif screen_num == 7:
        screen_7()
    elif screen_num == 8:
        screen_8()
    elif screen_num == 9:
        screen_9()
    pygame.display.update()


def player_handle_movement(keys_pressed, player, rotate_angle) -> int:
    if keys_pressed[pygame.K_a] and player.x - VEL > -60 and not player.colliderect(SCREEN_BARRIER_1
    ) and not player.colliderect(SCREEN_BARRIER_2) and not player.colliderect(SCREEN_BARRIER_3) and not player.colliderect(SCREEN_BARRIER_4
    ) and not player.colliderect(SCREEN_BARRIER_5) and not player.colliderect(SCREEN_BARRIER_6):  # LEFT
        player.x -= VEL
        if player.colliderect(SCREEN_BARRIER_1) or player.colliderect(SCREEN_BARRIER_2
        ) or player.colliderect(SCREEN_BARRIER_3) or player.colliderect(SCREEN_BARRIER_4) or player.colliderect(SCREEN_BARRIER_5
        ) or player.colliderect(SCREEN_BARRIER_6):
            player.x += 5
    if keys_pressed[pygame.K_d] and player.x - VEL < WIDTH and not player.colliderect(SCREEN_BARRIER_1
    ) and not player.colliderect(SCREEN_BARRIER_2) and not player.colliderect(SCREEN_BARRIER_3) and not player.colliderect(SCREEN_BARRIER_4
    ) and not player.colliderect(SCREEN_BARRIER_5) and not player.colliderect(SCREEN_BARRIER_6):  # RIGHT
        player.x += VEL
        if player.colliderect(SCREEN_BARRIER_1) or player.colliderect(SCREEN_BARRIER_2
        ) or player.colliderect(SCREEN_BARRIER_3) or player.colliderect(SCREEN_BARRIER_4) or player.colliderect(SCREEN_BARRIER_5
        ) or player.colliderect(SCREEN_BARRIER_6):
            player.x -= 5
    if keys_pressed[pygame.K_w] and player.y - VEL > -60 and not player.colliderect(SCREEN_BARRIER_1
    ) and not player.colliderect(SCREEN_BARRIER_2) and not player.colliderect(SCREEN_BARRIER_3) and not player.colliderect(SCREEN_BARRIER_4
    ) and not player.colliderect(SCREEN_BARRIER_5) and not player.colliderect(SCREEN_BARRIER_6):  # UP
        player.y -= VEL
        if player.colliderect(SCREEN_BARRIER_1) or player.colliderect(SCREEN_BARRIER_2
        ) or player.colliderect(SCREEN_BARRIER_3) or player.colliderect(SCREEN_BARRIER_4) or player.colliderect(SCREEN_BARRIER_5
        ) or player.colliderect(SCREEN_BARRIER_6):
            player.y += 5
    if keys_pressed[pygame.K_s] and player.y - VEL < HEIGHT and not player.colliderect(SCREEN_BARRIER_1
    ) and not player.colliderect(SCREEN_BARRIER_2) and not player.colliderect(SCREEN_BARRIER_3) and not player.colliderect(SCREEN_BARRIER_4
    ) and not player.colliderect(SCREEN_BARRIER_5) and not player.colliderect(SCREEN_BARRIER_6):  # DOWN
        player.y += VEL
        if player.colliderect(SCREEN_BARRIER_1) or player.colliderect(SCREEN_BARRIER_2
        ) or player.colliderect(SCREEN_BARRIER_3) or player.colliderect(SCREEN_BARRIER_4) or player.colliderect(SCREEN_BARRIER_5
        ) or player.colliderect(SCREEN_BARRIER_6):
            player.y -= 5
    rotate_angle = -pygame.mouse.get_pos()[0] 
    return rotate_angle

def screen_1():
    SCREEN_BARRIER_1.update(300, 300, 600, 20)
    SCREEN_BARRIER_2.update(0, 0, 20, 100)
    SCREEN_BARRIER_3.update(50, 50, 20, 20)
    SCREEN_BARRIER_4.update(800, 200, 20, 100)
    SCREEN_BARRIER_5.update(200, 300, 600, 20)
    SCREEN_BARRIER_6.update(150, 200, 20, 20)

def screen_2():
    WIN.blit(CASTLE, (206, 20))
    SCREEN_BARRIER_1.update(300, 300, 600, 20)
    SCREEN_BARRIER_2.update(0, 0, 0, 0)
    SCREEN_BARRIER_3.update(0, 0, 0, 0)
    SCREEN_BARRIER_4.update(0, 0, 0, 0)
    SCREEN_BARRIER_5.update(0, 0, 0, 0)
    SCREEN_BARRIER_6.update(0, 0, 0, 0)

def screen_3():
    SCREEN_BARRIER_1.update(0, 0, 0, 0)
    SCREEN_BARRIER_2.update(150, 200, 100, 20)
    SCREEN_BARRIER_3.update(0, 0, 0, 0)
    SCREEN_BARRIER_4.update(0, 0, 0, 0)
    SCREEN_BARRIER_5.update(0, 0, 0, 0)
    SCREEN_BARRIER_6.update(0, 0, 0, 0)

def screen_4():
    SCREEN_BARRIER_1.update(300, 300, 600, 300)
    SCREEN_BARRIER_2.update(0, 0, 0, 0)
    SCREEN_BARRIER_3.update(0, 0, 0, 0)
    SCREEN_BARRIER_4.update(0, 0, 0, 0)
    SCREEN_BARRIER_5.update(0, 0, 0, 0)
    SCREEN_BARRIER_6.update(0, 0, 0, 0)
    
def screen_5():
    SCREEN_BARRIER_1.update(600, 400, 600, 20)
    SCREEN_BARRIER_2.update(0, 0, 0, 0)
    SCREEN_BARRIER_3.update(0, 0, 0, 0)
    SCREEN_BARRIER_4.update(0, 0, 0, 0)
    SCREEN_BARRIER_5.update(0, 0, 0, 0)
    SCREEN_BARRIER_6.update(0, 0, 0, 0)

def screen_6():
    SCREEN_BARRIER_1.update(300, 300, 100, 10)
    SCREEN_BARRIER_2.update(0, 0, 0, 0)
    SCREEN_BARRIER_3.update(0, 0, 0, 0)
    SCREEN_BARRIER_4.update(0, 0, 0, 0)
    SCREEN_BARRIER_5.update(0, 0, 0, 0)
    SCREEN_BARRIER_6.update(0, 0, 0, 0)

def screen_7():
    SCREEN_BARRIER_1.update(0, 0, 0, 0)
    SCREEN_BARRIER_2.update(0, 0, 0, 0)
    SCREEN_BARRIER_3.update(0, 0, 0, 0)
    SCREEN_BARRIER_4.update(0, 0, 0, 0)
    SCREEN_BARRIER_5.update(100, 100, 100, 10)
    SCREEN_BARRIER_6.update(0, 0, 0, 0)
    
def screen_8():
    SCREEN_BARRIER_1.update(0, 0, 0, 0)
    SCREEN_BARRIER_2.update(300, 200, 40, 40)
    SCREEN_BARRIER_3.update(0, 0, 0, 0)
    SCREEN_BARRIER_4.update(0, 0, 0, 0)
    SCREEN_BARRIER_5.update(0, 0, 0, 0)
    SCREEN_BARRIER_6.update(0, 0, 0, 0)

def screen_9():
    SCREEN_BARRIER_1.update(0, 0, 0, 0)
    SCREEN_BARRIER_2.update(0, 0, 0, 0)
    SCREEN_BARRIER_3.update(0, 0, 0, 0)
    SCREEN_BARRIER_4.update(0, 0, 0, 0)
    SCREEN_BARRIER_5.update(0, 0, 0, 0)
    SCREEN_BARRIER_6.update(0, 0, 0, 0)


def main():
    clock = pygame.time.Clock()
    rotate_angle = 0
    player = pygame.Rect(100,  300, 60, 60)

    run = True
    screen_num = 1
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        PLAYER = pygame.transform.rotate(pygame.transform.scale(PLAYER_IMAGE, (60, 60)), rotate_angle)
        
        screen_num = handle_screen(player, screen_num)
        draw_window(player, PLAYER, screen_num)
        keys_pressed = pygame.key.get_pressed()
        rotate_angle = player_handle_movement(keys_pressed, player, rotate_angle)
        
    pygame.quit


if __name__ == "__main__":
    main()