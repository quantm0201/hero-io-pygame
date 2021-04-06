import pygame, sys
from pygame.locals import *
import Config as cf
from Component import *

class GameScene:
    def __init__(self):
        self.surface = pygame.Surface((cf.WITDH, cf.HEIGHT - 100), SRCALPHA)
        self.surface.fill(cf.DARK_GREEN)

    def draw(self, surface):
        surface.blit(self.surface, (0, 100))

    def receiveKey(self, key):
        return None
        