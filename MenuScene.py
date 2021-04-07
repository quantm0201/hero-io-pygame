import pygame, sys
from pygame.locals import *
import Config as cf
from Component import *

class MenuScene:
    def __init__(self):
        self.surface = pygame.Surface((cf.WIDTH, cf.HEIGHT), SRCALPHA)
        self.surface.fill(cf.BLACK + (110,))

        self.btnStart = pygame.Surface((200, 100), SRCALPHA)
        self.btnStart_rect = self.btnStart.get_rect()
        self.btnStart_rect.center = (cf.WIDTH/2, cf.HEIGHT/2 - 100)
        self.statTxt = Text(self.btnStart,"START", cf.WHITE, 30)

        self.btnQuit = pygame.Surface((200, 100), SRCALPHA)
        self.btnQuit_rect = self.btnQuit.get_rect()
        self.btnQuit_rect.center = (cf.WIDTH/2, cf.HEIGHT/2 + 100)
        self.quitTxt = Text(self.btnQuit, "QUIT", cf.WHITE, 30)

        self.select = cf.START_GAME
        self.changeSelect()

    def draw(self, surface):
        surface.blit(self.surface, (0, 0))

    def receiveKey(self, key):
        if key == K_UP:
            if self.select == cf.QUIT:
                self.select = cf.START_GAME
                self.changeSelect()
        if key == K_DOWN:
            if self.select == cf.START_GAME:
                self.select = cf.QUIT
                self.changeSelect()
        if key == K_RETURN:
            return self.select
        return None

    def changeSelect(self):
        if self.select == cf.START_GAME:
            self.btnStart.fill(cf.WHITE)
            self.statTxt.setColor(cf.BLACK)
            self.btnQuit.fill(cf.BLACK)
            self.quitTxt.setColor(cf.WHITE)
        if self.select == cf.QUIT:
            self.btnQuit.fill(cf.WHITE)
            self.quitTxt.setColor(cf.BLACK)
            self.btnStart.fill(cf.BLACK)
            self.statTxt.setColor(cf.WHITE)
        self.surface.blit(self.btnStart, self.btnStart_rect)
        self.surface.blit(self.btnQuit, self.btnQuit_rect)
        