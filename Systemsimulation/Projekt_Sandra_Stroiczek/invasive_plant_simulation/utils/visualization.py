
import matplotlib.pyplot as plt

# Aktiviert den interaktiven Modus für Live-Updates
def plot_grid(grid, step):
    plt.imshow(grid, cmap='Greens')
    plt.title(f"Step {step}")
    plt.axis('off')
    plt.pause(0.05)
