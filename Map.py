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
                    block = Block(i*len(cf.MAP_1[i]) + j,(cf.BLOCK_SIZE*j, cf.BLOCK_SIZE*i))
                    self.blocks.append(block)
    
    def draw(self, surface):
        surface.blit(self.surface, (0, 100))
        self.surface.fill(cf.GREEN)
        for block in self.blocks:
            block.draw(self.surface)

    def getHeroInitPos(self, heroId):
        for i in range(len(cf.MAP_1)):
            for j in range(len(cf.MAP_1[i])):
                if cf.MAP_1[i][j] == heroId + 2:
                    return cf.BLOCK_SIZE*j, cf.BLOCK_SIZE*i

    def checkCollision(self, oldX, oldY, x, y):
        coll = False
        collX = False
        collY = False
        for block in self.blocks:
            if block.checkCollidePoint(x, y):
                coll = True
            if block.checkCollidePoint(oldX, y):
                collY = True
            if block.checkCollidePoint(x, oldY):
                collX = True
        if coll:
            if collX and collY:
                return cf.COLLISON_BOTH
            elif collX:
                return cf.COLLISON_X
            elif collY:
                return cf.COLLISON_Y
        return cf.NO_COLLISION


class Block:
    def __init__(self, id, pos):
        self.id = id
        self.width = self.height = cf.BLOCK_SIZE
        self.pos = pos
        self.surface = pygame.Surface((self.width, self.height), SRCALPHA)
        self.surface.fill(cf.BLACK)

    def draw(self, surface):
        surface.blit(self.surface, self.pos)

    def checkCollidePoint(self, x, y):
        return self.pos[0] <= x <= self.pos[0] + self.width and self.pos[1] <= y <= self.pos[1] + self.height