import block
import pygame
import player
import globals
import alien
import bullet
import random


class Game:
    def __init__(self):

        #setting up blocks
        self.shape = block.shape
        self.blockSize = 6
        self.blocks = pygame.sprite.Group()
        self.numBlocks = 4
        self.blockXPosses = [num * (globals.SCREEN_WIDTH/self.numBlocks) for num in range(self.numBlocks)]
        self.createAllBlocks(globals.SCREEN_WIDTH/15, 480, *self.blockXPosses)


        #setting up aliens
        self.aliens = []
        #self.alienSetup(6, 8)
        self.alienDirection = 1
        self.alienBullets = []

        self.score = 0
    

    def alienSetup(self, rows, cols):
        for rowIndex, row in enumerate(range(rows)):
            for colIndex, col in enumerate(range(cols)):
                x = colIndex * 60 + 70
                y = rowIndex * 48 + 100
                
                # Setting back aliens to different colours
                # will also give more points when hit
                if rowIndex == 0:
                    myAlien = alien.Alien(x, y, globals.BULE, 500)  
                elif rowIndex < 3:
                    myAlien = alien.Alien(x, y, globals.GREEN, 200)
                else:
                    myAlien = alien.Alien(x, y, globals.RED, 100)

                self.aliens.append(myAlien)
            
    def alienBorderCheck(self):
        for a in self.aliens:
            #Left check
            if a.rect.x <= 0:
                self.alienDirection = 1
                self.alienDown(2)

            #Right check
            elif a.rect.x + a.width >= globals.SCREEN_WIDTH:
                self.alienDirection = -1
                self.alienDown(2)

    def alienDown(self, distance):
        for a in self.aliens:
            a.rect.y += distance 

    def alienShoot(self):
        if self.aliens:
            someAlien = random.choice(self.aliens)
            aBullet = bullet.Bullet((someAlien.rect.x +someAlien.width/2), someAlien.rect.y + 10, 10, 5, -6)
            self.alienBullets.append(aBullet)
    

    def createBlock(self, xStart, yStart, offsetX):
        for rowIndex, row in enumerate (self.shape):
            for colIndex, col in enumerate(row):
                if col == 'x':
                    x = xStart + colIndex * self.blockSize + offsetX
                    y = yStart + rowIndex * self.blockSize
                    myBlock = block.Block(self.blockSize, globals.RED, x, y )
                    self.blocks.add(myBlock)

    def createAllBlocks(self, xStart, yStart, *offset):
        for offsetX in offset:
            self.createBlock(xStart, yStart, offsetX)


    def CollisionCheck(self, player):
        #player bullets
        if player.bullets:
            for b in player.bullets:
                #hit blocks
                if pygame.sprite.spritecollide(b, self.blocks, True): 
                    player.bullets.remove(b)
                
                #hit aliens
                for a in self.aliens: 
                    if pygame.Rect.colliderect(b.rect, a.rect):
                        self.score += a.score
                        player.bullets.remove(b)
                        self.aliens.remove(a)
        
        #alien bullets
        if self.alienBullets:
            for ab in self.alienBullets:
            #hit blocks
                if pygame.sprite.spritecollide(ab, self.blocks, True): 
                    self.alienBullets.remove(ab)

                if pygame.Rect.colliderect(ab.rect, player.rect):
                    player.health -= 1
                    self.alienBullets.remove(ab)
        
        #alien
        if self.aliens:
            for a in self.aliens:
                pygame.sprite.spritecollide(a, self.blocks, True)

                if pygame.Rect.colliderect(a.rect, player.rect):
                    player.health = 0



    def run(self, player, screen):
        
        #player actions
        player.update(screen)
        player.draw(screen)

        #setting up blocks
        self.blocks.draw(screen)

        #alien actions
        self.alienBorderCheck()
        self.CollisionCheck(player)
        for a in self.aliens:
            a.update(self.alienDirection)
            a.draw(screen)

        for ab in self.alienBullets:
            ab.update()
            ab.draw(screen)
            if ab.destroy():
                self.alienBullets.remove(ab)
