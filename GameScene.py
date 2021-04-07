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
        self.hero1 = Hero(cf.HERO_1_ID, self.map)
        self.hero2 = Hero(cf.HERO_2_ID, self.map)

    def draw(self, surface):
        surface.blit(self.surface, (0, 0))
        self.map.draw(self.surface)
        self.hero1.draw(self.map.surface)
        self.hero2.draw(self.map.surface)

    def receiveEvent(self, event):
        self.hero1.receiveEvent(event)
        self.hero2.receiveEvent(event)
        return None
        