import globals

class Bot:
    def __init__(self):
        pass

    def EvenHeightMove(self, snake):
        
        if snake.xDirection == 0 and snake.yDirection == 0:
            started = False
        else:
            started =  True

        #First move of a new game is to move the snake to the edge of the grid
        if started == False:
            self.Movesnake('L', snake)

        #Gathering current head position and second cell to determine best move
        headPos = snake.bodyPosition[0]
        secCellPos = snake.bodyPosition[1]

        if headPos[0] == 0:
            self.Movesnake('D', snake)

        #Makes turn at bottom left corner
        if headPos[1] == globals.SCREEN_HEIGHT - globals.GRIDSQSIZE:
            self.Movesnake('R', snake)

        #ZIGZAG MOVEMENT
        #Checking right most border
        #Making 180
        if headPos[0] == globals.SCREEN_WIDTH - globals.GRIDSQSIZE:
            self.Movesnake('U', snake)

        if headPos[0] == globals.SCREEN_WIDTH - globals.GRIDSQSIZE and headPos[1] != secCellPos[1]:
            self.Movesnake('L', snake)

        #Checking Left side of zigzag area
        if headPos[0] == globals.GRIDSQSIZE and headPos[1] != globals.SCREEN_HEIGHT - globals.GRIDSQSIZE  and started and headPos[1]!=0:
            self.Movesnake('U', snake)

        if headPos[0] == globals.GRIDSQSIZE and headPos[1] != secCellPos[1]:
            self.Movesnake('R', snake)

    def BothDimOddMove(self, snake, apples):
    
        #Checks if there is currently an apple in the 
        #top right of the grid
        appleTR = False

        for a in apples:
            if a.x == globals.SCREEN_WIDTH-globals.GRIDSQSIZE and a.y == 0:
                appleTR = True            

        if snake.xDirection == 0 and snake.yDirection == 0:
            started = False
        else:
            started =  True

        #First move of a new game is to move the snake to the edge of the grid
        if started == False:
            self.Movesnake('L', snake)
            return #Finsh method early for effiency

        #Gathering current head position and second cell to determine best move
        headPos = snake.bodyPosition[0]
        secCellPos = snake.bodyPosition[1]
        if headPos[0] == 0:
            self.Movesnake('D', snake)

        #Makes turn at bottom left corner
        if headPos[1] == globals.SCREEN_HEIGHT - globals.GRIDSQSIZE:
            self.Movesnake('R', snake)

        #ZIGZAG MOVEMENT
        #Checking right most border
        #Making 180
        if headPos[0] == globals.SCREEN_WIDTH - globals.GRIDSQSIZE:
            self.Movesnake('U', snake)

        if headPos[0] == globals.SCREEN_WIDTH - globals.GRIDSQSIZE and headPos[1] != secCellPos[1] and headPos[1] != globals.GRIDSQSIZE:
            self.Movesnake('L', snake)

        #Checking Left side of zigzag area
        if headPos[0] == globals.GRIDSQSIZE and headPos[1] != globals.SCREEN_HEIGHT - globals.GRIDSQSIZE  and started and headPos[1]!=0:
            self.Movesnake('U', snake)

        if headPos[0] == globals.GRIDSQSIZE and headPos[1] != secCellPos[1]:
            self.Movesnake('R', snake)


        #TOP 2 ROWS ZIGZAG
        #Path if apple is currently in top right of grid
        if appleTR:
            #Top Border
            if headPos[1] == 0 and headPos[0] < globals.SCREEN_WIDTH - (globals.GRIDSQSIZE)*2:
                self.Movesnake('D', snake)

            if headPos[1] == 0 and headPos != 0 and headPos[0] == secCellPos[0]:
                self.Movesnake('L', snake)

            #Bottom border
            if headPos[1] == globals.GRIDSQSIZE and headPos[0] != globals.SCREEN_WIDTH - globals.GRIDSQSIZE and headPos[0]!=0:
                self.Movesnake('L', snake)

            if headPos[1] == globals.GRIDSQSIZE and headPos[0] != globals.SCREEN_WIDTH - globals.GRIDSQSIZE and headPos[1] == secCellPos[1]:
                self.Movesnake('U', snake)

        #Default path
        else:
            #Top Border
            if headPos[1] == 0 and headPos[0] < globals.SCREEN_WIDTH - (globals.GRIDSQSIZE)*2:
                self.Movesnake('D', snake)

            if headPos[1] == 0 and headPos != 0 and headPos[0] == secCellPos[0]:
                self.Movesnake('L', snake)

            #Bottom border
            if headPos[1] == globals.GRIDSQSIZE and headPos[0]!=0:
                self.Movesnake('L', snake)

            if headPos[1] == globals.GRIDSQSIZE and headPos[0] != globals.SCREEN_WIDTH - globals.GRIDSQSIZE and headPos[1] == secCellPos[1]:
                self.Movesnake('U', snake)

    
    def OddHeightEvenLength(self, snake):
            
        if snake.xDirection == 0 and snake.yDirection == 0:
            started = False
        else:
            started =  True

        #First move of a new game is to move the snake to the edge of the grid
        if started == False:
            self.Movesnake('R', snake)
            return #Finsh method early for effiency

        #Gathering current head position and second cell to determine best move
        headPos = snake.bodyPosition[0]
        secCellPos = snake.bodyPosition[1]

        if headPos[1] == 0:
            self.Movesnake('R', snake)

        #Makes turn at top right corner
        if headPos[0] == globals.SCREEN_WIDTH - globals.GRIDSQSIZE:
            self.Movesnake('D', snake)


        #ZIGZAG MOVEMENT
        #Checking bottom most border
        #Making 180
        if headPos[1] == globals.SCREEN_HEIGHT - globals.GRIDSQSIZE:
            self.Movesnake('L', snake)

        if headPos[1] == globals.SCREEN_HEIGHT - globals.GRIDSQSIZE and headPos[0] != secCellPos[0]:
            self.Movesnake('U', snake)

        #Checking top side of zigzag area
        if headPos[1] == globals.GRIDSQSIZE and headPos[0] != globals.SCREEN_WIDTH -globals.GRIDSQSIZE  and started and headPos[0]!=0:
            self.Movesnake('L', snake)

        if headPos[1] == globals.GRIDSQSIZE and headPos[0] != secCellPos[0]:
            self.Movesnake('D', snake)

    def Movesnake(self, dir, snake):
        #UP
        if dir == 'U':
            snake.xDirection = 0
            snake.yDirection = -globals.GRIDSQSIZE

        #DOWN
        if dir == 'D':
            snake.xDirection = 0
            snake.yDirection = globals.GRIDSQSIZE

        #LEFT
        if dir == 'L':
            snake.xDirection = -globals.GRIDSQSIZE
            snake.yDirection = 0

        #RIGHT
        if dir == 'R':
            snake.xDirection = globals.GRIDSQSIZE
            snake.yDirection = 0