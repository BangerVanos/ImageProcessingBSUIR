import cv2
import numpy as np


class Anaglyph:

    @staticmethod
    def color_anaglyph(left, right):
        result = np.zeros_like(left, dtype=np.uint8)

        left_red = left[:, :, 2]

        right_green = right[:, :, 1]
        right_blue = right[:, :, 0]

        result[:, :, 2] = left_red
        result[:, :, 1] = right_green
        result[:, :, 0] = right_blue

        return result

    @staticmethod
    def half_color_anaglyph(left, right):
        result = np.zeros_like(left, dtype=np.uint8)

        left_red = left[:, :, 2]
        left_green = left[:, :, 1]
        left_blue = left[:, :, 0]

        right_green = right[:, :, 1]
        right_blue = right[:, :, 0]

        result[:, :, 2] = (left_red * 0.299) + (left_green * 0.587) + (left_blue * 0.114)
        result[:, :, 1] = right_green
        result[:, :, 0] = right_blue

        return result

    @staticmethod
    def optimized_anaglyph(left, right):
        result = np.zeros_like(left, dtype=np.uint8)

        left_green = left[:, :, 1]
        left_blue = left[:, :, 0]

        right_green = right[:, :, 1]
        right_blue = right[:, :, 0]

        result[:, :, 2] = (left_green * 0.7) + (left_blue * 0.3)
        result[:, :, 1] = right_green
        result[:, :, 0] = right_blue

        return result
