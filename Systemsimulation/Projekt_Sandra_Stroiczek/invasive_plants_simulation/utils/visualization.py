
import matplotlib.pyplot as plt

def plot_grid(grid, step):
    plt.imshow(grid, cmap='Greens')
    plt.title(f"Step {step}")
    plt.axis('off')
    plt.pause(0.1)
