from __future__ import division             # Division in Python 2.7
import matplotlib
matplotlib.use('TkAgg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import colorsys as cs

from matplotlib import colors

dane = []
mapa = []

def gradient_hsv(v):
    return cs.hsv_to_rgb(0.3 - 0.3*v, 1, 1)

if __name__ == '__main__':

    with open("big.dem") as f:
        first_line = f.readline().strip()
        rows, cols, dist = map(int, first_line.split()[:3])  
        
        dane = [[0] * cols for _ in range(rows)]
        
        for i, line in enumerate(f):
            values = list(map(float, line.split()))  
            if i < rows:
                dane[i] = values[:cols] 

    
    dane_array = np.array(dane)
    min_val = np.min(dane_array)
    max_val = np.max(dane_array)

    normalized_dane = (dane_array - min_val) / (max_val - min_val)

    # Zwykły gradient
    mapa = np.array([[gradient_hsv(value) for value in row] for row in normalized_dane])

    # Display the `mapa` array as an image
    plt.imshow(mapa, origin='upper')
    plt.title("2D Map Visualization (Red to Green Gradient)")
    plt.axis('off') 

    
    # plt.savefig("2d_map_gradient.png", dpi=300, bbox_inches='tight', pad_inches=0)
    plt.show()