import pygame


class Node:
    def __init__(self, row, col, width, total_rows, color):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row * width
        self.y = col * width
        self.node_type = "path"
        self.node_color = color
        self.is_start = False
        self.is_finish = False
        self.is_barrier = False
        self.is_open = False
        self.is_closed = False
    
    def change_type(self, node_type):
        if node_type in ["path", "wall", "start", "finish"]:
            self.node_type = node_type
            
            if node_type == "wall":
                self.node_color = (0, 0, 0)
                self.is_barrier = True
            
            if node_type == "start":
                self.node_color = (255, 165, 0)
                self.is_start = True
            
            if node_type == "finish":
                self.node_color = (255, 255, 255)
                self.is_finish = True
            
            if node_type == "path":
                self.node_color = (128, 128, 128)
        # throw exception or something like that.
    
    def close_node(self):
        self.node_color = (255, 0, 0)
        self.is_closed = True
    
    def open_node(self):
        self.node_color = (0, 255, 0)
        self.is_open = True
    
    def draw_node(self, win):
        pygame.draw.rect(win, self.node_color, (self.x, self.y, self.width, self.width))

