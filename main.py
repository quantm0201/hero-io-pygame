import pygame, sys
from pygame.locals import *
from MenuScene import *
from GameScene import *


pygame.init()

SCREEN = pygame.display.set_mode((cf.WIDTH, cf.HEIGHT))

pygame.display.set_caption("Hero.io")

menuScene = MenuScene()

clock = pygame.time.Clock()

started = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if started:
            gameScene.receiveEvent(event)
        elif event.type == KEYDOWN:
            ret = menuScene.receiveKey(event.key)
            if ret == cf.CMD_QUIT:
                pygame.quit()
                sys.exit()
            elif ret != None:
                started = True
                gameScene = GameScene(ret)

    if started:
        gameScene.draw(SCREEN)
    else:
        menuScene.draw(SCREEN)
    pygame.display.update()
    clock.tick(cf.FPS)