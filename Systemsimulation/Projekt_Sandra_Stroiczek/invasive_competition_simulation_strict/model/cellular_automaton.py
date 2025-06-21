
import numpy as np
import random

# CellularAutomaton-Klasse zur Simulation von Zellulären Automaten
class CellularAutomaton:

    # Konstruktor der CellularAutomaton-Klasse
    def __init__(self, width, height):
        self.grid = np.zeros((height, width), dtype=int)

    # Initialisiert die Zellen mit Arten-IDs an den angegebenen Positionen
    def seed(self, species_id, positions):
        for x, y in positions:
            self.grid[y, x] = species_id

    # Führt einen Simulationsschritt durch, bei dem Arten basierend auf lokaler Eignung und Wettbewerbsfähigkeit wachsen
    def step(self, environment, species_list):
        new_grid = self.grid.copy()
        height, width = self.grid.shape

        for y in range(height):
            for x in range(width):
                current_species = self.grid[y, x]

                # Skip if already occupied
                if current_species != 0:
                    continue

                neighbor_species = {}
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < width and 0 <= ny < height:
                            neighbor_id = self.grid[ny, nx]
                            if neighbor_id != 0:
                                neighbor_species[neighbor_id] = neighbor_species.get(neighbor_id, 0) + 1

                if not neighbor_species:
                    continue

                suitability = environment.get_suitability(x, y)
                best_score = -1
                selected_species = 0

                for species_id, count in neighbor_species.items():
                    species = next(s for s in species_list if s.id == species_id)
                    min_suit, max_suit = species.preferred_suitability_range

                    if not (min_suit <= suitability <= max_suit):
                        continue

                    score = (species.reproduction_rate * count * species.competitiveness)
                    if score > best_score:
                        best_score = score
                        selected_species = species_id

                if selected_species != 0:
                    new_grid[y, x] = selected_species

        self.grid = new_grid
