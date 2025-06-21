
import numpy as np

# CellularAutomaton-Klasse zur Simulation eines zellulären Automaten
# Diese Klasse ermöglicht die Simulation von Zellwachstum basierend auf der Eignung des Geländes und der Nachbarschaftsbedingungen.

class CellularAutomaton:

    # Konstruktor der CellularAutomaton-Klasse
    def __init__(self, width, height):
        self.grid = np.zeros((height, width), dtype=np.int8)
    
    # Initialisiert die Zellen mit den angegebenen Koordinaten
    # Diese Methode setzt die Zellen an den angegebenen Koordinaten auf 1, um sie als besiedelt zu markieren.
    def seed(self, coords):
        for x, y in coords:
            self.grid[y, x] = 1

    # Führt einen Simulationsschritt durch, bei dem die Zellen basierend auf der Eignung des Geländes und der Nachbarschaftsbedingungen wachsen
    # Diese Methode aktualisiert das Gitter, indem sie prüft, ob Zellen wachsen können, basierend auf der Eignung des Geländes und der Anzahl der Nachbarn.
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

    # Zählt die Nachbarn einer Zelle
    def count_neighbors(self, x, y):
        return np.sum(self.grid[max(0, y-1):y+2, max(0, x-1):x+2]) - self.grid[y, x]

