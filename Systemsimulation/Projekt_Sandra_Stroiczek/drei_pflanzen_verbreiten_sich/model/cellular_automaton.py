
import numpy as np

class CellularAutomaton:
    def __init__(self, width, height):
        self.grid = np.zeros((height, width), dtype=np.int8)

    def seed(self, species_id, coords):
        for x, y in coords:
            self.grid[y, x] = species_id

    # Steps the cellular automaton forward by one time step
    # Each species tries to spread based on its competitiveness and local suitability
    # If a species has more neighbors than its competitiveness allows, it will not spread
    # If a neighboring species has higher competitiveness, it will replace the current species
    # If the cell is empty, it will be filled with the most competitive species that can spread there
    # The suitability of the environment is taken into account for each cell
    # The species with the highest competitiveness that can spread will take over the cell
    # If multiple species have the same competitiveness, the first one in the list will take over
    # The grid is updated in a new grid to avoid conflicts during the step
    # The method assumes that species_list is a list of PlantSpecies objects
    def step(self, env, species_list):
        new_grid = self.grid.copy()
        height, width = self.grid.shape

        for y in range(height):
            for x in range(width):
                current_species_id = self.grid[y, x]
                local_suitability = env.get_suitability(x, y)

                candidates = []
                for species in species_list:
                    neighbors = self.count_neighbors(x, y, species.id)
                    if neighbors > 0 and species.should_spread(local_suitability, neighbors):
                        candidates.append((species.competitiveness, species.id))

                if candidates:
                    candidates.sort(reverse=True)  # stärkste zuerst
                    top_competitiveness, top_species_id = candidates[0]

                    # Nur ersetzen, wenn Feld leer ist oder schwächere Art verdrängt wird
                    if current_species_id == 0:
                        new_grid[y, x] = top_species_id
                    elif current_species_id != top_species_id:
                        current_species = next((s for s in species_list if s.id == current_species_id), None)
                        if current_species and top_competitiveness > current_species.competitiveness:
                            new_grid[y, x] = top_species_id

        self.grid = new_grid

    def count_neighbors(self, x, y, species_id):
        y_min = max(0, y - 1)
        y_max = min(self.grid.shape[0], y + 2)
        x_min = max(0, x - 1)
        x_max = min(self.grid.shape[1], x + 2)
        region = self.grid[y_min:y_max, x_min:x_max]
        return np.sum(region == species_id)
