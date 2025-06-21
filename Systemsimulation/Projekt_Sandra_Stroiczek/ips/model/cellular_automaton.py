import numpy as np

class CellularAutomaton:
    def __init__(self, width, height):
        self.grid = np.zeros((height, width), dtype=np.int8)

    def seed(self, species_id, coords):
        for x, y in coords:
            self.grid[y, x] = species_id

    def step(self, env, species_list):
        new_grid = self.grid.copy()
        for y in range(self.grid.shape[0]):
            for x in range(self.grid.shape[1]):
                if self.grid[y, x] == 0:  # nur leere Zellen
                    for species in species_list:
                        neighbors = self.count_neighbors(x, y, species.id)
                        if neighbors > 0:
                            suitability = env.get_suitability(x, y)
                            if species.should_spread(suitability, neighbors):
                                new_grid[y, x] = species.id
                                break  # zuerst erfolgreiche Art gewinnt
        self.grid = new_grid

    def count_neighbors(self, x, y, species_id):
        y_min = max(0, y - 1)
        y_max = min(self.grid.shape[0], y + 2)
        x_min = max(0, x - 1)
        x_max = min(self.grid.shape[1], x + 2)
        region = self.grid[y_min:y_max, x_min:x_max]
        return np.sum(region == species_id)

