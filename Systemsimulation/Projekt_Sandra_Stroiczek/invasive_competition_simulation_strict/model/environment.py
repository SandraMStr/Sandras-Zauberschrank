
from PIL import Image
import numpy as np

# Umweltklasse zur Darstellung des Geländes und seiner Eignung für das Artenwachstum

class Environment:

    # Initialisiert die Umgebung mit einem Bild, das die Eignung des Geländes darstellt
    def __init__(self, image_path):
        img = Image.open(image_path).convert("L")
        self.terrain = np.array(img) / 255.0
        self.width = self.terrain.shape[1]
        self.height = self.terrain.shape[0]

    # Gibt die Eignung eines bestimmten Punktes (x, y) zurück
    def get_suitability(self, x, y):
        return self.terrain[y, x]
