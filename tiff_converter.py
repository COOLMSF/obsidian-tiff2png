from PIL import Image
import sys

def convert_tiff_to_png(tiff_path, png_path):
    with Image.open(tiff_path) as image:
        image.save(png_path, 'PNG')


if __name__ == '__main__':
    convert_tiff_to_png(sys.argv[1], sys.argv[2])