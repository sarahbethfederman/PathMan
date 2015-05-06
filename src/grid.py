# Functions for generating a grid
import random
import sys

termcolor = True

try:
    import termcolor 
except ImportError:
    termcolor = False

class Grid():
    """Represents a grid of integers, a game map"""

    def __init__(self,
                 rows=0,
                 cols=0,
                 min_val=0,
                 rand_seed=0,
                 pattern=None):
        """Constructs and generates a grid with supplied or default values
        """
        self.rows = rows
        self.cols = cols
        self.min_val = min_val
        self.max_val = 0  # Set by pattern generation
        self.rand_seed = rand_seed
        self.pattern = pattern
        self.solution = []  # Can only be assigned by generating a grid
        self.path = []  # Can only be assigned by generating a grid

    def get_valid_next(self, pos, path):
        """given a current position and path, returns a list of valid next
           positions for the path, or an empty list if there are none.
           THIS IS FOR GENERATING A PATH. DO NOT USE THIS TO CHECK PLAYER INPUT """    
        out = [] 
        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i) == abs(j):
                    pass
                elif not 0 <= pos[0] + i < self.rows:
                    pass
                elif not 0 <= pos[1] + j < self.cols:
                    pass
                elif (pos[0] + i, pos[1] + j) not in path:
                    out.append((pos[0] + i, pos[1] + j))

        return out

    def generate_grid(self):
        """Generates a grid, ensuring that there is a valid path from the
           top-left corner of the grid to the bottom right
        """
        path = [(0, 0)]  # Spaces in the correct path, in (row, column) format
        pos = (0, 0)     # Initial position for mapping

        random.seed(self.rand_seed)

        self.grid = [[0 for i in range(self.rows)] for j in range(self.cols)]
        while pos != (self.rows - 1, self.cols - 1):
            valid_next = self.get_valid_next(pos, path)
            if not valid_next:
                pos = (0, 0)
                path = [(0, 0)]
            else:
                new_pos = valid_next[random.randint(0, len(valid_next) - 1)]
                path.append(new_pos)
                pos = new_pos

        self.path = path

        # If the pattern for the current grid is defined...
        if self.pattern:
            result = []  # List to store all numbers in pattern
            self.grid[0][0] = self.min_val
            cur_val = self.min_val
            result.append(cur_val)
            for path_coord in self.path[1:]:
                next_val = self.pattern.apply_pattern(cur_val)
                self.grid[path_coord[0]][path_coord[1]] = next_val
                cur_val = next_val
                result.append(cur_val)

            self.max_val = max(result)

            for r in range(self.rows):
                for c in range(self.cols):
                    if (r, c) not in self.path:
                        num = random.randint(self.min_val, self.max_val)
                        self.grid[r][c] = num
            
            for p in self.path:
                self.solution.append(self.grid[p[0]][p[1]])

        else:
            self.grid = [[random.randint(self.min_val, 1000)
                          for i in range(self.rows)]
                         for j in range(self.cols)]

    def print_grid(self, row=None, col=None):
        """Prints the grid to stdout.  Optionally prints a number in bold"""
        global termcolor
        if self.max_val > 0:
            max_len = len(str(self.max_val))
        else:
            max_len = 4

        for r in range(self.rows):
            to_print = ""
            for c in range(self.cols):
                for i in range(max_len - len(str(self.grid[r][c])) + 1):
                    to_print = to_print + " "

                if termcolor and row == r and col == c:
                    to_print = to_print+'\033[1m'+str(self.grid[r][c])+'\033[0m'
                else:
                    to_print = to_print + str(self.grid[r][c])
            print(to_print)

    def get_tile(self, row, col):
        return self.grid[row][col]
