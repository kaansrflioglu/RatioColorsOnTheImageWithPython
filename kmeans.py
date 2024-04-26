import numpy as np
from sklearn.cluster import KMeans

def kmeans_clustering(image_rgb, num_clusters=5):
    # Resmi yeniden şekillendirerek pikselleri düzenle
    pixels = image_rgb.reshape(-1, 3)

    # K-means kümeleme uygula
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(pixels)
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_

    return centers, labels
