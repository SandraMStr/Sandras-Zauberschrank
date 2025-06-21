
from PIL import Image
import numpy as np

class Environment:
    def __init__(self, image_path):
        img = Image.open(image_path).convert("L")
        self.terrain = np.array(img)
        self.height, self.width = self.terrain.shape

    def get_suitability(self, x, y):
        return self.terrain[y, x] / 255.0
