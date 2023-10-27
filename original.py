import pygame
import os
import random
pygame.font.init()


WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0

WIDTH, HEIGHT = 800, 800
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game")

#declare events
START = pygame.USEREVENT + 1
LOSE = pygame.USEREVENT + 2

TITLE_FONT = pygame.font.SysFont('comicsans', 25)

START_BUTTON_IMAGE = pygame.image.load(os.path.join("python_games", "snakeGame", "images", "start button.jpg"))
START_BUTTON = pygame.transform.scale(START_BUTTON_IMAGE, (250, 100))
START_RECT = START_BUTTON.get_rect()

def draw_title():
    WIN.fill(WHITE)
    title_text = TITLE_FONT.render("click anywhere to begin", 1, BLACK)
    WIN.blit(title_text, (WIDTH/2 - title_text.get_width()/2, HEIGHT*3/5 - title_text.get_height()/2))
    WIN.blit(START_BUTTON, (WIDTH/2 - 125, HEIGHT/2 - 50))
    pygame.display.flip()
    
    
def draw_bg():
    for i in range(0, WIDTH, 40):                           #CHECKERS
        pygame.draw.line(WIN, BLACK, (0, i), (WIDTH, i))    #HORIZONTAL
        pygame.draw.line(WIN, BLACK, (i, 0), (i, HEIGHT))      #VERTICAL
    pygame.display.flip()

def draw_snake(snake_xpos, snake_ypos):
    pygame.draw.rect(WIN, GREEN, pygame.Rect(snake_xpos + 1, snake_ypos + 1, WIDTH/40, HEIGHT/40))
    pygame.display.flip()

def snake_movement():
    snake_len = 3
    
    


def main():
    clock = pygame.time.Clock()
    run = True
    draw_title()
    if pygame.mouse.get_pressed()[0]:
        pygame.event.post(pygame.event.Event(START))
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == START:
                snake_xpos = random.randint(WIDTH/2 - 40, WIDTH/2 + 40)
                snake_ypos = random.randint(HEIGHT/2 - 40, HEIGHT/2 + 40)
                draw_snake(snake_xpos, snake_ypos)
                snake_movement()
                draw_bg()
        
        

    main()
    
if __name__ == "__main__":
    main()