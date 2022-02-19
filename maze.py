import numpy as np
from numpy import random

from node import Node


def distance(node_a, node_b):
    dist = 0
    for x_i, y_i in zip(node_a, node_b):
        dist += abs(x_i + y_i)
    
    return dist


class Maze:
    def __init__(self, n_distribution: int, p_distribution: float, size: int):
        self.n_distribution = n_distribution
        if 0 < p_distribution < 1:
            self.p_distribution = p_distribution
        else:
            raise ValueError("p_distribution has to be between 0 and 1")
        self.size = size
        self.__grid = self.__generate_grid()
        self.list_of_nodes = []
        self.maze = []
        self.shape = []
        self.maze_start = None
        self.maze_end = None
    
    def __generate_grid(self):
        grid = np.random.binomial(self.n_distribution, self.p_distribution, size=(self.size, self.size))
        
        first_row = grid[0]
        first_row[first_row == 1] = 0
        
        grid[0] = first_row
        
        for i in range(1, self.size):
            grid[i, self.size - 1] = 1
        
        return grid
    
    def __carve_maze(self, grid):
        output_grid = np.empty([self.size * 3, self.size * 3], dtype=int)
        output_grid[:] = 1
        
        i = 0
        j = 0
        
        while i < self.size:
            w = i * 3 + 1
            
            while j < self.size:
                k = j * 3 + 1
                
                toss = grid[i, j]
                output_grid[w, k] = 0
                
                if toss == 0 and k + 2 < self.size * 3:
                    output_grid[w, k + 1] = 0
                    output_grid[w, k + 2] = 0
                
                if toss == 1 and w - 2 >= 0:
                    output_grid[w - 1, k] = 0
                    output_grid[w - 2, k] = 0
                
                j = j + 1
            
            i = i + 1
            j = 0
        
        self.shape = output_grid.shape
        
        return output_grid
    
    def __create_node_grid(self, window_width: int, maze):
        node_grid = []
        gap = window_width // maze.shape[0] + 1
        id_span = 1
        
        for row in range(maze.shape[0]):
            node_grid.append([])
            for col in range(maze.shape[1]):
                node = Node(row, col, gap, maze.shape[0], (160, 160, 160), id_span)
                
                if maze[row, col] == 1:
                    node.change_type("wall")
                else:
                    self.list_of_nodes.append(node)
                
                node_grid[row].append(node)
                id_span += 1
        
        return node_grid
    
    def create_maze(self, width: int):
        blank_maze = self.__carve_maze(self.__grid)
        self.maze = self.__create_node_grid(width, blank_maze)
    
    def set_start_and_end(self):
        self.maze_start = self.list_of_nodes[random.randint(0, len(self.list_of_nodes))]
        print(self.maze_start.node_id)
        self.maze_start.change_type("start")
        
        self.maze_end = self.list_of_nodes[random.randint(0, len(self.list_of_nodes))]
        print(self.maze_end.node_id)
        self.maze_end.change_type("finish")
    
    # def __get_end_node(self, start):
    #    end = self.list_of_nodes[random.randint(0, len(self.list_of_nodes))]
    #    dist = distance((start.row, start.col), (end.row, end.col))
    #    print(dist)
    #    if end.node_id != start.node_id and dist > 60:
    #        print(end.node_id)
    #        print(type(end))
    #        return end
    #    else:
    #        self.__get_end_node(start)

