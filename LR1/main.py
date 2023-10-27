from PIL import Image
from src.image_processors import median_filter, find_contours, image_equalize
import numpy as np


if __name__ == "__main__":
    original_image = Image.open("image.jpg")

    # Median filter test
    filtered_image = median_filter(original_image, 4)
    filtered_image.save("filtered_image.jpg")

    # Edge highlighting test
    grayscale_image = filtered_image.convert('L')
    image_with_edges = find_contours(grayscale_image, gradient_threshold=160)
    image_with_edges.save('edge_image.jpg')

    # Equalizing test
    equalized_image = image_equalize(filtered_image)
    equalized_image.save('equalized_image.jpg')
