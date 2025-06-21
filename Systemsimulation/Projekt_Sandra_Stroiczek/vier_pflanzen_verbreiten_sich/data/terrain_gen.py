
# terrain_gen.py
from PIL import Image
import numpy as np
import os

terrain = np.full((100, 100), 180, dtype=np.uint8)

# Simulierter Fluss
for x in range(100):
    y = int(50 + 8 * np.sin(x / 7))
    terrain[max(0, y - 2):min(100, y + 3), x] = 30

# Felsen
for _ in range(10):
    cx, cy = np.random.randint(0, 100, size=2)
    rr = np.random.randint(2, 5)
    for y in range(cy - rr, cy + rr):
        for x in range(cx - rr, cx + rr):
            if 0 <= x < 100 and 0 <= y < 100:
                terrain[y, x] = 60

# Hochfruchtbare Bereiche
for _ in range(5):
    cx, cy = np.random.randint(0, 100, size=2)
    rr = np.random.randint(3, 6)
    for y in range(cy - rr, cy + rr):
        for x in range(cx - rr, cx + rr):
            if 0 <= x < 100 and 0 <= y < 100:
                terrain[y, x] = 240

os.makedirs("data", exist_ok=True)
Image.fromarray(terrain).save("data/terrain.png")
