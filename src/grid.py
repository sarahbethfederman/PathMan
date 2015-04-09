# Functions for generating a grid
import random
import sys
import pattern

class Grid():
    def __init__(self,
                 rows = 0,
                 cols = 0,
                 min_val = 0,
                 max_val = 0,
                 rand_seed = 0,
                 pattern = 0):
        self.rows = rows
        self.cols = cols
        self.min_val = min_val
        self.max_val = max_val
        self.rand_seed = rand_seed
        self.pattern = pattern

        random.seed(self.rand_seed)
        self.grid = [[random.randint(self.min_val, self.max_val) 
                      for i in range(self.rows)] 
                      for j in range(self.cols)]
        

    def print_grid(self):
        for r in range(self.rows):
            print(self.grid[r])
    
