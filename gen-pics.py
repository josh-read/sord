import numpy as np
from PIL import Image
from random import randint, choice


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return [red, green, blue]


def random_image():
    upper_left = random_color()
    upper_right = random_color()
    lower_left = random_color()
    lower_right = random_color()

    pixels = np.zeros([400, 400, 3], dtype=np.uint8)
    pixels[:100, :100] = upper_left
    pixels[:100, 100:] = upper_right
    pixels[100:, :100] = lower_left
    pixels[100:, 100:] = lower_left
    return pixels


def main():
    pixels = random_image()
    img = Image.fromarray(pixels)
    img.save('testrgb.png')


if __name__ == '__main__':
    main()
