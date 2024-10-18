import pygame
import globals
import player
import bullet
import game

screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
myPlayer = player.Player()

pygame.init()

resume = True
clock = pygame.time.Clock()
mygame = game.Game()
alienBullets = pygame.USEREVENT + 1
pygame.time.set_timer(alienBullets, 800)
textFont = pygame.font.SysFont('Arial', 30)
victoryFont = pygame.font.SysFont('Arial', 100)


def drawText(text, font, colour, x, y):
    img = font.render(text, True, colour)
    screen.blit(img, (x,y))

while resume:

    screen.fill(globals.BLACK)
    mygame.run(myPlayer, screen)

    drawText("Health: " + str(myPlayer.health), textFont, globals.WHITE, 0, 0)
    drawText("Score: " + str(mygame.score), textFont, globals.WHITE, globals.SCREEN_WIDTH/2, 0)

    if myPlayer.health == 0:
        resume = False
    
    if not mygame.aliens:
        drawText("VICTORY!", victoryFont, globals.WHITE, 115, 200)
        


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False
        if event.type == alienBullets:
            mygame.alienShoot()

    pygame.display.update()
    clock.tick(60)

pygame.quit()