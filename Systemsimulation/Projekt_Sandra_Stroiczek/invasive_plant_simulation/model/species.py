import numpy as np

# InvasiveSpecies-Klasse zur Darstellung invasiver Pflanzenarten mit spezifischen Eigenschaften

class InvasiveSpecies:

    # Konstruktor der InvasiveSpecies-Klasse
    def __init__(self, reproduction_rate=0.4):
        self.reproduction_rate = reproduction_rate
    
    # Methode zur Bestimmung, ob die Art sich ausbreiten sollte
    def should_spread(self, suitability, neighbors):
        base_chance = suitability * self.reproduction_rate
        return neighbors > 0 and np.random.rand() < base_chance


