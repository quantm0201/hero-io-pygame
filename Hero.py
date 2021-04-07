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
        self.x = parentMap.getHeroInitPos(id)[0]
        self.y = parentMap.getHeroInitPos(id)[1]

        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False

        self.speedPxPerFr = cf.HERO_BASE_SPEED_PX_PER_FR

        self.surface = pygame.Surface((cf.HERO_WIDTH, cf.HERO_HEIGHT), SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect_center = (cf.HERO_WIDTH//2, cf.HERO_HEIGHT//2)


        # bullet
        self.direction = Point(1, 0)
        self.bulletPool = BulletPool(10)
        self.upDirection = False
        self.downDirection = True


    def shoot(self):
        pos = Point(self.x, self.y)
        self.bulletPool.shoot(pos, self.direction)
    
    def draw(self, surface):
        self.update()
        self.rect.center = (self.x, self.y)
        surface.blit(self.surface, self.rect)
        pygame.draw.circle(self.surface, self.color, (cf.HERO_WIDTH//2, cf.HERO_HEIGHT//2), cf.HERO_SIZE//2)

        # bullet
        self.bulletPool.update(surface)
        

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
            return
        else:
            return