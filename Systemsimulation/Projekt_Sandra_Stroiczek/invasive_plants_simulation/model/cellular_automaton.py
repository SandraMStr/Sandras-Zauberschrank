
import numpy as np

class CellularAutomaton:
    def __init__(self, width, height):
        self.grid = np.zeros((height, width), dtype=np.int8)
    
    def seed(self, coords):
        for x, y in coords:
            self.grid[y, x] = 1

    def step(self, env, species):
        new_grid = self.grid.copy()
        for y in range(self.grid.shape[0]):
            for x in range(self.grid.shape[1]):
                if self.grid[y, x] == 0:
                    neighbors = self.count_neighbors(x, y)
                    suitability = env.get_suitability(x, y)
                    if species.should_spread(suitability, neighbors):
                        new_grid[y, x] = 1
        self.grid = new_grid

    def count_neighbors(self, x, y):
        return np.sum(self.grid[max(0, y-1):y+2, max(0, x-1):x+2]) - self.grid[y, x]

