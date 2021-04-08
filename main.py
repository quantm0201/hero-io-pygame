import pygame, sys
from pygame.locals import *
from MenuScene import *
from GameScene import *
from EndGameScene import *


pygame.init()

SCREEN = pygame.display.set_mode((cf.WIDTH, cf.HEIGHT))

pygame.display.set_caption("Hero.io")

menuScene = MenuScene()

clock = pygame.time.Clock()

started = False
ended = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if ended:
            ret = endGameScene.receiveEvent(event)
            cf.gameOverSound.play()
            pygame.mixer.music.pause()
            if ret:
                ended = False
                started = False
        elif started:
            gameScene.receiveEvent(event)
        elif event.type == KEYDOWN:
            ret = menuScene.receiveKey(event.key)
            if ret == cf.CMD_QUIT:
                pygame.quit()
                sys.exit()
            elif ret != None:
                started = True
                gameScene = GameScene(ret)
                pygame.mixer.music.play(-1)

    if started:
        gameScene.draw(SCREEN)
        if gameScene.endGame != 0:
            endGameScene = EndGameScene(gameScene.endGame)
            ended = True
    else:
        menuScene.draw(SCREEN)

    if ended:
        endGameScene.draw(SCREEN)
    
    pygame.display.update()
    clock.tick(cf.FPS)