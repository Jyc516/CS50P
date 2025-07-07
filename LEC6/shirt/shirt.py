import sys
import os
from PIL import Image
from PIL import ImageOps

def main():
    input, output = get_name()
    try:
        generate_file(input, output)
    except FileNotFoundError:
        sys.exit("Input does not exist", input)


def get_name():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-lines arguments")

    input = sys.argv[1].strip()
    name_i, ext_i = os.path.splitext(input)
    ext_i = ext_i.lower()
    if not (ext_i == ".jpg" or ext_i == ".jpeg" or ext_i == ".png"):
        sys.exit("Invalid input")
    output = sys.argv[2].strip()
    name_o, ext_o = os.path.splitext(input)
    ext_o = ext_o.lower()
    if not (ext_o == ".jpg" or ext_o == ".jpeg" or ext_o == ".png"):
        sys.exit("Invalid output")
    if ext_i != ext_o:
        sys.exit("Input and output have different extensions")

    input = name_i + ext_i
    output = name_o + ext_o
    return input, output


def generate_file(input, output):
    shirt = Image.open("shirt.png")
    photo = Image.open(input)
    shirt = shirt.resize(photo.size)
    photo.paste(shirt, shirt)
    photo.save(output)


main()