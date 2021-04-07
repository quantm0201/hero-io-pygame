import pygame, sys
from pygame.locals import *
import Config as cf
from Util import *

bulletSrc = "res/Bullet/bullet1.png"

class Bullet:
    def __init__(self, id, mainMap, bulletPool):
        self.id = id
        self.mainMap = mainMap
        self.bulletPool = bulletPool
        self.surfaceOrigin = pygame.image.load(bulletSrc)
        self.surfaceOrigin = pygame.transform.scale(self.surfaceOrigin, (cf.BULLET_WIDTH, cf.BULLET_HEIGHT))
        self.pos = Point(0, 0)
        self.isFree = True

        # State
        self.countDieTime = 0
        

    def update(self, surface):
        if self.countDieTime > cf.BULLET_TIME_TO_DIE * cf.FPS:
            self.free()

        if (not self.isFree):
            self.updatePosition()
            self.countDieTime += 1
        
        surface.blit(self.surface, self.pos.getValue())

    def free(self):
        self.isFree = True

    def run(self, pos, vector, angle):

        posX = pos.x - self.surfaceOrigin.get_width() / 2
        posY = pos.y - self.surfaceOrigin.get_height() / 2

        # self.pos = Point(posX, posY)
        self.vector = normalize(vector)
        self.angle = angle
        self.countDieTime = 0
        self.isFree = False
        self.surface = pygame.transform.rotate(self.surfaceOrigin, -self.angle)
        self.rect = self.surface.get_rect(center = self.surfaceOrigin.get_rect().center)
        self.pos = Point(posX + self.rect.left, posY + self.rect.top)

    def updatePosition(self):
        oldPos = (self.pos.x + self.surface.get_width() / 2, self.pos.y + self.surface.get_width() / 2)

        deltaX = self.vector.x * cf.BULLET_SPEED / cf.FPS
        deltaY = self.vector.y * cf.BULLET_SPEED / cf.FPS
        self.pos.addDelta(deltaX, deltaY)

        newPos = (self.pos.x + self.surface.get_width() / 2, self.pos.y + self.surface.get_width() / 2)

        state = self.mainMap.checkCollisionByFor(oldPos[0], oldPos[1], newPos[0], newPos[1])
        if state:
            self.free()

        state = self.bulletPool.checkCollisionOponent(oldPos[0], oldPos[1], newPos[0], newPos[1])
        if state:
            self.free()
            print("Hited Oponent id: " + str(self.bulletPool.oponent.id))

    

        
    # def draw(self, surface):

class BulletPool: 
    def __init__(self, amount, mainMap):
        self.amount = amount
        self.mainMap = mainMap
        self.bullets = []
        for i in range(amount):
            bullet = Bullet(i, self.mainMap, self)
            self.bullets.append(bullet)

    # run bullet from "pos" with "vector" direction
    def shoot(self, pos, vector, angle):
        for bullet in self.bullets:
            if (bullet.isFree):
                bullet.run(pos, vector, angle)
                return

    def update(self, surface):
        for bullet in self.bullets:
            if (not bullet.isFree):
                bullet.update(surface)

    def setOponent(self, oponent):
        self.oponent = oponent

    def checkCollisionOponent(self, oldX, oldY, x, y):
        deltaX = (x - oldX) / cf.DETECT_SLICE
        deltaY = (y - oldY) / cf.DETECT_SLICE
        startX = x
        startY = y

        oponentPos = self.oponent.rect

        for i in range(cf.DETECT_SLICE):
            state = oponentPos.left <= x <= oponentPos.left + cf.HERO_WIDTH and oponentPos.top <= y <= oponentPos.top + cf.HERO_HEIGHT
            if state:
                return True

            startX -= deltaX
            startY -= deltaY
        
        return False

        