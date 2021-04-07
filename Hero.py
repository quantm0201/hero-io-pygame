import pygame, sys
from pygame.locals import *
import Config as cf
from Component import *

class Hero:
    def __init__(self, id, initPos):
        self.id = id
        if self.id == 0:
            self.color = cf.RED
        else:
            self.color = cf.BLUE
        self.pos = initPos
        self.surface = pygame.Surface((cf.HERO_WIDTH, cf.HERO_HEIGHT), SRCALPHA)
        self.surface.fill((0, 0, 0, 0))
        self.rect_center = (cf.HERO_WIDTH//2, cf.HERO_HEIGHT//2)
        pygame.draw.circle(self.surface, self.color, self.rect_center, cf.HERO_SIZE//2)
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)