import pygame, sys
from pygame.locals import *
import Config as cf
from Component import *

class MenuScene:
    def __init__(self):
        self.surface = pygame.Surface((cf.WIDTH, cf.HEIGHT), SRCALPHA)
        self.surface.fill(cf.BLACK + (110,))

        self.btnMap1 = pygame.Surface((200, 100), SRCALPHA)
        self.btnMap1_rect = self.btnMap1.get_rect()
        self.btnMap1_rect.center = (cf.WIDTH/4, cf.HEIGHT/5)
        self.map1Txt = Text(self.btnMap1,"DESERT", cf.WHITE, 30)

        self.btnMap2 = pygame.Surface((200, 100), SRCALPHA)
        self.btnMap2_rect = self.btnMap2.get_rect()
        self.btnMap2_rect.center = (cf.WIDTH/4, cf.HEIGHT*2/5)
        self.map2Txt = Text(self.btnMap2,"FOREST", cf.WHITE, 30)

        self.btnMap3 = pygame.Surface((200, 100), SRCALPHA)
        self.btnMap3_rect = self.btnMap3.get_rect()
        self.btnMap3_rect.center = (cf.WIDTH/4, cf.HEIGHT*3/5)
        self.map3Txt = Text(self.btnMap3,"YARD", cf.WHITE, 30)

        self.btnQuit = pygame.Surface((200, 100), SRCALPHA)
        self.btnQuit_rect = self.btnQuit.get_rect()
        self.btnQuit_rect.center = (cf.WIDTH/2, cf.HEIGHT*4/5)
        self.quitTxt = Text(self.btnQuit, "QUIT", cf.WHITE, 30)

        self.select = cf.CMD_MAP_1
        self.changeSelect()

    def draw(self, surface):
        surface.blit(self.surface, (0, 0))

    def receiveKey(self, key):
        if key == K_UP:
            if self.select == cf.CMD_QUIT:
                self.select = cf.CMD_MAP_3
            elif self.select == cf.CMD_MAP_3:
                self.select = cf.CMD_MAP_2
            elif self.select == cf.CMD_MAP_2:
                self.select = cf.CMD_MAP_1
            self.changeSelect()
        if key == K_DOWN:
            if self.select == cf.CMD_MAP_1:
                self.select = cf.CMD_MAP_2
            elif self.select == cf.CMD_MAP_2:
                self.select = cf.CMD_MAP_3
            elif self.select == cf.CMD_MAP_3:
                self.select = cf.CMD_QUIT
            self.changeSelect()
        if key == K_RETURN:
            return self.select
        return None

    def changeSelect(self):
        if self.select == cf.CMD_MAP_1:
            self.btnMap1.fill(cf.WHITE)
            self.map1Txt.setColor(cf.BLACK)
            self.btnMap2.fill(cf.BLACK)
            self.map2Txt.setColor(cf.WHITE)
            self.btnMap3.fill(cf.BLACK)
            self.map3Txt.setColor(cf.WHITE)
            self.btnQuit.fill(cf.BLACK)
            self.quitTxt.setColor(cf.WHITE)
            self.bg = pygame.image.load("res/bg_desert.png").convert()
        if self.select == cf.CMD_MAP_2:
            self.btnMap2.fill(cf.WHITE)
            self.map2Txt.setColor(cf.BLACK)
            self.btnMap1.fill(cf.BLACK)
            self.map1Txt.setColor(cf.WHITE)
            self.btnMap3.fill(cf.BLACK)
            self.map3Txt.setColor(cf.WHITE)
            self.btnQuit.fill(cf.BLACK)
            self.quitTxt.setColor(cf.WHITE)
            self.bg = pygame.image.load("res/bg_grass.jpg").convert()
        if self.select == cf.CMD_MAP_3:
            self.btnMap3.fill(cf.WHITE)
            self.map3Txt.setColor(cf.BLACK)
            self.btnMap2.fill(cf.BLACK)
            self.map2Txt.setColor(cf.WHITE)
            self.btnMap1.fill(cf.BLACK)
            self.map1Txt.setColor(cf.WHITE)
            self.btnQuit.fill(cf.BLACK)
            self.quitTxt.setColor(cf.WHITE)
            self.bg = pygame.image.load("res/bg_ground.jpg").convert()
        if self.select == cf.CMD_QUIT:
            self.btnQuit.fill(cf.WHITE)
            self.quitTxt.setColor(cf.BLACK)
            self.btnMap1.fill(cf.BLACK)
            self.map1Txt.setColor(cf.WHITE)
            self.btnMap2.fill(cf.BLACK)
            self.map2Txt.setColor(cf.WHITE)
            self.btnMap3.fill(cf.BLACK)
            self.map3Txt.setColor(cf.WHITE)
        self.surface.blit(self.btnMap1, self.btnMap1_rect)
        self.surface.blit(self.btnMap2, self.btnMap2_rect)
        self.surface.blit(self.btnMap3, self.btnMap3_rect)
        self.surface.blit(self.btnQuit, self.btnQuit_rect)
        self.bg = pygame.transform.scale(self.bg, (500, 380))
        self.bg_rect = self.bg.get_rect()
        self.bg_rect.center = (cf.WIDTH*3/4 - 100, cf.HEIGHT*2/5)
        self.surface.blit(self.bg, self.bg_rect)
        