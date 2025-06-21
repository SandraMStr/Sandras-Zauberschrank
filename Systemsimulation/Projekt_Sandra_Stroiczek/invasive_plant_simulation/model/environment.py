
from PIL import Image
import numpy as np

# Umweltklasse zur Darstellung des Geländes und seiner Eignung für das Artenwachstum

class Environment:

    # Initialisiert die Umgebung mit einem Bild, das die Eignung des Geländes darstellt
    def __init__(self, image_path):
        img = Image.open(image_path).convert("L")
        self.terrain = np.array(img)
    
    # Gibt die Eignung eines bestimmten Punktes (x, y) zurück
    # Normalisiert die Eignung auf den Bereich [0, 1], wobei 0 Wasser und 1 sehr fruchtbar ist
    def get_suitability(self, x, y):
        val = self.terrain[y, x]
        # 0-255 → 0 (Wasser) bis 1 (sehr fruchtbar)
        return val / 255.0

