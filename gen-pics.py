import numpy as np
from PIL import Image
from random import randint, choice
from string import ascii_letters as chars


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return [red, green, blue]


def random_pixels():
    upper_left = random_color()
    upper_right = random_color()
    lower_left = random_color()
    lower_right = random_color()

    pixels = np.zeros([150, 150, 3], dtype=np.uint8)
    pixels[:75, :75] = upper_left
    pixels[:75, 75:] = upper_right
    pixels[75:, :75] = lower_left
    pixels[75:, 75:] = lower_right
    return pixels


def random_image():
    pixels = random_pixels()
    img = Image.fromarray(pixels)
    # Random filename
    img_name = []
    [img_name.append(choice(chars)) for n in range(5)]
    img_name = ''.join(img_name)
    ext = ['jpg', 'png', 'pdf']
    img_name = '.'.join([img_name, choice(ext)])
    img.save(img_name)


def main():
    random_image()

if __name__ == '__main__':
    main()
