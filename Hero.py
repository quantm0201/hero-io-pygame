import pygame, sys
from pygame.locals import *
import Config as cf
from Component import *

class Hero:
    def __init__(self, id, parentMap):
        self.id = id
        if self.id == 0:
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
        self.surface.fill((0, 0, 0, 0))
    
    def draw(self, surface):
        self.update()
        self.rect.center = (self.x, self.y)
        surface.blit(self.surface, self.rect)
        pygame.draw.circle(self.surface, self.color, (cf.HERO_WIDTH//2, cf.HERO_HEIGHT//2), cf.HERO_SIZE//2)

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
    
    def receiveEvent(self, event):
        if event.type == KEYDOWN:
            if self.id == 0:
                if event.key == K_w:
                    self.movingUp = True
                if event.key == K_s:
                    self.movingDown = True
                if event.key == K_a:
                    self.movingLeft = True
                if event.key == K_d:
                    self.movingRight = True
        if event.type == KEYUP:
            if self.id == 0:
                if event.key == K_w:
                    self.movingUp = False
                if event.key == K_s:
                    self.movingDown = False
                if event.key == K_a:
                    self.movingLeft = False
                if event.key == K_d:
                    self.movingRight = False
        return None