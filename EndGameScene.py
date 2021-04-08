import pygame, sys
from pygame.locals import *
import Config as cf
from Component import *

class EndGameScene:
    def __init__(self, winnerId):
        self.surface = pygame.image.load("res/victoryBg.png")
        self.rect = self.surface.get_rect()
        self.rect.center = (cf.WIDTH//2, cf.HEIGHT//2)

        txt = ""
        if winnerId == cf.HERO_1_ID:
            txt = "HERO 1 IS THE BOSS!"
        else:
            txt = "HERO 2 IS THE BOSS!"
        self.txtWinner = Text(self.surface, (self.surface.get_width()//2, self.surface.get_height()//2 - 20), txt, cf.YELLLOW, 15)
        self.txtEnter = Text(self.surface, (self.surface.get_width()//2, self.surface.get_height()//2 + 60), "Press Enter to continue...", cf.WHITE, 10)

    def draw(self, surface):
        surface.blit(self.surface, self.rect)

    def receiveEvent(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                return True
        return False