import pygame, sys
from pygame.locals import *
import Config as cf
from Component import Point
from Util import *

bulletSrc = "res/Bullet/bullet1.png"

class Bullet:
    def __init__(self, id):
        self.id = id
        self.pos = Point(0, 0)
        self.surface = pygame.image.load(bulletSrc)
        self.surface = pygame.transform.scale(self.surface, (cf.BULLET_WIDTH, cf.BULLET_HEIGHT))
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

    def run(self, pos, vector):
        self.pos = pos
        self.vector = normalize(vector)
        self.countDieTime = 0
        self.isFree = False

    def updatePosition(self):
        deltaX = self.vector.x * cf.BULLET_SPEED / cf.FPS
        deltaY = self.vector.y * cf.BULLET_SPEED / cf.FPS
        self.pos.addDelta(deltaX, deltaY)


        

        
    # def draw(self, surface):

class BulletPool: 
    def __init__(self, amount):
        self.amount = amount
        self.bullets = []
        for i in range(amount):
            bullet = Bullet(i)
            self.bullets.append(bullet)

    # run bullet from "pos" with "vector" direction
    def shoot(self, pos, vector):
        for bullet in self.bullets:
            if (bullet.isFree):
                bullet.run(pos, vector)
                return

    def update(self, surface):
        for bullet in self.bullets:
            if (not bullet.isFree):
                bullet.update(surface)
    

        