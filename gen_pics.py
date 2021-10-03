import numpy as np
from PIL import Image
from random import randint, choice
from string import ascii_letters as chars
import os
import shutil


TARGET_DIR = 'mixed_pics'


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
    ext = ['jpg', 'png']
    img_name = '.'.join([img_name, choice(ext)])
    img.save('/'.join([TARGET_DIR, img_name]))


def clear_folder():
    files = os.listdir(TARGET_DIR)
    filepaths = (os.path.join(TARGET_DIR, f) for f in files)
    for p in filepaths:
        os.remove(p)


def duplicate_images():
    files = os.listdir(TARGET_DIR)
    for i, f in enumerate(files):
        path = os.path.join(TARGET_DIR, f)
        if (i%2 == 0):
            shutil.copyfile(path, os.path.join(TARGET_DIR, ('copy'+f)))


def main():
    clear_folder()
    [random_image() for _ in range(10)]
    duplicate_images()


if __name__ == '__main__':
    main()
