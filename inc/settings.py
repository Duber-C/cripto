import pygame as pg
import os

# directorios
path = os.path.dirname(__file__)
spritesheet_path = os.path.join(path ,"img")

# colores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
L_BLUE = (100, 100, 255)
D_BLUE = (220, 220, 255)
GRAY = (50, 50, 50)

# opciones de configuracion
WIDTH = 600
HEIGHT = 400
TITLE = "cripto"
FPS = 60
FONT_NAME = 'segoe'
BGCOLOR = GRAY
TEXT_COLOR = BLACK
COLOR_ACTIVE = GREEN
COLOR_INACTIVE = WHITE

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
