import pygame


black = (0,0,0)

class Cell:
    def __init__(self, id, height, width):
        self.id = id
        self.height = height
        self.width = width
        self.colour = black

        self.clicked = False

        self.symbol = ''


    def draw(self,screen, x, y ):

        action = False

        rect = pygame.Rect(x, y, self.height, self.width)
        pygame.draw.rect(screen, self.colour, rect, 5)

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check collision and click
        if rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        return action
