
# terrain_gen.py
from PIL import Image
import numpy as np
import os

terrain = np.random.randint(80, 255, (100, 100), dtype=np.uint8)
os.makedirs("data", exist_ok=True)
Image.fromarray(terrain).save("data/terrain.png")
