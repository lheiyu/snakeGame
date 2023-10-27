import pygame
from pygame.locals import *
import time
import random

SIZE = 40
start_length = 1
WHITE = (255, 255, 255)

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("C:/workspace/python_games/snakeGame/resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3
        
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
        
    def move(self):
        self.x = random.randint(1, 19)*SIZE
        self.y = random.randint(2, 19)*SIZE


class Snake:
    def __init__(self, parent_win, length):
        self.parent_win = parent_win
        self.length = length
        self.block = pygame.image.load("python_games/snakeGame/resources/block.jpg").convert()
        self.x = [SIZE*(random.randint(5, 15))] * length
        self.y = [SIZE*(random.randint(5, 15))] * length
        
        directions = ["up", "down", "left", "right"]
        self.direction = directions[random.randint(0, 3)]
        
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
        
    def move_up(self):
        self.direction = "up"
    def move_down(self):
        self.direction = "down"
    def move_left(self):
        self.direction = "left"
    def move_right(self):
        self.direction = "right"
    
    def walk(self):
        
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        
        if self.direction == "up":
            self.y[0] -= SIZE
        if self.direction == "down":
            self.y[0] += SIZE
        if self.direction == "left":
            self.x[0] -= SIZE
        if self.direction == "right":
            self.x[0] += SIZE
        
        self.draw()
        
    def draw(self):
        self.parent_win.fill(WHITE)
        for i in range(self.length):
            self.parent_win.blit(self.block, (self.x[i], self.y[i]))
            pygame.display.flip()
    
        
class Game:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((800, 800))
        self.apple = Apple(self.win)
        self.snake = Snake(self.win, start_length)
        
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1< y2 + SIZE:
                return True
        return False
            
    def out_of_bound(self, x, y):
        if 0 <= x < 800:
            if 0 <= y < 800:
                return False
        else:
            return True
            
        
    def play(self):
        self.win.fill(WHITE)
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
    
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()
            
        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game over. "
            
        if self.out_of_bound(self.snake.x[0], self.snake.y[0]):
            raise "Game over. "
            
    def display_score(self):
        font =pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (0, 0, 0))
        self.win.blit(score, (0, 0))
    
    def show_game_over(self):
        self.win.fill(WHITE)
        font = pygame.font.SysFont('arial', 30)
        game_over_score = font.render(f"Game over, your score was {self.snake.length}", True, (0, 0, 0))
        self.win.blit(game_over_score, (200, 100))
        replay_text = font.render("To play again press Enter, to exit press Esc!", True, (0, 0, 0))
        self.win.blit(replay_text, (100, 220))
        pygame.display.flip() 
        
    def reset(self):
        self.win = pygame.display.set_mode((800, 800))
        self.apple = Apple(self.win)
        self.snake = Snake(self.win, start_length)
    
    
    def run(self):
            run = True
            pause = False
            while run:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            run = False
                        if event.key == K_RETURN:
                            pause = False
                            self.reset()
                        
                        if not pause:
                            if event.key == K_UP:
                                self.snake.move_up()
                            if event.key == K_DOWN:
                                self.snake.move_down()
                            if event.key == K_LEFT:
                                self.snake.move_left()
                            if event.key == K_RIGHT:
                                self.snake.move_right()
                            
                    elif event.type == QUIT:
                        run = False
                
                try:
                    if not pause:  
                        self.play()
                except Exception as e:
                    self.show_game_over()
                    pause = True
                    
                time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()
    

