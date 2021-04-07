import pygame, sys
from pygame.locals import *
from MenuScene import *
from GameScene import *


pygame.init()

SCREEN = pygame.display.set_mode((cf.WIDTH, cf.HEIGHT))

pygame.display.set_caption("Hero.io")

menuScene = MenuScene()
gameScene = GameScene()

FPS = 60
clock = pygame.time.Clock()

started = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if started:
                ret = gameScene.receiveKey(event.key)
            else:
                ret = menuScene.receiveKey(event.key)
            if ret == cf.QUIT:
                pygame.quit()
                sys.exit()
            if ret == cf.START_GAME:
                started = True

    if started:
        gameScene.draw(SCREEN)
    else:
        menuScene.draw(SCREEN)
    pygame.display.update()
    clock.tick(FPS)