import sys

import pygame
from pygame.locals import KEYDOWN, K_q

from maze import Maze

ROWS = 10
BLACK = (0, 0, 0)
GREY = (160, 160, 160)


# main loop:
def main(window_width, maze: Maze):
    pygame.init()
    window = pygame.display.set_mode((window_width, window_width))
    
    while True:
        check_events()
        window.fill(GREY)
        cur_grid = maze.maze
        
        for row in cur_grid:
            for node in row:
                node.draw_node(window)
        
        draw_grid_lines(window, window_width, maze)
        pygame.display.update()


# event checker: keyboard-key q for quitting the app
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


# outline the __grid elements:
def draw_grid_lines(win, element_width, maze):
    gap = element_width // maze.shape[0] + 1
    for row in range(maze.shape[0]):
        pygame.draw.line(win, BLACK, (0, row * gap), (element_width, row * gap))
        for col in range(maze.shape[1]):
            pygame.draw.line(win, BLACK, (col * gap, 0), (col * gap, element_width))


if __name__ == '__main__':
    # params:
    width = 800
    
    # prepare maze
    cur_maze = Maze(1, 0.5, ROWS)
    cur_maze.create_maze(width)
    cur_maze.set_start_and_end()
    
    main(width, cur_maze)
