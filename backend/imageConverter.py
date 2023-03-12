import pygame
import numpy as np
from PIL import ImageColor

import backend.pygameReadMapToGrid as rmg

SCREENSIZE = WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
GREY = (160, 160, 160)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

COLOURS = {1: RED, 2: BLUE, 3: GREEN}


def displayImage(pixels: list[list[int]], colourCodes: dict):
    pixelsMAP = np.array(pixels, dtype=int)
    _VARS = {
        'surf': False, 'gridWH': 400,
        'gridOrigin': (200, 100), 'gridCells': pixelsMAP.shape[0],
        'lineWidth': 2
    }
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    while True:
        rmg.checkEvents()
        _VARS['surf'].fill(GREY)
        rmg.drawSquareGrid(_VARS)
        rmg.placeCells(_VARS, pixelsMAP, colourCodes)
        pygame.display.update()


def hexToCol(hexcodes: dict):
    for k in hexcodes:
        hexcodes[k] = ImageColor.getcolor(hexcodes[k], "RGB")
    return hexcodes
