import pygame
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    
    win = pygame.display.set_mode((1000, 500))
    win.fill((255, 255, 255))
    pygame.display.flip()
    
    block = pygame.image.load("resources/block.jpg").convert()
    
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            elif event.type == QUIT:
                run = False