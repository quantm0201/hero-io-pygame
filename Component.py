import pygame, sys
from pygame.locals import *
import Config as cf


class Text:
    def __init__(self, parent, pos, txt, color = cf.WHITE, size = 20):
        self.font = pygame.font.SysFont('consolas', size)
        self.text = txt
        self.color = color
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.center = pos
        self.parent = parent
        self.parent.blit(self.surface, self.rect)

    def setText(self, txt, parent):
        self.text = txt
        self.parent = parent
        self.reDraw()

    def setColor(self, color):
        self.color = color
        self.reDraw()
    
    def reDraw(self):
        self.surface = self.font.render(self.text, True, self.color)
        self.parent.blit(self.surface, self.rect)
    
class Animation:
    def __init__(self, res, amount, time, scale = 1):
        self.amount = amount
        self.time = time * cf.FPS
        self.deltaTime = self.time / amount
        self.countTime = 0
        self.index = 0
        self.effect = []
        self.isRunning = False
        self.isMove = False
        self.isRotate = False
        self.backPos = None
        self.surface = None

        for i in range(amount):
            step = pygame.image.load(res + str(i) + ".png")
            self.effect.append(step)

        if (scale != 1):
            w = int(self.effect[0].get_width() * scale)
            h = int(self.effect[0].get_height() * scale)
            for i in range(amount):
                self.effect[i] = pygame.transform.scale(self.effect[i], (w, h))


    def draw(self, surface):
        
        if (self.isMove):
            self.pos = (self.pos[0] + self.deltaX, self.pos[1] + self.deltaY)

        if (self.isRotate and self.isRunning):
            self.backPos = self.pos
            self.surface = pygame.transform.rotate(self.effect[self.index], -self.angle)
            rect = self.surface.get_rect(center = self.effect[self.index].get_rect().center)
            self.pos = (self.backPos[0] + rect.left , self.backPos[1] + rect.top)

        if (self.isRunning):
            self.countTime += 1
            if (self.countTime > self.deltaTime):
                self.countTime = 0
                self.index += 1
                if (self.index == self.amount):
                    self.stop()
                    return

            if (not self.isRotate):
                self.surface = self.effect[self.index]
            surface.blit(self.surface, self.pos)

            if (self.isRotate):
                self.pos = self.backPos

    def start(self, pos):
        self.pos = (pos[0] - self.effect[0].get_width() / 2, pos[1] - self.effect[1].get_height() / 2)
        self.countTime = 0
        self.index = 0
        self.isRunning = True
        self.isMove = False
        self.isRotate = False
        self.surface = self.effect[self.index]
        self.backPos = None

    def stop(self):
        self.isRunning = False
        self.isMove = False

    def setMove(self, cur, des):
        self.isMove = True
        self.deltaX = des[0] - cur[0]
        self.deltaY = des[1] - cur[1]

    def setRotate(self, angle):
        self.isRotate = True
        self.angle = angle