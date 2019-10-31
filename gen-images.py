#!/usr/bin/env python3
from pathlib import Path

from PIL import Image, ImageDraw
import random
from math import floor

H = 256
W = 512


def make_image(x, y):
    "Make an image with a blob at the given location."
    im = Image.new("1", (W, H))
    draw = ImageDraw.Draw(im)
    draw.ellipse((x-1, y-1, x+1, y+1), fill=1)
    # im.show()
    return im


def create_image_file(x, y):
    """Make an image with a blob at the given location,
    and save it to a specially-formulated filename."""
    im = make_image(x, y)
    dirname = Path(__file__).parent / 'set1'
    dirname.mkdir(exist_ok=True)
    im.save(dirname / 'img_{}_{}.png'.format(x, y), format='png')

for _ in range(20):
    x = floor(random.uniform(0, W))
    y = floor(random.uniform(0, H))
    create_image_file(x, y)
