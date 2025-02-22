import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
SPRITE_SIZE = 50
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Color Change Event")

class Sprite:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, SPRITE_SIZE, SPRITE_SIZE)
        self.color = color
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
    
    def change_color(self):
        self.color = random.choice(COLORS)

sprite1 = Sprite(200, 250, random.choice(COLORS))
sprite2 = Sprite(500, 250, random.choice(COLORS))

pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

running = True
while running:
    pygame.time.delay(30)
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()
    
    sprite1.draw(screen)
    sprite2.draw(screen)
    
    pygame.display.update()

pygame.quit()