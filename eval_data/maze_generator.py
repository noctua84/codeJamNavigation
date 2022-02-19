import numpy as np


def carve_maze(carve_grid, carve_size):
    output_grid = np.empty([carve_size * 3, carve_size * 3], dtype=int)
    output_grid[:] = 1
    
    i = 0
    j = 0
    
    while i < carve_size:
        w = i * 3 + 1
        
        while j < carve_size:
            k = j * 3 + 1
            
            toss = carve_grid[i, j]
            output_grid[w, k] = 0
            
            if toss == 0 and k + 2 < carve_size * 3:
                output_grid[w, k + 1] = 0
                output_grid[w, k + 2] = 0
            
            if toss == 1 and w - 2 >= 0:
                output_grid[w - 1, k] = 0
                output_grid[w - 2, k] = 0
            
            j = j + 1
        
        i = i + 1
        j = 0
    
    return output_grid
