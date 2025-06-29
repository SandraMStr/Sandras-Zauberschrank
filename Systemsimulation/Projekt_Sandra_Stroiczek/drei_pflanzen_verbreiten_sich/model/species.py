
import numpy as np

# Represents a plant species with its properties and behavior in the cellular automaton 
class PlantSpecies:
    def __init__(self, id, reproduction_rate, color, preferred_range, competitiveness):
        self.id = id
        self.reproduction_rate = reproduction_rate
        self.color = color
        self.preferred_range = preferred_range  # Tuple: (min, max) suitability
        self.competitiveness = competitiveness  # Float: Stärke im Wettbewerb

    def should_spread(self, suitability, neighbor_count):
        min_pref, max_pref = self.preferred_range
        if not (min_pref <= suitability <= max_pref):
            return False
        chance = suitability * self.reproduction_rate * neighbor_count
        return np.random.rand() < chance
