import pygame
import bullet
import globals

class Player:
    def __init__(self):
        self.height = 20
        self.width = 50
        
        self.rect = pygame.Rect((globals.SCREEN_WIDTH/2 - self.width/2), (globals.SCREEN_HEIGHT - self.height), self.width, self.height)

        self.health = 3

        self.ready = True
        self.bulletTime = 0
        self.coolDown = 600

        self.bullets = []

    def draw(self, screen):
        pygame.draw.rect(screen, globals.WHITE, self.rect)
        

    def shootBullet(self):
        newBullet = bullet.Bullet(self.rect.x + (self.width/2), self.rect.y - 10, 10,5, 5)
        self.bullets.append(newBullet)


    def input(self):

        key = pygame.key.get_pressed()
        #player movement
        if(key[pygame.K_a] or key[pygame.K_LEFT]):
            if(self.rect.x >=0):
                self.rect.x -= 5
        if(key[pygame.K_d] or key[pygame.K_RIGHT]):
            if(self.rect.x <= globals.SCREEN_WIDTH - 30):
                self.rect.x += 5

        if(key[pygame.K_SPACE] and self.ready):
            self.shootBullet()
            self.ready = False
            self.bulletTime = pygame.time.get_ticks()
    
    def reload(self):
        if self.ready == False:
            currentTime = pygame.time.get_ticks()
            if (currentTime - self.bulletTime) >= self.coolDown:
                self.ready = True
            
    
    def update(self, screen):
        self.input()
        self.reload()

        #Draw all Lasers and move them
        for bullet in self.bullets:
            bullet.update()
            bullet.draw(screen)
            if bullet.destroy():
                self.bullets.remove(bullet)
