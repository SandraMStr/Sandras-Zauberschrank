
from model.environment import Environment
from model.species import PlantSpecies
from model.cellular_automaton import CellularAutomaton
from utils.visualization import plot_grid
import time

def run_simulation():
    env = Environment("data/terrain.png")
    ca = CellularAutomaton(env.width, env.height)

    species_list = [
        PlantSpecies(1, 0.6, (0, 150, 0), (0.1, 0.8), 0.8),  # Staudenknöterich – uferliebend
        PlantSpecies(2, 0.4, (255, 0, 0), (0.6, 1.0), 0.9),  # Riesenbärenklau – trockenliebend
        PlantSpecies(3, 0.5, (0, 0, 255), (0.2, 0.7), 0.6),  # Springkraut – feuchtliebend
        PlantSpecies(4, 0.7, (200, 200, 0), (0.4, 1.0), 0.5) # Kudzu – meidet Wasser
    ]

    ca.seed(1, [(10, 10)])
    ca.seed(2, [(80, 10)])
    ca.seed(3, [(10, 80)])
    ca.seed(4, [(80, 80)])

    for step in range(100):
        ca.step(env, species_list)
        plot_grid(ca.grid, species_list, step)
        time.sleep(0.1)

if __name__ == "__main__":
    run_simulation()
