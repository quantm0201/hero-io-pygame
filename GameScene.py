import pygame, sys
from pygame.locals import *
import Config as cf
from Component import *
from Map import Map
from Hero import Hero

class GameScene:
    def __init__(self, map_cmd):
        self.surface = pygame.Surface((cf.WIDTH, cf.HEIGHT), SRCALPHA)
        self.surface.fill(cf.BLACK)

        mapPos = (0, 100)
        if map_cmd == cf.CMD_MAP_1:
            self.map = Map(cf.MAP_1_ID, mapPos)
        if map_cmd == cf.CMD_MAP_2:
            self.map = Map(cf.MAP_2_ID, mapPos)
        if map_cmd == cf.CMD_MAP_3:
            self.map = Map(cf.MAP_3_ID, mapPos)
        self.hero1 = Hero(cf.HERO_1_ID, self.map)
        self.hero2 = Hero(cf.HERO_2_ID, self.map)
        
        self.hero1.setOponent(self.hero2)
        self.hero2.setOponent(self.hero1)

        self.scoreBg = pygame.image.load("res/scoreBg.png").convert()
        self.lblHero1_score = pygame.transform.scale(self.scoreBg, (200, 100))
        self.lbl1_rect = self.lblHero1_score.get_rect()
        self.lbl1_rect.center = (200, 50)
        self.lblHero1_scoreTxt = Text(self.lblHero1_score, (100, 30),"Hero 1 Score: " + str(self.hero1.score), cf.WHITE, 20)
        self.lblHero1_bulletTxt = Text(self.lblHero1_score, (100, 70), "Bullets: " + str(self.hero1.numBullet), cf.YELLLOW, 12)

        self.lblHero2_score = pygame.transform.scale(self.scoreBg, (200, 100))
        self.lbl2_rect = self.lblHero2_score.get_rect()
        self.lbl2_rect.center = (cf.WIDTH - 200, 50)
        self.lblHero2_scoreTxt = Text(self.lblHero2_score, (100, 30), "Hero 2 Score: " + str(self.hero2.score), cf.WHITE, 20)
        self.lblHero2_bulletTxt = Text(self.lblHero2_score, (100, 70), "Bullets: " + str(self.hero2.numBullet), cf.YELLLOW, 12)

        self.logo = cf.GAME_LOGO
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.center = (cf.WIDTH//2, 50)
        self.surface.blit(self.logo, self.logo_rect)

        self.waitToNewRoundTime = -1
        self.endGame = 0

    def draw(self, surface):
        self.update()
        surface.blit(self.surface, (0, 0))
        self.map.draw(self.surface)
        self.hero1.draw(self.map.surface)
        self.hero2.draw(self.map.surface)
        self.lblHero1_score = pygame.transform.scale(self.scoreBg, (200, 100))
        self.lblHero2_score = pygame.transform.scale(self.scoreBg, (200, 100))
        self.lblHero1_scoreTxt.setText("Hero 1 Score: " + str(self.hero1.score), self.lblHero1_score)
        self.lblHero2_scoreTxt.setText("Hero 2 Score: " + str(self.hero2.score), self.lblHero2_score)
        self.lblHero1_bulletTxt.setText("Bullets: " + str(self.hero1.numBullet), self.lblHero1_score)
        self.lblHero2_bulletTxt.setText("Bullets: " + str(self.hero2.numBullet), self.lblHero2_score)
        self.surface.blit(self.lblHero1_score, self.lbl1_rect)
        self.surface.blit(self.lblHero2_score, self.lbl2_rect)

    def update(self):
        if self.hero1.isDead or self.hero2.isDead:
            if self.hero1.score == cf.GAME_SCORE_TO_WIN:
                self.endGame = self.hero1.id
                return None
            if self.hero2.score == cf.GAME_SCORE_TO_WIN:
                self.endGame = self.hero2.id
                return None
            if self.waitToNewRoundTime == -1:
                self.waitToNewRoundTime = cf.GAME_WAIT_NEW_ROUND_TIME * cf.FPS
            elif self.waitToNewRoundTime > 0:
                self.waitToNewRoundTime -= 1
            elif self.waitToNewRoundTime == 0:
                self.hero1.respawn()
                self.hero2.respawn()
                self.waitToNewRoundTime = -1
        

    def receiveEvent(self, event):
        if self.hero1.isDead or self.hero2.isDead:
            return None
        self.hero1.receiveEvent(event)
        self.hero2.receiveEvent(event)
        