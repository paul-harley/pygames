import pygame
import globals

class Apple:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
    
    def draw(self, screen):
        pygame.draw.rect(screen, globals.RED, (self.x, self.y, self.width, self.height ))

