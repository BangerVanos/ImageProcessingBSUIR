import cv2
import os
from src.anaglyphs import Anaglyph


anaglyphs_options = {
    'color': ['clr', 'color', 'colour', 'cl', 'c'],
    'half_color': ['hf', 'half', 'hfcl', 'half_color', 'half_colour', 'hc', 'half color',
                   'half colour'],
    'optimized': ['opt', 'optimized', 'o', 'om', 'optim']
}


def run():
    img_path = input('Enter image file path: ')
    while not os.path.isfile(img_path):
        img_path = input('This path does not lead to image!\n'
                         'Enter path to image again: ')

    img = cv2.imread(img_path)
    filename = os.path.split(img_path)[1]
    img_shape = img.shape
    left_part = img
    right_part = img[int(img_shape[0] * 0.04):, int(img_shape[0] * 0.04):]
    left_part = cv2.resize(left_part, (img_shape[1], img_shape[0]), interpolation=cv2.INTER_LINEAR)
    right_part = cv2.resize(right_part, (img_shape[1], img_shape[0]), interpolation=cv2.INTER_LINEAR)

    option = input('Choose anaglyph (for example: color, half color, optimized): ')
    while option not in sum(anaglyphs_options.values(), start=[]):
        option = input('Incorrect option!\n'
                       'Choose anaglyph (for example: color, half color, optimized): ')
    if option in anaglyphs_options['color']:
        result = Anaglyph.color_anaglyph(left_part, right_part)
        cv2.imwrite(f'output/color_{filename}', result)
        print(f'Successfully applied Color Anaglyph to {img_path}')
    elif option in anaglyphs_options['half_color']:
        result = Anaglyph.half_color_anaglyph(left_part, right_part)
        cv2.imwrite(f'output/half_color_{filename}', result)
        print(f'Successfully applied Half Color Anaglyph to {img_path}')
    elif option in anaglyphs_options['optimized']:
        result = Anaglyph.optimized_anaglyph(left_part, right_part)
        cv2.imwrite(f'output/optimized_{filename}', result)
        print(f'Successfully applied Optimized Anaglyph to {img_path}')


if __name__ == '__main__':
    run()
