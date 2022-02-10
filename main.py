import sys
from typing import Union

import pygame
from pygame import Surface, SurfaceType
from pygame.locals import KEYDOWN, K_q

import numpy as np

# constants:
WIDTH = 800
ROWS = 50
BLACK = (0, 0, 0)
GREY = (160, 160, 160)

# global vars:
_VARS = {
    'surf': Union[Surface, SurfaceType]
}

MAP = np.zeros((ROWS, ROWS), dtype=int)
cellMAP = np.random.randint(2, size=(ROWS, ROWS))
print(cellMAP)


# main loop:
def main():
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode((WIDTH, WIDTH))
    
    while True:
        check_events()
        _VARS['surf'].fill(GREY)
        draw_grid(_VARS["surf"])
        pygame.display.update()


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


def draw_grid(win):
    gap = WIDTH // ROWS
    for row in range(cellMAP.shape[0]):
        pygame.draw.line(win, BLACK, (0, row * gap), (WIDTH, row * gap))
        for col in range(cellMAP.shape[1]):
            pygame.draw.line(win, BLACK, (col * gap, 0), (col * gap, WIDTH))


if __name__ == '__main__':
    main()