
import numpy as np

# PlantSpecies-Klasse zur Darstellung verschiedener Pflanzenarten mit ihren Eigenschaften

class PlantSpecies:

    # Konstruktor der PlantSpecies-Klasse
    def __init__(self, id, reproduction_rate, color, preferred_range, competitiveness):
        self.id = id
        self.reproduction_rate = reproduction_rate
        self.color = color
        self.preferred_range = preferred_range
        self.competitiveness = competitiveness

    # Methode zur Bestimmung, ob eine Art sich ausbreiten sollte
    # basierend auf der Eignung des Geländes und der Anzahl der Nachbarn
    def should_spread(self, suitability, neighbor_count):
        min_pref, max_pref = self.preferred_range
        if not (min_pref <= suitability <= max_pref):
            return False
        chance = suitability * self.reproduction_rate * neighbor_count
        return np.random.rand() < chance
