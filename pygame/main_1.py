import pygame
import os 
import time 
import random

WIDTH, HEIGHT = 750, 750

player_x = 0
player_y = 0

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Codinglab")

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

run = True
while run:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - 5 > 0: # left
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x + 5 < WIDTH: # right
        player_x += 5
    if keys[pygame.K_UP] and player_y - 5 > 0: # up
        player_y -= 5
    if keys[pygame.K_DOWN] and player_y + 5  < HEIGHT: # down
        player_y += 5

    window.blit(BG, (0,0))
    window.blit(YELLOW_SPACE_SHIP, (player_x,player_y))
    pygame.display.update()
pygame.quit()