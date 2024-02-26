'''
    This script was created for "private" (actually no huh) use.

    Image To Json

    How to use:
    1.  Drag n Drop .png image on this script and u got a json image format in script folder.
    2.  Run script through console with argument "disc:/PATH/TO/YOUR/IMAGE.png"

    JSON Structure:
    {
        "size": [x, y],
        "colors_set": [
            [r, g, b, a]
        ],
        "pixels": [
            [x, y, color id]
        ]
    }

    Thx for using this wierd script.

    Made by CoCuCoH41k
'''

from PIL import Image
import os, sys, json

colors_set = []
pixels = []
size = []


def call_color(r, g, b, a) -> bool:
    global colors_set
    if not ((r, g, b, a) in colors_set):
        colors_set.append((r, g, b, a))
        return False
    return True


def get_color_index(r, g, b, a) -> int:
    global colors_set
    if not call_color(r, g, b, a):
        print(f'No such color as {r, g, b, a}. Appending...')
    return colors_set.index((r, g, b, a))

def get_pixel_data() -> list:
    global size, pixels
    data = []
    index = 0
    for x in range(size[0]):
        for y in range(size[1]):
            color = pixels[index]
            data.append([x, y, get_color_index(color[0], color[1], color[2], color[3])])
            index += 1
    return data
def prepare_image(path) -> Image:
    if not os.path.exists(path):
        print(f'File at "{path}" is doesnt exist.')
        exit(0)

    global size, colors_set, pixel
    image = Image.open(path)
    for tup in image.getcolors():
        colors_set.append(tup[1])
    size.append(image.size[0])
    size.append(image.size[1])
    raw_pixels :list = image.load()
    for x in range(size[0]):
        for y in range(size[1]):
            pixels.append(raw_pixels[x, y])


def do_dict() -> dict:
    global size, colors_set
    pixels_set = get_pixel_data()
    data = {
        "size": size,
        "colors_set": colors_set,
        "pixels": pixels_set
    }
    return data


def main(args):
    prepare_image(args[1])
    data = do_dict()
    path = r''
    raw_path = args[0].split('\\')[:len(args[0].split('\\')) - 1]
    json_name = args[1].split('\\')[len(args[1].split('\\')) - 1].split('.')[0] + '.json'
    print(json_name)
    for point in raw_path:
        path += point + '\\'
    with open(path + json_name, 'w') as file:
        json.dump(data, file)


main(sys.argv)

