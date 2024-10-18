import pygame

class Cell:
    def __init__(self, width, height, colourRGB):
        
        self.width = width
        self.height = height
        self.colourRGB = colourRGB
        self.fillAmount = 3

        self.colourSH = ''
        self.clicked = False


    def draw(self, screen, x, y):
        Action = False
        myShape = pygame.Rect(x, y, self.width, self.height)
        pygame.draw.rect(screen, self.colourRGB, myShape, self.fillAmount, 50)

        #getting mouse position
        pos = pygame.mouse.get_pos()

        #checking collision
        if myShape.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                Action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        return Action


