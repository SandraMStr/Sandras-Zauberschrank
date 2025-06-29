
from PIL import Image
import numpy as np

# Environment class that represents the terrain and its suitability for plant species
class Environment:
    def __init__(self, image_path):
        img = Image.open(image_path).convert("L")
        self.terrain = np.array(img)
        self.height, self.width = self.terrain.shape

    # Returns the suitability of a cell at (x, y)
    def get_suitability(self, x, y):
        return self.terrain[y, x] / 255.0
