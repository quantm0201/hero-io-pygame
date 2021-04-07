import pygame, sys
from pygame.locals import *
import Config as cf
from Component import *

class Map:
    def __init__(self, id):
        self.id = id
        self.surface = pygame.Surface((cf.BLOCK_SIZE*len(cf.MAP_1[0]), cf.BLOCK_SIZE*len(cf.MAP_1)), SRCALPHA)
        self.surface.fill(cf.GREEN)
        self.blocks = []
        for i in range(len(cf.MAP_1)):
            for j in range(len(cf.MAP_1[i])):
                if cf.MAP_1[i][j] == 1:
                    block = Block(self.surface, (cf.BLOCK_SIZE*j, cf.BLOCK_SIZE*i))
                    self.blocks.append(block)
    
    def draw(self, surface):
        surface.blit(self.surface, (0, 100))

    def getHeroInitPos(self, heroId):
        for i in range(len(cf.MAP_1)):
            for j in range(len(cf.MAP_1[i])):
                if cf.MAP_1[i][j] == heroId + 2:
                    return cf.BLOCK_SIZE*j, cf.BLOCK_SIZE*i


class Block:
    def __init__(self, parent, pos):
        self.width = self.height = cf.BLOCK_SIZE
        self.pos = pos
        self.surface = pygame.Surface((self.width, self.height), SRCALPHA)
        self.surface.fill(cf.BLACK)
        self.rect = self.surface.get_rect()
        parent.blit(self.surface, self.pos)