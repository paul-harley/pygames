import pygame
import globals
import cell

pygame.init()

resume = True
playerTurn = 'R'
rWins = 0
yWins = 0
score_font = pygame.font.SysFont("Arial", 30)


#CREATING GRID FOR ALL CELLS TO HOLD GAME DATA

def resetBoard():
    grid = []
    screen.fill(globals.BLACK)
    
    
    #CREATING SCORE SECTION AT TOP
    pygame.draw.rect(screen, globals.RED, (95, 20, 70, 70),0, 50)
    pygame.draw.rect(screen, globals.YELLOW, (globals.SCREEN_WIDTH-70, 20, 70, 70),0, 50)

    drawText(rWins, score_font, (255,255,255), 200, 40)
    drawText(yWins, score_font, (255,255,255), globals.SCREEN_WIDTH-120, 40)

    turnIndicator()

    for i in range(7):
        ROW = []
        for j in range(6):
            myCell = cell.Cell(globals.CELLSIZE, globals.CELLSIZE, globals.BLUE)
            ROW.append(myCell)
        grid.append(ROW)
    return grid
        
def turnIndicator():

    #SETTING WHITE BELOW RED AND BLACK UNDER YELLOW 
    if playerTurn == 'R':
        pygame.draw.rect(screen, globals.WHITE, (95, 90, 70, 10))  
        pygame.draw.rect(screen, globals.BLACK, (globals.SCREEN_WIDTH-70, 90, 70, 10))

    #SETTING WHITE BELOW YELLOW AND BLACK UNDER RED 
    elif playerTurn == 'Y':
        pygame.draw.rect(screen, globals.WHITE, (globals.SCREEN_WIDTH-70, 90, 70, 10))
        pygame.draw.rect(screen, globals.BLACK, (95, 90, 70, 10))





screen = pygame.display.set_mode((globals.SCREEN_HEIGHT, globals.SCREEN_WIDTH))
screen.fill(globals.BLACK)


def findCorrectCell (Grid, i):
    #STOPS INSTANTLY IF THE COL IS FULL
    if Grid[i][0].colourSH != '':
        return -1
    
    #RETURNS EARLY IF COL IS EMPTY 
    elif Grid[i][5].colourSH == '':
        return 5
    
    #LOOPS THROUGH ALL CELLS IN THE COL UNTIL IT FINDS THE FIRST EMPTY CELL 
    #RETURNS CORD OF EMPTY CELL
    for j in range(1, 5):
        if Grid[i][j].colourSH == '' and (Grid[i][j+1].colourSH != ''):
            return j
    

    return 0
    

def checkWin(Grid):

    #HORIZONTAL WINS
    for i in range(4):
        for j in range(6):
            if Grid[i][j].colourSH != '':
                if (Grid[i][j].colourSH == Grid[i+1][j].colourSH) and (Grid[i][j].colourSH == Grid[i+2][j].colourSH) and (Grid[i][j].colourSH == Grid[i+3][j].colourSH):
                    return True

    #VERTICAL WINS
    for i in range(7):
        for j in range(3):
            if Grid[i][j].colourSH != '':
                if (Grid[i][j].colourSH == Grid[i][j+1].colourSH) and (Grid[i][j].colourSH == Grid[i][j+2].colourSH) and (Grid[i][j].colourSH == Grid[i][j+3].colourSH):
                    return True

    #DIAGONAL WINS
    #TOP LEFT - BOTTOM RIGHT
    for i in range(7):
        for j in range(6):
            if (i+3) < 7 and (j+3)<6:
                if Grid[i][j].colourSH != '':
                    if (Grid[i][j].colourSH == Grid[i+1][j+1].colourSH) and (Grid[i][j].colourSH == Grid[i+2][j+2].colourSH) and (Grid[i][j].colourSH == Grid[i+3][j+3].colourSH):
                        return True

    
    #BOTTOM LEFT - TOP RIGHT
    for i in range(7):
        for j in range(6):
            if (i+3) < 7 and (j-3)>-1:
                if Grid[i][j].colourSH != '':
                    if (Grid[i][j].colourSH == Grid[i+1][j-1].colourSH) and (Grid[i][j].colourSH == Grid[i+2][j-2].colourSH) and (Grid[i][j].colourSH == Grid[i+3][j-3].colourSH):
                        return True
    return False


def drawText (text, font, colour, x, y):
    pygame.draw.rect(screen, globals.BLACK, (x, y, 30, 30),)
    img = font.render(str(text), 1, colour)
    screen.blit(img, (x,y))


GRID = resetBoard()
while resume:

    win = False
    for i in range(7):
        for j in range(6):
            #CHECK IF CELL IS CLICKED
            if GRID[i][j].draw(screen, (globals.CELLSIZE*i) + 105, (globals.CELLSIZE*j) + 120):

                downCell = findCorrectCell(GRID, i)
                #SETTING CHOSEN CELL TO CORRECT COLOUR
                
                #RED
                if playerTurn == 'R':
                    if(downCell!= -1):
                        GRID[i][downCell].fillAmount= 0
                        GRID[i][downCell].colourRGB = globals.RED
                        GRID[i][downCell].colourSH= 'R'
                        if checkWin(GRID):
                            if win == False:
                                rWins += 1
                                #drawText(rWins, score_font, (255,255,255), 100, 100)
                                win = True
                        playerTurn = 'Y'    #ALTERNATING PLAYER TURN
                        turnIndicator()
                
                #YELLOW
                elif playerTurn == 'Y':
                    if(downCell!= -1):
                        GRID[i][downCell].fillAmount= 0
                        GRID[i][downCell].colourRGB = globals.YELLOW
                        GRID[i][downCell].colourSH= 'Y'
                        if checkWin(GRID):
                            if win == False:
                                yWins += 1
                                #drawText(yWins, score_font, (255,255,255), 100, 100)
                                win = True
                        playerTurn = 'R'    #ALTERNATING PLAYER TURN
                        turnIndicator()
                


    if win:
        pygame.display.update()
        pygame.time.delay(3000)
        GRID = resetBoard()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False
            
    pygame.display.update()
