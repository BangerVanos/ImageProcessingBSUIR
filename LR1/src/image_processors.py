import numpy as np
from PIL import Image


def median_filter(image, kernel_size):
    """Median filter. 'image' is array of pixels. 'kernel_size' - how much neighbours of pixel we will filter"""

    # Filtered image pixels matrix
    filtered_image = np.zeros_like(image)

    # Filtering
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Get the pixels in pixel neighbourhood
            neighbors = image[max(i - kernel_size // 2, 0):min(i + kernel_size // 2 + 1, image.shape[0]),
                              max(j - kernel_size // 2, 0):min(j + kernel_size // 2 + 1, image.shape[1])]

            # Sorting pixels
            sorted_neighbors = np.sort(neighbors.reshape(-1))

            # Find median
            filtered_image[i][j] = sorted_neighbors[kernel_size // 2]

    return filtered_image


if __name__ == "__main__":
    image = np.array(Image.open("flip.jpg"))
    filtered_image = median_filter(image, 20)
    Image.fromarray(filtered_image).save("filtered_image.jpg")
