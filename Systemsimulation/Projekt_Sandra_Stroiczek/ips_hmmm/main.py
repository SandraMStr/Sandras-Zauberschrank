
from model.environment import Environment
from model.cellular_automaton import CellularAutomaton
from model.species import PlantSpecies
from utils.visualization import plot_grid
import time

def run_simulation():
    env = Environment("data/terrain.png")
    ca = CellularAutomaton(env.width, env.height)

    species_list = [
        PlantSpecies(1, 0.4, (0, 255, 0), (0.2, 1.0), 0.6),
        PlantSpecies(2, 0.3, (255, 0, 0), (0.0, 0.6), 0.8),
        PlantSpecies(3, 0.2, (0, 0, 255), (0.3, 0.9), 0.4),
        PlantSpecies(4, 0.5, (255, 255, 0), (0.1, 0.8), 0.7),
    ]

    ca.seed(1, [(10, 10)])
    ca.seed(2, [(80, 20)])
    ca.seed(3, [(30, 80)])
    ca.seed(4, [(70, 70)])

    for step in range(150):
        ca.step(env, species_list)
        plot_grid(ca.grid, species_list, step)
        time.sleep(0.1)

if __name__ == "__main__":
    run_simulation()
