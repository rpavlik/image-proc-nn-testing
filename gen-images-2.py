#!/usr/bin/env python3
from pathlib import Path

from PIL import Image, ImageDraw
import random
from math import floor

H = 256
W = 512

# If we let MIN_R be 0, then it permits a single white pixel,
# which we probably want to ignore as noise.
MIN_R = 1
MAX_R = 15
COUNT = 500


def make_image(x, y, r=1):
    "Make an image with a blob at the given location."
    im = Image.new("1", (W, H))
    draw = ImageDraw.Draw(im)
    draw.ellipse((x-r, y-r, x+r, y+r), fill=1)
    # im.show()
    return im


def create_image_file(x, y, r):
    """Make an image with a blob at the given location,
    and save it to a specially-formulated filename."""
    im = make_image(x, y, r)
    dirname = Path(__file__).parent / 'set2'
    dirname.mkdir(exist_ok=True)

    # Images are named x_y_r.png
    im.save(dirname / '{}_{}_{}.png'.format(x, y, r), format='png')


for _ in range(COUNT):
    x = floor(random.uniform(0, W))
    y = floor(random.uniform(0, H))
    r = floor(random.uniform(MIN_R, MAX_R))
    create_image_file(x, y, r)
