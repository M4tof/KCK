from __future__ import division
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import colorsys as cs

dane = []
mapa = []

def gradient_hsv(v):
    return cs.hsv_to_rgb(0.3 - 0.3 * v, 1, 1)

def calculate_shading(normalized_dane, light_vector, sun_power):
    rows, cols = normalized_dane.shape
    shaded_map = np.zeros((rows, cols, 3))

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            #różnica w elewacji, razy 2 dla większego efektu 3d
            dzdx = (normalized_dane[i, j + 1] - normalized_dane[i, j - 1]) * 2
            dzdy = (normalized_dane[i + 1, j] - normalized_dane[i - 1, j]) * 2

            # normalizacja wektora prostopadłego do zbocza
            v = np.array([-dzdx, -dzdy, 1.0])
            v = v / np.linalg.norm(v)

            # cosinus kąta
            intensity = np.dot(v, light_vector)

            # jasność ze względu na słońce
            intensity *= sun_power

            # transformacje z wartości punktu do cieniowanego rgb (przejście przez hsv dla lepszej kontroli)
            hsv_color = cs.rgb_to_hsv(*gradient_hsv(normalized_dane[i, j]))
            shaded_rgb = cs.hsv_to_rgb(hsv_color[0], hsv_color[1], intensity)
            shaded_map[i, j] = shaded_rgb

    return shaded_map

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
    normalized_dane = (dane_array - min_val) / (max_val - min_val)  #normalizowane dane z pliku

    mapa = np.array([[gradient_hsv(value) for value in row] for row in normalized_dane])
    # w tym miejscu mapa "Wygląda płasko"
        # plt.imshow(mapa, origin='upper')
        # plt.axis('off')
        # plt.title("Unshaded Map")
        # plt.show()

    light_vector = np.array([-1, -1, 1])    # pozycja słońca
    light_vector = light_vector / np.linalg.norm(light_vector)

    sun_power = 1.7 #stopień rozjaśniania
    shaded_mapa = calculate_shading(normalized_dane, light_vector, sun_power) #funkcja do cieniowania

    plt.imshow(shaded_mapa, origin='upper')
    plt.axis('off')
    plt.savefig("ocieniowana-mapa.pdf", dpi=300, bbox_inches='tight', pad_inches=0)
        # plt.show()