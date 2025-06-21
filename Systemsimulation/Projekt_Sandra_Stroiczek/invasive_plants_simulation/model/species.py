import numpy as np

class InvasiveSpecies:
    def __init__(self, reproduction_rate=0.4):
        self.reproduction_rate = reproduction_rate
    
    def should_spread(self, suitability, neighbors):
        base_chance = suitability * self.reproduction_rate
        return neighbors > 0 and np.random.rand() < base_chance


