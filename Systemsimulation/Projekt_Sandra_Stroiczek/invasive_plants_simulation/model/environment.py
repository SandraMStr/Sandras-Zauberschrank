
from PIL import Image
import numpy as np

class Environment:
    def __init__(self, image_path):
        img = Image.open(image_path).convert("L")
        self.terrain = np.array(img)
    
    def get_suitability(self, x, y):
        val = self.terrain[y, x]
        # 0-255 → 0 (Wasser) bis 1 (sehr fruchtbar)
        return val / 255.0

