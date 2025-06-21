
from PIL import Image
import numpy as np

class Environment:
    def __init__(self, image_path):
        img = Image.open(image_path).convert("L")
        self.terrain = np.array(img) / 255.0
        self.width = self.terrain.shape[1]
        self.height = self.terrain.shape[0]

    def get_suitability(self, x, y):
        return self.terrain[y, x]
