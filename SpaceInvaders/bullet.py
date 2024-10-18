import pygame
import globals

class Bullet:
    def __init__ (self, x, y, height, width, speed):

        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

        self.speed = speed

    
    def draw(self, screen):
        pygame.draw.rect(screen, globals.WHITE, self.rect)

    def update(self):
        self.rect.y -= self.speed

    def destroy(self):
        if self.rect.y < 0-self.height or self.rect.y > globals.SCREEN_HEIGHT:
            return True
