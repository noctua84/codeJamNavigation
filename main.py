import sys

import pygame
from pygame.locals import KEYDOWN, K_q

import numpy as np
import maze_generator

# constants:
from node import Node

ROWS = 10
BLACK = (0, 0, 0)
GREY = (160, 160, 160)


# main loop:
def main(window_width, initial_maze):
    pygame.init()
    window = pygame.display.set_mode((window_width, window_width))
    
    while True:
        check_events()
        window.fill(GREY)
        cur_grid = make_maze_elements(window_width, initial_maze)
        
        for row in cur_grid:
            for node in row:
                node.draw_node(window)
        
        draw_grid_lines(window, window_width, initial_maze)
        pygame.display.update()


# event checker: keyboard-key q for quitting the app
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


# populate the grid with nodes to be used by the traversal algorithm
def make_maze_elements(element_width, maze):
    grid = []
    gap = element_width // maze.shape[0] + 1
    for row in range(maze.shape[0]):
        grid.append([])
        for col in range(maze.shape[1]):
            node = Node(row, col, gap, maze.shape[0], GREY)
            if maze[row, col] == 1:
                node.change_type("wall")
            
            grid[row].append(node)
    
    return grid


# outline the grid elements:
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
    maze_map = np.random.binomial(1, 0.5, (ROWS, ROWS))
    first_row = maze_map[0]
    first_row[first_row == 1] = 0
    
    maze_map[0] = first_row
    
    for i in range(1, ROWS):
        maze_map[i, ROWS - 1] = 1
    
    generated_maze = maze_generator.carve_maze(maze_map, ROWS)
    
    main(width, generated_maze)
