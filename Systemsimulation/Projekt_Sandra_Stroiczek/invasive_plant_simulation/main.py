
from model.environment import Environment
from model.cellular_automaton import CellularAutomaton
from model.species import InvasiveSpecies
from utils.visualization import plot_grid

# Vier invasive Pflanzen verbreiten sich in einem Ökosystem
# mit unterschiedlichen Wachstumsbedingungen und Konkurrenzverhalten.
def run_simulation():
    env = Environment("data/terrain.png")
    ca = CellularAutomaton(100, 100)
    species = InvasiveSpecies()

    ca.seed([(50, 50)])  # Initiale Pflanzenstandorte
    
    for step in range(100):
        ca.step(env, species)
        plot_grid(ca.grid, step)

if __name__ == "__main__":
    run_simulation()
