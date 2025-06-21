
import matplotlib.pyplot as plt
import numpy as np

def plot_grid(grid, species_list, step):
    color_map = {0: (1, 1, 1)}
    for species in species_list:
        color_map[species.id] = tuple(np.array(species.color) / 255)

    rgb_grid = np.zeros(grid.shape + (3,))
    for species_id, color in color_map.items():
        mask = grid == species_id
        rgb_grid[mask] = color

    plt.figure(figsize=(6, 6))
    plt.imshow(rgb_grid)
    plt.title(f"Step {step}")
    plt.axis("off")
    plt.pause(0.01)
    plt.clf()
