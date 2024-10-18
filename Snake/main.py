import pygame
import globals
import snake
import apple
import bot
import random

screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
pygame.init()

apples = []
score = 0
score_font = pygame.font.SysFont("Arial",globals.GRIDSQSIZE )
humanPlaying = False
if humanPlaying is False:
    myBot = bot.Bot()


def drawText (text, font, colour, x, y):
    img = font.render(str(text), 1, colour)
    screen.blit(img, (x,y))


# Draws backgorund of game screen
def DrawGrid():
    for i in range(int(globals.SCREEN_WIDTH/globals.GRIDSQSIZE)):
        for j in range(int(globals.SCREEN_WIDTH/globals.GRIDSQSIZE)):
            pygame.draw.rect(screen, globals.DARK_GREEN, (globals.GRIDSQSIZE*i, globals.GRIDSQSIZE*j, globals.GRIDSQSIZE, globals.GRIDSQSIZE), 1)

def MakeApple():

    #Generating random coords for apple to spawn on
    #Need to check they do not appear on the snakes bodys
    if len(SNAKE.bodyPosition) < (globals.SCREEN_HEIGHT/globals.GRIDSQSIZE) * (globals.SCREEN_WIDTH/globals.GRIDSQSIZE) -3: 

        #Weird do while loop cause python has none
        xCord = random.randint(0, int(globals.SCREEN_WIDTH/globals.GRIDSQSIZE) -1) * globals.GRIDSQSIZE
        yCord = random.randint(0, int(globals.SCREEN_HEIGHT/globals.GRIDSQSIZE) -1) * globals.GRIDSQSIZE
        valid = True
        for i in range(len(SNAKE.bodyPosition)):
            if xCord == SNAKE.bodyPosition[i][0] and yCord == SNAKE.bodyPosition[i][1]:
                valid = False

        for i in range(len(apples)):
            if xCord == apples[i].x and yCord == apples[i].y:
                valid = False

        while valid is False:
            valid = True

            xCord = random.randint(0, int(globals.SCREEN_WIDTH/globals.GRIDSQSIZE) -1) * globals.GRIDSQSIZE
            yCord = random.randint(0, int(globals.SCREEN_HEIGHT/globals.GRIDSQSIZE) -1) * globals.GRIDSQSIZE

            for i in range(len(SNAKE.bodyPosition)):
                if xCord == SNAKE.bodyPosition[i][0] and yCord == SNAKE.bodyPosition[i][1]:
                    valid = False

            for i in range(len(apples)):
                if xCord == apples[i].x and yCord == apples[i].y:
                    valid = False

        APPLE = apple.Apple(xCord, yCord, globals.GRIDSQSIZE, globals.GRIDSQSIZE)
        apples.append(APPLE)


def DrawAllApples():
    for i in range(len(apples)):
        apples[i].draw(screen)


def MoveSnake(dir):

    #UP
    if dir == 'U':
        SNAKE.xDirection = 0
        SNAKE.yDirection = -globals.GRIDSQSIZE

    #DOWN
    if dir == 'D':
        SNAKE.xDirection = 0
        SNAKE.yDirection = globals.GRIDSQSIZE
    
    #LEFT
    if dir == 'L':
        SNAKE.xDirection = -globals.GRIDSQSIZE
        SNAKE.yDirection = 0
    
    #RIGHT
    if dir == 'R':
        SNAKE.xDirection = globals.GRIDSQSIZE
        SNAKE.yDirection = 0

def botMove():
    
    #EVEN SCREEN HEIGHT
    if (globals.SCREEN_HEIGHT/globals.GRIDSQSIZE)%2 == 0:
        myBot.EvenHeightMove(SNAKE)
    
    #BOTH DIMENSIONS ODD 
    elif (globals.SCREEN_HEIGHT/globals.GRIDSQSIZE)%2 == 1 and (globals.SCREEN_WIDTH/globals.GRIDSQSIZE)%2 == 1:
        myBot.BothDimOddMove(SNAKE, apples) 
    
    #ODD HEIGHT EVEN LENGTH
    else:
        myBot.OddHeightEvenLength(SNAKE)

#Creating game variables
SNAKE = snake.Snake(globals.GRIDSQSIZE, globals.GRIDSQSIZE, 0, 0)

#set number of apples in play
for i in range(3):
    MakeApple()

resume = True
clock = pygame.time.Clock()

while resume:

    screen.fill(globals.BLACK)
    DrawGrid()
    SNAKE.updatePos()


    #COLLISION POSSIBILTIES
    collisionRes = SNAKE.checkCollisions(apples, globals.GRIDSQSIZE)

    #APPLE COLLISION
    if collisionRes >= 1:
        apples.pop(collisionRes-1)
        score += 100
        MakeApple()

    #Could save a top 10 scores
    #Would add here on death
    if collisionRes == -1:
        apples.clear()
        for i in range(3):
            MakeApple()

        score = 0

    SNAKE.draw(screen)
    DrawAllApples()

    #PLAYER MOVEMENT 
    if humanPlaying:
        key = pygame.key.get_pressed()

        if key[pygame.K_w]: #UP
            if SNAKE.yDirection != globals.GRIDSQSIZE:          #Ensures snake cannot move directly back into cell behind head
               MoveSnake('U')

        if key[pygame.K_s]: #DOWN
            if SNAKE.yDirection != -globals.GRIDSQSIZE:
                MoveSnake('D')

        if key[pygame.K_a]: #LEFT
            if SNAKE.xDirection != globals.GRIDSQSIZE:
                MoveSnake('L')

        if key[pygame.K_d]: #RIGHT
            if SNAKE.xDirection != -globals.GRIDSQSIZE:
                MoveSnake('R')
    else:
        botMove()

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            resume = False
         
    drawText(str(score), score_font, (255,255,255), globals.GRIDSQSIZE, globals.GRIDSQSIZE)
    pygame.display.update()
    clock.tick(10)


pygame.quit()