import pygame
import cell

pygame.init()

screenWidth = 450
screenHeight = 600
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
screen = pygame.display.set_mode((screenWidth, screenHeight))


Grid = []
idCounter = 1
#Creating Cells
for i in range (3):
    Row = []
    for j in range(3):
        cells = cell.Cell(idCounter, 150, 150)
        idCounter += 1
        Row.append(cells)
    Grid.append(Row)


def CheckWin(grid):

    #Horizontal Wins
    j = 0
    for i in range(3):
        if grid[i][j].symbol != '':
            if (grid[i][j].symbol == grid[i][j + 1].symbol) and (grid[i][j].symbol == grid[i][j + 2].symbol):
                return True
    
    #Vertical Wins
    j = 0
    for i in range(3):
        if grid[j][i].symbol != '':
            if (grid[j][i].symbol == grid[j+1][i].symbol) and (grid[j][i].symbol == grid[j+2][i].symbol):
                return True

    #Diagonal Wins
    #Sloping TLBR
    if grid[0][0].symbol != '':
        if (grid[0][0].symbol == grid[1][1].symbol) and (grid[0][0].symbol == grid[2][2].symbol):
            return True

    #Sloping BLTR
    if grid[0][2].symbol != '':
        if (grid[0][2].symbol == grid[1][1].symbol) and (grid[0][2].symbol == grid[2][0].symbol):
            return True
    
    return False

resume = True
playerTurn = 'o'

while resume:

    screen.fill((255,255,255))

    #Making Turns 1v1
    for x in range(3):
        for y in range(3):
            if Grid[y][x].draw(screen, 150*x, 150*y):
                if playerTurn == 'x':
                    Grid[y][x].symbol = 'x'
                    Grid[y][x].colour = red
                    Grid[y][x].draw(screen, 150*x, 150*y)
                    playerTurn = 'o'
                    if CheckWin(Grid):
                        resume = False

                elif playerTurn == 'o':
                    Grid[y][x].symbol = 'o'
                    Grid[y][x].colour = green
                    Grid[y][x].draw(screen, 150*x, 150*y)
                    playerTurn = 'x'
                    if CheckWin(Grid):
                        resume = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False
    pygame.display.update()


pygame.quit()

