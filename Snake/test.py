#Attempting to change the first element in the array
#then shift every other element down one index
#discarding the last value


#MYNUMS = [12,13,14,15,16,17,18,19]
MYNUMS = [[20, 40], [20, 60], [20,80], [20,100], [20,120]]

MYNUMS.insert(0, [20, 20])
MYNUMS.pop()


#temp = MYNUMS[1]
#MYNUMS[1] = MYNUMS[0]
#MYNUMS[0] = 27
#
#temp2 = 0
#
#for i in range(2, len(MYNUMS), 1):
#    if i%2 == 0:
#        temp2 = MYNUMS[i]
#        MYNUMS[i] = temp
#    elif i%2 == 1:
#        temp = MYNUMS[i]
#        MYNUMS[i] = temp2


#Loopable
#temp2 = MYNUMS[2]
#MYNUMS[2] = temp
#
#temp = MYNUMS[3]
#MYNUMS[3] = temp2
#
#temp2 = MYNUMS[4]
#MYNUMS[4] = temp
#
#temp = MYNUMS[5]
#MYNUMS[5] = temp2
#
#temp2 = MYNUMS[6]
#MYNUMS[6] = temp
#
#temp = MYNUMS[7]
#MYNUMS[7] = temp2


#print(MYNUMS)


#BOT IDEAS

#ZigZagOptions

        #ZIGZAG MOVEMENT
        #Checking right most border
        #Making 180
        #if headPos[0] == globals.SCREEN_WIDTH - gridSqSize:
            #MoveSnake('U')
        #BotZigZagFarBoundary(headPos, secCellPos, (globals.SCREEN_WIDTH - gridSqSize), 'U', False )

        #if headPos[0] == globals.SCREEN_WIDTH - gridSqSize and headPos[1] != secCellPos[1]:
            #MoveSnake('L')
        #BotZigZagFarBoundary(headPos, secCellPos, (globals.SCREEN_WIDTH - gridSqSize), 'L', True)

        #Checking Left side of zigzag area
        #if headPos[0] == gridSqSize and headPos[1] != globals.SCREEN_HEIGHT - gridSqSize  and started and headPos[1]!=0:
            #MoveSnake('U')

        #if headPos[0] == gridSqSize and headPos[1] != secCellPos[1]:
            #MoveSnake('R')

#def BotZigZagFarBoundary(headPos, secCellPos, cordsToTurnAt, moveDir, extraReq):

 #   if extraReq is False:
  #      if headPos[0] == cordsToTurnAt:
    #        MoveSnake(moveDir)
   # else:
     #   if headPos[0] == cordsToTurnAt and headPos[1] != secCellPos[1]:
      #      MoveSnake(moveDir)