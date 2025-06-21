
import numpy as np

class PlantSpecies:
    def __init__(self, id, reproduction_rate, color):
        self.id = id
        self.reproduction_rate = reproduction_rate
        self.color = color

    def should_spread(self, suitability, neighbor_count):
        chance = suitability * self.reproduction_rate * neighbor_count
        return np.random.rand() < chance
