import sys
import pygame
from pygame.locals import KEYDOWN, K_q
import numpy as np

# CONSTANTS:
SCREENSIZE = WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
GREY = (160, 160, 160)

# OUR GRID MAP:
cellMAP = np.random.randint(2, size=(10, 10))

# print(cellMAP)
# [[1 0 1 0 0 0 1 0 1 0]
#  [0 0 0 1 0 0 0 1 1 0]
#  [0 0 1 1 0 0 1 1 1 0]
#  [0 0 1 0 0 0 1 0 0 1]
#  [0 1 1 0 0 0 0 1 1 0]
#  [0 1 0 0 1 0 0 1 1 1]
#  [0 1 0 0 1 1 1 1 0 1]
#  [1 0 1 0 1 1 1 1 0 1]
#  [0 1 0 1 0 0 0 1 0 0]
#  [0 1 1 1 0 1 1 0 0 1]]

_VARS = {'surf': False, 'gridWH': 400,
         'gridOrigin': (200, 100), 'gridCells': cellMAP.shape[0], 'lineWidth': 2}


def main():
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    while True:
        checkEvents()
        _VARS['surf'].fill(GREY)
        drawSquareGrid(
            _VARS,
        )
        placeCells(_VARS, cellMAP)
        pygame.display.update()


# NEW METHOD FOR ADDING CELLS :
def placeCells(VARS, cellMap, colourCodes=None):
    # GET CELL DIMENSIONS...
    if colourCodes is None:
        colourCodes = {1: BLACK}
    cellBorder = 6
    celldimX = celldimY = (VARS['gridWH']/VARS['gridCells']) - (cellBorder*2)
    # DOUBLE LOOP
    for row in range(cellMap.shape[0]):
        for column in range(cellMap.shape[1]):
            # Is the grid cell tiled ?
            if(cellMap[column][row] != 0):
                drawSquareCell(
                    VARS['surf'],
                    VARS['gridOrigin'][0] + (celldimY*row)
                    + cellBorder + (2*row*cellBorder) + VARS['lineWidth']/2,
                    VARS['gridOrigin'][1] + (celldimX*column)
                    + cellBorder + (2*column*cellBorder) + VARS['lineWidth']/2,
                    celldimX, celldimY, colourCodes[cellMap[column][row]])


# Draw filled rectangle at coordinates
def drawSquareCell(surf, x, y, dimX, dimY, colour):
    pygame.draw.rect(
     surf, colour,
     (x, y, dimX, dimY)
    )


def drawSquareGrid(VARS):

    origin, gridWH, cells, surf = VARS['gridOrigin'], VARS['gridWH'], VARS['gridCells'], VARS['surf']

    CONTAINER_WIDTH_HEIGHT = gridWH
    cont_x, cont_y = origin

    # DRAW Grid Border:
    # TOP lEFT TO RIGHT
    pygame.draw.line(
      surf, BLACK,
      (cont_x, cont_y),
      (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y), VARS['lineWidth'])
    # # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
      surf, BLACK,
      (cont_x, CONTAINER_WIDTH_HEIGHT + cont_y),
      (CONTAINER_WIDTH_HEIGHT + cont_x,
       CONTAINER_WIDTH_HEIGHT + cont_y), VARS['lineWidth'])
    # # LEFT TOP TO BOTTOM
    pygame.draw.line(
      surf, BLACK,
      (cont_x, cont_y),
      (cont_x, cont_y + CONTAINER_WIDTH_HEIGHT), VARS['lineWidth'])
    # # RIGHT TOP TO BOTTOM
    pygame.draw.line(
      surf, BLACK,
      (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y),
      (CONTAINER_WIDTH_HEIGHT + cont_x,
       CONTAINER_WIDTH_HEIGHT + cont_y), VARS['lineWidth'])

    # Get cell size, just one since its a square grid.
    cellSize = CONTAINER_WIDTH_HEIGHT/cells

    # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
    for x in range(cells):
        pygame.draw.line(
           surf, BLACK,
           (cont_x + (cellSize * x), cont_y),
           (cont_x + (cellSize * x), CONTAINER_WIDTH_HEIGHT + cont_y), 2)
    # # HORIZONTAl DIVISIONS
        pygame.draw.line(
          surf, BLACK,
          (cont_x, cont_y + (cellSize*x)),
          (cont_x + CONTAINER_WIDTH_HEIGHT, cont_y + (cellSize*x)), 2)


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()



