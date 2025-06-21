
# Diese Datei ist Teil des Invasive Competition Simulation Strict-Projekts.

class PlantSpecies:

    # PlantSpecies-Klasse zur Darstellung verschiedener Pflanzenarten mit ihren Eigenschaften
    def __init__(self, id, reproduction_rate, color, preferred_suitability_range, competitiveness):
        self.id = id
        self.reproduction_rate = reproduction_rate
        self.color = color
        self.preferred_suitability_range = preferred_suitability_range
        self.competitiveness = competitiveness
