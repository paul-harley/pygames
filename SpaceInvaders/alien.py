import pygame

class Alien:
    def __init__(self, x, y, colour, score):
        self.height = 20
        self.width = 45

        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.colour = colour
        self.score = score

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)

    def update(self, direction):
        self.rect.x += direction

