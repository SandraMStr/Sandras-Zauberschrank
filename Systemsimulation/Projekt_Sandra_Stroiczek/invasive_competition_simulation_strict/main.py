
from model.environment import Environment
from model.species import PlantSpecies
from model.cellular_automaton import CellularAutomaton
from utils.visualization import plot_grid
import time

# Vier Pflanzen verbreiten sich in einem Ökosystem
# mit unterschiedlichen Wachstumsbedingungen und Konkurrenzverhalten.
def run_simulation():
    env = Environment("data/terrain.png")
    ca = CellularAutomaton(env.width, env.height)

    species_list = [
        # Staudenknöterich (Grün)
        PlantSpecies(1, 0.7, (0, 150, 0), (0.3, 0.9), 0.85),
        # Riesenbärenklau (Rot)
        PlantSpecies(2, 0.6, (255, 0, 0), (0.5, 1.0), 0.95),
        # Springkraut (Blau)
        PlantSpecies(3, 0.9, (0, 0, 255), (0.2, 0.8), 0.5),
        # Kudzu (Gelb)
        PlantSpecies(4, 0.85, (200, 200, 0), (0.4, 1.0), 0.7)
    ]

    ca.seed(1, [(10, 10)])
    ca.seed(2, [(90, 10)])
    ca.seed(3, [(10, 90)])
    ca.seed(4, [(90, 90)])

    for step in range(150):
        ca.step(env, species_list)
        plot_grid(ca.grid, species_list, step)
        time.sleep(0.05)

if __name__ == "__main__":
    run_simulation()
