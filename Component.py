import pygame, sys
from pygame.locals import *
import Config as cf


class Text:
    def __init__(self, parent, txt, color = cf.WHITE, size = 20):
        self.font = pygame.font.SysFont('consolas', size)
        self.text = txt
        self.color = color
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.center = (parent.get_width()//2, parent.get_height()//2)
        self.parent = parent
        self.parent.blit(self.surface, self.rect)

    def setText(self, txt):
        self.text = txt
        self.reDraw()

    def setColor(self, color):
        self.color = color
        self.reDraw()
    
    def reDraw(self):
        self.surface = self.font.render(self.text, True, self.color)
        self.parent.blit(self.surface, self.rect)
    
        