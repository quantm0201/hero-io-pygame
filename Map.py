import pygame, sys
from pygame.locals import *
import Config as cf
from Component import *
import random

class Map:
    def __init__(self, id, pos):
        self.id = id
        self.pos = pos
        self.surface = pygame.Surface((cf.BLOCK_SIZE*len(cf.MAP_1[0]), cf.BLOCK_SIZE*len(cf.MAP_1)), SRCALPHA)
        self.surface.fill(cf.GREEN)
        self.blocks = []
        self.tiles = []
        self.items = []
        for i in range(len(cf.MAP_1)):
            for j in range(len(cf.MAP_1[i])):
                tile = Tile(i*len(cf.MAP_1[i]) + j, (cf.BLOCK_SIZE*j, cf.BLOCK_SIZE*i), self.id)
                self.tiles.append(tile)
                if cf.MAP_1[i][j] != 0 and cf.MAP_1[i][j] != cf.HERO_1_ID and cf.MAP_1[i][j] != cf.HERO_2_ID:
                    block = Block(i*len(cf.MAP_1[i]) + j, (cf.BLOCK_SIZE*j, cf.BLOCK_SIZE*i), self.id, cf.MAP_1[i][j])
                    self.blocks.append(block)
    
    def draw(self, surface):
        self.update()
        surface.blit(self.surface, self.pos)
        self.surface.fill(cf.GREEN)
        for tile in self.tiles:
            tile.draw(self.surface)
        for block in self.blocks:
            block.draw(self.surface)
        for item in self.items:
            item.draw(self.surface)

    def update(self):
        if random.randint(0, 120) == 1:
            for i in range(len(cf.MAP_1)):
                for j in range(len(cf.MAP_1[i])):
                    if cf.MAP_1[i][j] == 0 and random.randint(0, 5*cf.FPS) == 0:
                        item = Item(i*len(cf.MAP_1[i]) + j, (cf.BLOCK_SIZE*j, cf.BLOCK_SIZE*i), self.id, random.randint(cf.ITEM_BULLET_ID, cf.ITEM_SPEED_ID))
                        self.items.append(item)
                        return None

    def getHeroInitPos(self, heroId):
        for i in range(len(cf.MAP_1)):
            for j in range(len(cf.MAP_1[i])):
                if cf.MAP_1[i][j] == heroId:
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
        for item in self.items:
            if item.checkCollidePoint(x, y):
                self.items.remove(item)
                return item.type
        return cf.NO_COLLISION

    def checkCollisionByFor(self, oldX, oldY, x, y):
        deltaX = (x - oldX) / cf.DETECT_SLICE
        deltaY = (y - oldY) / cf.DETECT_SLICE
        startX = x
        startY = y

        for i in range(cf.DETECT_SLICE):
            for block in self.blocks:
                if block.checkCollidePoint(startX, startY):
                    return True
            startX -= deltaX
            startY -= deltaY
        
        return False

tileImg = [1, 1, 1]
tileImg[0] = pygame.image.load("res/tile_desert.png")
tileImg[1] = pygame.image.load("res/tile_grass.png")
tileImg[2] = pygame.image.load("res/tile_ground.png")

moreBulletsImg = pygame.image.load("res/Bullet/moreBullets.png")
moreSpeedImg = pygame.image.load("res/Bullet/moreSpeed.png")

class Tile(pygame.sprite.Sprite):
    def __init__(self, id, pos, mapId):
        pygame.sprite.Sprite.__init__(self)

        self.id = id
        self.pos = pos
        self.mapId = mapId
        self.width = self.height = cf.BLOCK_SIZE

        self.setImage()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image.set_colorkey(cf.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos[0] + cf.BLOCK_SIZE//2, self.pos[1] + cf.BLOCK_SIZE//2)

    def setImage(self):
        self.image = tileImg[self.mapId]

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Block(Tile):
    def __init__(self, id, pos, mapId, type):
        self.type = type
        Tile.__init__(self, id, pos, mapId)

    def setImage(self):
        mapName = ""
        if self.mapId == cf.MAP_1_ID:
            mapName = "desert"
        elif self.mapId == cf.MAP_2_ID:
            mapName = "grass"
        else:
            mapName = "ground"
        self.image = pygame.image.load("res/block" + str(self.type) + "_" + mapName + ".png").convert()
    

    def checkCollidePoint(self, x, y):
        return self.pos[0] <= x <= self.pos[0] + self.width and self.pos[1] <= y <= self.pos[1] + self.height

class Item(Tile):
    def __init__(self, id, pos, mapId, type):
        self.type = type
        Tile.__init__(self, id, pos, mapId)

    def setImage(self):
        if self.type == cf.ITEM_BULLET_ID:
            self.image = moreBulletsImg
        elif self.type == cf.ITEM_SPEED_ID:
            self.image = moreSpeedImg

    def checkCollidePoint(self, x, y):
        return self.pos[0] <= x <= self.pos[0] + self.width and self.pos[1] <= y <= self.pos[1] + self.height