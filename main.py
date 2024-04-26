import cv2
from kmeans import kmeans_clustering
from coloranalysis import calculate_color_percentage

if __name__ == "__main__":
    # Resmi oku
    image_path = "image.png"
    image = cv2.imread(image_path)

    # Renk uzayını BGR'den RGB'ye dönüştür
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # K-means kümeleme uygula
    centers, labels = kmeans_clustering(image_rgb)

    # Renk yüzdeliklerini hesapla
    color_percentages = calculate_color_percentage(centers, labels, image.shape)

    # Renkleri yüzdelerine göre büyükten küçüğe sırala
    sorted_colors = sorted(color_percentages.items(), key=lambda x: x[1], reverse=True)

    for color_name, percentage in sorted_colors:
        print(f"Color: {color_name} %{percentage:.2f}")
