from model.environment import Environment
from model.cellular_automaton import CellularAutomaton
from model.species import PlantSpecies
from utils.visualization import plot_grid
import time

def run_simulation():
    env = Environment("data/terrain.png")
    ca = CellularAutomaton(env.width, env.height)

    species_list = [
        PlantSpecies(1, 0.4, (0, 255, 0)),    # grün
        PlantSpecies(2, 0.3, (255, 0, 0)),    # rot
        PlantSpecies(3, 0.2, (0, 0, 255)),    # blau
        PlantSpecies(4, 0.5, (255, 255, 0)),  # gelb
    ]

    # Anfangspunkte pro Art
    ca.seed(1, [(10, 10)])
    ca.seed(2, [(80, 20)])
    ca.seed(3, [(30, 80)])
    ca.seed(4, [(70, 70)])

    for step in range(80):
        ca.step(env, species_list)
        plot_grid(ca.grid, species_list, step)
        time.sleep(0.1)

if __name__ == "__main__":
    run_simulation()

