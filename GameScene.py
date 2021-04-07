import pygame, sys
from pygame.locals import *
import Config as cf
from Component import *
from Map import Map
from Hero import Hero

class GameScene:
    def __init__(self):
        self.surface = pygame.Surface((cf.WIDTH, cf.HEIGHT), SRCALPHA)
        self.surface.fill(cf.DARK_GREEN)
        self.map = Map(1)
        self.hero1 = Hero(0, self.map.getHeroInitPos(0))
        self.hero2 = Hero(1, self.map.getHeroInitPos(1))

    def draw(self, surface):
        surface.blit(self.surface, (0, 0))
        self.map.draw(self.surface)
        self.hero1.draw(self.map.surface)
        self.hero2.draw(self.map.surface)

    def receiveKey(self, key):
        if (key == K_SPACE):
            print("shoot")
            self.hero1.shoot()
        return None
        