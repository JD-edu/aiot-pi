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
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))

class Ship:
    def __init__(self, x, y, ship_img):
        self.x = x
        self.y = y
        self.ship_img = ship_img

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

player = Ship(0, 0, YELLOW_SPACE_SHIP)

enemy = Ship(random.randrange(50, WIDTH-100), 50, RED_SPACE_SHIP)

run = True
while run:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - 5 > 0: # left
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x + 5 < WIDTH: # right
        player.x += 5
    if keys[pygame.K_UP] and player.y - 5 > 0: # up
        player.y -= 5
    if keys[pygame.K_DOWN] and player.y + 5  < HEIGHT: # down
        player.y += 5

    window.blit(BG, (0,0))
    player.draw(window)
    enemy.draw(window)
    pygame.display.update()
pygame.quit()