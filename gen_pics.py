from PIL import Image
from random import randint, choice
from string import ascii_letters as chars
import os
import shutil


# Path to directory in which images will be generated
TARGET_DIR = 'mixed_pics'


def random_color():
    """Generate a random 8 bit RGB color."""
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return (red, green, blue)


def random_image():
    """Generate a random image and save to the target directory with a random filename."""
    # Make the image
    img_dims = y, x = (2, 2)
    colors = [random_color() for _ in range(x * y)]
    img = Image.new('RGB', img_dims)
    img.putdata(colors)
    # Make the filename
    img_name = ''.join(choice(chars) for n in range(5))
    img_ext = choice(['jpg', 'png'])
    img_filename = '.'.join([img_name, img_ext])
    img.save('/'.join([TARGET_DIR, img_filename]))


def clear_folder():
    """Remove all files in the target directory."""
    files = os.listdir(TARGET_DIR)
    filepaths = (os.path.join(TARGET_DIR, f) for f in files)
    for p in filepaths:
        os.remove(p)


def duplicate_images():
    """Copy half of the files in target directory, prefixing them with 'copy'."""
    files = os.listdir(TARGET_DIR)
    for i, f in enumerate(files):
        path = os.path.join(TARGET_DIR, f)
        if (i%2 == 0):
            shutil.copyfile(path, os.path.join(TARGET_DIR, ('copy'+f)))


def main():
    """Empty the target directory, generate 10 new random images and copy 5 of them."""
    clear_folder()
    [random_image() for _ in range(10)]
    duplicate_images()


if __name__ == '__main__':
    main()
