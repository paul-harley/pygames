import pygame
import globals

class Snake():
    def __init__(self, width, height, xDirection, yDirection, ):
        
        self.width = width
        self.height = height
        self.xDirection = xDirection
        self.yDirection = yDirection
        self.dead = False

        self.bodyPosition = [[globals.GRIDSQSIZE, globals.GRIDSQSIZE*2], [globals.GRIDSQSIZE*2, globals.GRIDSQSIZE*2]]

    def draw(self, screen):
        for i in range(len(self.bodyPosition)):
            pygame.draw.rect(screen, globals.GREEN, (self.bodyPosition[i][0], self.bodyPosition[i][1], self.width, self.height ))

    def checkCollisions(self, APPLES, gridSqSize):

        #Checks if head collides with any apples on the board
        for i in range(len(APPLES)):
            if self.bodyPosition[0][0] == APPLES[i].x and self.bodyPosition[0][1] == APPLES[i].y:
                
                #Adding to snakes body
                lastIndex = len(self.bodyPosition) - 1

                #The last 2 are horizontal together
                if self.bodyPosition[lastIndex][1] == self.bodyPosition[lastIndex-1][1]: 
                    newXcord = self.bodyPosition[lastIndex][0] + (self.bodyPosition[lastIndex][0] - self.bodyPosition[lastIndex][0])
                    newCords = [newXcord, self.bodyPosition[lastIndex][1]]
                
                #The last 2 are vertical
                else:
                    newYcord = self.bodyPosition[lastIndex][1] + (self.bodyPosition[lastIndex][1] - self.bodyPosition[lastIndex][1])
                    newCords = [self.bodyPosition[lastIndex][0], newYcord]
                    

                self.bodyPosition.append(newCords)
                return 1 + i
            
        #Checks for crashing into itself
        for i in range(1, len(self.bodyPosition)):
            if self.bodyPosition[0][0] == self.bodyPosition[i][0] and self.bodyPosition[0][1] == self.bodyPosition[i][1]:
                self.dead = True
        
        #Check for Win
        if len(self.bodyPosition) == (globals.SCREEN_HEIGHT/gridSqSize) * (globals.SCREEN_WIDTH/gridSqSize)-1:
            self.dead = True
        
        #Check for out of bounds
        if self.bodyPosition[0][0] >= globals.SCREEN_WIDTH or self.bodyPosition[0][0] < 0 :
            self.dead = True

        if self.bodyPosition[0][1] >= globals.SCREEN_HEIGHT or self.bodyPosition[0][1] < 0 :
            self.dead = True
        
        if self.dead:
            self.dead = False
            self.xDirection = 0
            self.yDirection = 0
            self.bodyPosition = [[globals.GRIDSQSIZE, globals.GRIDSQSIZE*2], [globals.GRIDSQSIZE*2, globals.GRIDSQSIZE*2]]
            return-1


        return 0

    def updatePos(self):

        if self.xDirection != 0 or self.yDirection != 0:
            #BODY MOVEMENT
            #Saving original pos
            orginalHeadLocation = self.bodyPosition[0]
        
            #Travelling X Axis
            if self.xDirection != 0:
                #Calculating new x pos and y stays the same
                newX = orginalHeadLocation[0] + self.xDirection
                self.bodyPosition.insert(0,[newX, orginalHeadLocation[1]])
                #Remove last position
                self.bodyPosition.pop()

            #Travelling Y Axis
            if self.yDirection != 0:
                #Calculating new y pos and x stays the same
                newY = orginalHeadLocation[1] + self.yDirection
                self.bodyPosition.insert(0,[orginalHeadLocation[0], newY])
                #Remove last position
                self.bodyPosition.pop()


    