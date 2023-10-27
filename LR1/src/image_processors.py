import PIL.Image
import numpy as np
from PIL import Image
import math


def median_filter(image: PIL.Image.Image, kernel_size) -> PIL.Image.Image:
    # Pillow image to array of pixels
    image_pixels = np.array(image)

    # Filtered image pixels matrix
    filtered_image = np.zeros_like(image_pixels)

    # Filtering
    for i in range(image_pixels.shape[0]):
        for j in range(image_pixels.shape[1]):
            # Get the pixels in pixel neighbourhood
            neighbors = image_pixels[max(i - kernel_size // 2, 0):min(i + kernel_size // 2 + 1, image_pixels.shape[0]),
                        max(j - kernel_size // 2, 0):min(j + kernel_size // 2 + 1, image_pixels.shape[1])]
            neighbors = np.concatenate(neighbors)

            # Sorting pixels
            sorted_neighbors = neighbors[np.lexsort((neighbors[:, 0], neighbors[:, 1], neighbors[:, 2]))]

            # Find median
            filtered_image[i][j] = sorted_neighbors[kernel_size // 2]

    return Image.fromarray(filtered_image)


def find_contours(grayscale_image: PIL.Image.Image, gradient_threshold: int = 10) -> PIL.Image.Image:
    image_pixels = np.array(grayscale_image)

    for i in range(image_pixels.shape[0] - 1):
        for j in range(image_pixels.shape[1] - 1):
            current_pixel = image_pixels[i][j]
            right_pixel = image_pixels[i][j + 1]
            up_pixel = image_pixels[i + 1][j]

            dx = abs(right_pixel - current_pixel)
            dy = abs(up_pixel - current_pixel)

            gradient = min(255, math.sqrt(dx**2 + dy**2))
            if gradient > gradient_threshold:
                image_pixels[i][j] = 255
            else:
                image_pixels[i][j] = 0

    return Image.fromarray(image_pixels, mode='L')


def image_equalize(image: PIL.Image.Image) -> PIL.Image.Image:
    image_pixels = np.array(image)

    hist = np.histogram(image_pixels, bins=256)

    # Вычисление PDF гистограммы
    pdf = hist[0] / hist[0].sum()

    # Интегрирование PDF гистограммы
    cdf = np.cumsum(pdf)

    # Нахождение нового значения яркости для каждого пикселя изображения
    new_image_array = np.zeros_like(image_pixels)
    for i in range(image_pixels.shape[0]):
        for j in range(image_pixels.shape[1]):
            new_image_array[i, j] = cdf[image_pixels[i, j]] * 255

    # Создание нового изображения
    new_image = Image.fromarray(new_image_array.astype(np.uint8))
    return new_image

