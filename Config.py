import pygame, sys
from pygame.locals import *
import math
from Util import *

# Resolution
WIDTH = 1200
HEIGHT = 720
# WIDTH = 960 
# HEIGHT = 480

# Color
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 110, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLLOW = (255, 204, 0)
TRANSPARENT = (0, 0, 0, 0)

# FPS
FPS = 60


# Game Command
CMD_QUIT = 0
CMD_MAP_1 = 1
CMD_MAP_2 = 2
CMD_MAP_3 = 3

GAME_LOGO = pygame.Surface((200, 100), SRCALPHA)
GAME_STAR = pygame.image.load("res/star.png")
gStar_rect = GAME_STAR.get_rect()
gStar_rect.center = (100, 35)
GAME_LOGO.blit(GAME_STAR, gStar_rect)
pygame.font.init()
gName_font = pygame.font.SysFont('comicsansms', 15, True, False)
GAME_NAME = gName_font.render("ROYALE BATTLE", True, YELLLOW)
gName_rect = GAME_NAME.get_rect()
gName_rect.center = (100, 75)
GAME_LOGO.blit(GAME_NAME, gName_rect)

# Game config
GAME_WAIT_NEW_ROUND_TIME = 3
GAME_SCORE_TO_WIN = 5


# Map
MAP_1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 8, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 6, 0, 0, 1],
[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 2, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

BLOCK_SIZE = BLOCK_WIDTH = BLOCK_HEIGHT = 30

MAP_1_ID = 0
MAP_2_ID = 1
MAP_3_ID = 2

NO_COLLISION = 0
COLLISON_X = 1
COLLISON_Y = 2
COLLISON_BOTH = 3

ITEM_BULLET_ID = 4
ITEM_SPEED_ID = 5

# Hero
HERO_SIZE = HERO_WIDTH = HERO_HEIGHT = 30
HERO_1_ID = 8
HERO_2_ID = 9

# keyName
K_ATTACK = "kAttack"
K_UP_DIRECTION = "kUpDirection"
K_DOWN_DIRECTION = "kDownDirection"

HERO_KEY = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
HERO_KEY[HERO_1_ID] = {
    "kUp": K_w,
    "kDown": K_s,
    "kLeft": K_a,
    "kRight": K_d,
    K_ATTACK: K_SPACE,
    K_UP_DIRECTION: K_q,
    K_DOWN_DIRECTION: K_e,
}

HERO_KEY[HERO_2_ID] = {
    "kUp": K_UP,
    "kDown": K_DOWN,
    "kLeft": K_LEFT,
    "kRight": K_RIGHT,
    K_ATTACK: K_PERIOD,
    K_UP_DIRECTION: K_COMMA,
    K_DOWN_DIRECTION: K_SLASH,
}



# Bullet
BULLET_SIZE = BULLET_WIDTH = BULLET_HEIGHT = 130
BULLET_SPEED = 1000      #   100pixel/s
BULLET_TIME_TO_DIE = 1
HERO_BASE_SPEED_PX_PER_FR = 2 #pixel per frame
NUM_SPEED_PER_ITEM = 0.5
HERO_MAX_SPEED_PX_PER_FR = 4

UP_DIRECTION_STATE = 0
DOWN_DIRECTION_STATE = 1
DIRECTION_SPEED = 2
DEGREE_TO_RADIAN = math.pi / 180

FORWARD_DIRECTION = Point(0, -1)
DETECT_SLICE = 10

NUM_BULLET_PER_ITEM = 10
INIT_NUM_BULLET = 2*NUM_BULLET_PER_ITEM
