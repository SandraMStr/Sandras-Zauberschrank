
import matplotlib.pyplot as plt
import numpy as np

# Aktiviert den interaktiven Modus für Live-Updates
def plot_grid(grid, species_list, step):
    color_map = np.zeros((*grid.shape, 3), dtype=np.uint8)
    for species in species_list:
        mask = grid == species.id
        color_map[mask] = species.color

    plt.imshow(color_map)
    plt.title(f"Step {step}")
    plt.axis('off')
    plt.pause(0.01)
    plt.clf()
