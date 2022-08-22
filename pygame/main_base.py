import pygame
import os 
import time 
import random

WIDTH, HEIGHT = 750, 750


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Codinglab")

run = True
while run:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
pygame.quit()