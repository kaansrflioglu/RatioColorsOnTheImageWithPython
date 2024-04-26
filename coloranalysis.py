import numpy as np
import webcolors

def calculate_color_percentage(centers, labels, image_shape):
    # Renk gruplarını ve her grubun piksel sayısını hesapla
    unique_colors, counts = np.unique(labels, return_counts=True)

    # Renklerin yüzdeliklerini hesapla ve büyükten küçüğe sırala
    color_percentages = {}
    total_pixels = image_shape[0] * image_shape[1]
    for color_idx, count in zip(unique_colors, counts):
        color = centers[color_idx].astype(int)  # Küme merkezini al ve tam sayıya dönüştür
        percentage = (count / total_pixels) * 100
        if percentage > 0.5:  # Sadece %0.5'den büyük değerleri göster
            color_name = get_color_name(color)  # Renk kodunu renk adına çevir
            color_percentages[color_name] = percentage

    return color_percentages

def get_color_name(color):
    closest_color = None
    min_distance = float("inf")
    for key, value in webcolors.CSS3_NAMES_TO_HEX.items():
        hex_value = value.lstrip("#")
        r, g, b = tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))
        distance = np.sqrt((color[0] - r) ** 2 + (color[1] - g) ** 2 + (color[2] - b) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_color = key
    return closest_color
