
import matplotlib.pyplot as plt
import numpy as np

plt.ion()

# Function to plot the grid of the cellular automaton
def plot_grid(grid, species_list, step):
    height, width = grid.shape
    rgb_image = np.zeros((height, width, 3), dtype=np.uint8)

    for species in species_list:
        mask = grid == species.id
        rgb_image[mask] = species.color

    plt.clf()
    plt.imshow(rgb_image)
    plt.title(f"Step {step}")
    plt.axis('off')
    plt.draw()
    plt.pause(0.01)
