#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os
from PIL import Image, ImageFont, ImageDraw
from StringIO import StringIO

PADDING = (40, 50)
IMAGE_SIZE = (600, 315) # width, height
BG_COLOR = (42, 194, 241) # rgb
USER_COLOR = (0, 0, 0)
LABEL_COLOR = (255, 255, 255)
LINE_WIDTH = 5
LINE_SPACING = 25

def generate_image(field1, field2, author):
    project_dir = os.path.dirname(os.path.realpath(__file__))
    font_file = os.path.abspath(os.path.join(project_dir, '../app_files/lihei-pro.ttf'))
    font = ImageFont.truetype(font_file, 60)
    image = Image.new('RGB', IMAGE_SIZE, BG_COLOR)
    draw = ImageDraw.Draw(image)

    pos = PADDING
    t = u"全城"
    ts = draw.textsize(t, font=font)
    draw.text(pos, t, LABEL_COLOR, font=font)

    pos = (pos[0] + ts[0], pos[1])
    t = field1
    ts = draw.textsize(t, font=font)
    draw.text(pos, t, USER_COLOR, font=font)

    draw.line((pos[0], pos[1]+ts[1]+8, pos[0]+ts[0], pos[1]+ts[1]+8), fill=0, width=LINE_WIDTH)

    pos = (pos[0] + ts[0], pos[1])
    t = u"！"
    ts = draw.textsize(t, font=font)
    draw.text((pos[0], pos[1]), t, LABEL_COLOR, font=font)

    pos = (PADDING[0], pos[1] + ts[1] + LINE_SPACING)
    t = u"向"
    ts = draw.textsize(t, font=font)
    draw.text(pos, t, LABEL_COLOR, font=font)

    pos = (pos[0] + ts[0], pos[1])
    t = field2
    ts = draw.textsize(t, font=font)
    draw.text(pos, t, USER_COLOR, font=font)

    draw.line((pos[0], pos[1]+ts[1]+8, pos[0]+ts[0], pos[1]+ts[1]+8), fill=0, width=LINE_WIDTH)

    pos = (pos[0] + ts[0], pos[1])
    t = u"說不"
    ts = draw.textsize(t, font=font)
    draw.text((pos[0], pos[1]), t, LABEL_COLOR, font=font)

    pos = (pos[0] + ts[0], pos[1])
    t = u"！"
    ts = draw.textsize(t, font=font)
    draw.text((pos[0], pos[1]), t, LABEL_COLOR, font=font)

    author_font = ImageFont.truetype(font_file, 20)
    pos = (PADDING[0], pos[1] + ts[1] + LINE_SPACING)
    t = author
    ts = draw.textsize(t, font=author_font)
    draw.text((pos[0], pos[1]), t, USER_COLOR, font=author_font)
    draw.line((pos[0], pos[1]+ts[1]+8, pos[0]+ts[0], pos[1]+ts[1]+8), fill=0, width=3)
    return image

def generate_image_png(*args):
    image = generate_image(*args)

    f = StringIO()
    image.save(f, format="PNG")
    f.seek(0)
    return f.read()

def main():
    open('/vagrant/boo1.png', 'w').write(generate_image_png(u"上水", u"元朗", u"屯門"))

if __name__=='__main__':
    main()
