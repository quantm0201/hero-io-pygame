import pygame, sys
from pygame.locals import *
import Config as cf
from Component import *
from Bullet import *
from Util import *

class Hero:
    def __init__(self, id, parentMap):
        self.id = id
        if self.id == cf.HERO_1_ID:
            self.color = cf.RED
        else:
            self.color = cf.BLUE

        self.parentMap = parentMap
        self.respawn()

        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False

        if (id == cf.HERO_1_ID):
            self.surface = pygame.image.load("res/player/player1.png")
        else:
            self.surface = pygame.image.load("res/player/player2.png")
        
        self.surface = pygame.transform.scale(self.surface, (cf.HERO_WIDTH, cf.HERO_HEIGHT))
        self.rect = self.surface.get_rect()

        # bullet
        self.direction = cf.FORWARD_DIRECTION
        self.forward = cf.FORWARD_DIRECTION
        self.angle = 0
        self.bulletPool = BulletPool(10, self.parentMap, self)
        self.upDirection = False
        self.downDirection = False

        # Gun
        self.gunOrigin = pygame.image.load("res/Bullet/gun2.png")
        self.gunOrigin = pygame.transform.scale(self.gunOrigin, (16, 70))

        # Effect
        self.fireShot = Animation("res/effect/fireshot", 4, 0.5, 0.7)
        self.explode = Animation("res/effect/Explosion", 8, 1, 0.3)

        # score
        self.score = 0

    def setOponent(self, oponent):
        self.bulletPool.setOponent(oponent)


    def shoot(self):
        pos = Point(self.x, self.y)
        self.bulletPool.shoot(pos, self.direction, self.angle)

        
        self.fireShot.start((self.x, self.y))

    def die(self):
        self.isDead = True
    
    def respawn(self):
        self.isDead = False
        self.alpha = 255
        self.x = self.parentMap.getHeroInitPos(self.id)[0]
        self.y = self.parentMap.getHeroInitPos(self.id)[1]
        self.speedPxPerFr = cf.HERO_BASE_SPEED_PX_PER_FR

    def addScore(self, score):
        self.score += score
    
    def draw(self, surface):
        self.update()
        self.rect.center = (self.x, self.y)
        # bullet
        self.bulletPool.update(surface)
        # gun
        self.drawGun(surface)

        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.rect)

        # effect
        self.fireShot.setRotate(self.angle)
        self.fireShot.draw(surface)
        
        self.explode.draw(surface)
        


    def update(self):
        if self.movingLeft or self.movingDown or self.movingUp or self.movingRight:
            x = self.x
            y = self.y
            if self.movingUp and self.movingLeft:
                x = self.x - self.speedPxPerFr/1.4
                y = self.y - self.speedPxPerFr/1.4
            elif self.movingUp and self.movingRight:
                x = self.x + self.speedPxPerFr/1.4
                y = self.y - self.speedPxPerFr/1.4
            elif self.movingUp:
                y = self.y - self.speedPxPerFr
            elif self.movingDown and self.movingLeft:
                x = self.x - self.speedPxPerFr/1.4
                y = self.y + self.speedPxPerFr/1.4
            elif self.movingDown and self.movingRight:
                x = self.x + self.speedPxPerFr/1.4
                y = self.y + self.speedPxPerFr/1.4
            elif self.movingDown:
                y = self.y + self.speedPxPerFr
            elif self.movingLeft:
                x = self.x - self.speedPxPerFr
            elif self.movingRight:
                x = self.x + self.speedPxPerFr
            ret = self.parentMap.checkCollision(self.x, self.y, x, y)
            if ret == cf.COLLISON_X:
                x = self.x
            if ret == cf.COLLISON_Y:
                y = self.y
            if ret == cf.COLLISON_BOTH:
                x = self.x
                y = self.y
            self.x = x
            self.y = y

        # bullet
        if self.upDirection and self.downDirection:
            return
        elif self.upDirection:
            self.changeDirection(cf.UP_DIRECTION_STATE)
        elif self.downDirection:
            self.changeDirection(cf.DOWN_DIRECTION_STATE)
                
        # alive state
        if self.isDead:
            self.blur()

    
    def receiveEvent(self, event):
        if event.type == KEYDOWN:
            if event.key == cf.HERO_KEY[self.id].get("kUp"):
                self.movingUp = True
            if event.key == cf.HERO_KEY[self.id].get("kDown"):
                self.movingDown = True
            if event.key == cf.HERO_KEY[self.id].get("kLeft"):
                self.movingLeft = True
            if event.key == cf.HERO_KEY[self.id].get("kRight"):
                self.movingRight = True
            if event.key == cf.HERO_KEY[self.id].get(cf.K_ATTACK):
                self.shoot()
            if event.key == cf.HERO_KEY[self.id].get(cf.K_UP_DIRECTION):
                self.upDirection = True
            if event.key == cf.HERO_KEY[self.id].get(cf.K_DOWN_DIRECTION):
                self.downDirection = True
        if event.type == KEYUP:
            if event.key == cf.HERO_KEY[self.id].get("kUp"):
                self.movingUp = False
            if event.key == cf.HERO_KEY[self.id].get("kDown"):
                self.movingDown = False
            if event.key == cf.HERO_KEY[self.id].get("kLeft"):
                self.movingLeft = False
            if event.key == cf.HERO_KEY[self.id].get("kRight"):
                self.movingRight = False
            if event.key == cf.HERO_KEY[self.id].get(cf.K_UP_DIRECTION):
                self.upDirection = False
            if event.key == cf.HERO_KEY[self.id].get(cf.K_DOWN_DIRECTION):
                self.downDirection = False
        return None

    def changeDirection(self, state):
        if (state == cf.UP_DIRECTION_STATE):
            self.angle = (self.angle - cf.DIRECTION_SPEED) % 360
        else:
            self.angle = (self.angle + cf.DIRECTION_SPEED) % 360

        radian = self.angle * cf.DEGREE_TO_RADIAN
        dirX = self.forward.x * math.cos(radian) - self.forward.y * math.sin(radian)
        dirY = self.forward.x * math.sin(radian) + self.forward.y * math.cos(radian)
        self.direction = Point(dirX, dirY)
    
    def blur(self):
        if self.alpha - 5 > 0:
            self.alpha -= 5
        elif self.alpha > 0:
            self.alpha = 0
        

    def drawGun(self, surface): 
        self.gunPos = (self.x - self.gunOrigin.get_width() / 2, self.y - self.gunOrigin.get_height() / 2)

        self.gun = pygame.transform.rotate(self.gunOrigin, -self.angle)
        rect = self.gun.get_rect(center = self.gunOrigin.get_rect().center)
        self.gunPos = (self.gunPos[0] + rect.left, self.gunPos[1] + rect.top)
        self.gun.set_alpha(self.alpha)
        surface.blit(self.gun, self.gunPos)