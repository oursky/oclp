#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os
from PIL import Image, ImageFont, ImageDraw
from StringIO import StringIO

def app_files_path(filename):
    project_dir = os.path.dirname(os.path.realpath(__file__))
    absfile = os.path.abspath(os.path.join(project_dir, '../app_files', filename))
    return absfile

def generate_image(field1, field2, author, scale=1):
    PADDING = (30 * scale, 30 * scale)
    IMAGE_SIZE = (600 * scale, 600 * scale) # width, height
    BG_COLOR = (42, 194, 241) # rgb
    USER_COLOR = (0, 0, 0)
    LABEL_COLOR = (255, 255, 255)
    LINE_WIDTH = 5 * scale
    LINE_SPACING = 25 * scale
    FONT_SIZE = 60 * scale
    AUTHOR_FONT_SIZE = 25 * scale
    LOGO_FILE = 'home-logo-300.png' if scale >= 2 else 'home-logo-150.png'
    LOGO_SIZE = (300, 163) if scale >= 2 else (150, 82)
    LOGO_MARGIN = (15 * scale, 15 * scale)

    font_file = app_files_path('heiti.ttc')
    font = ImageFont.truetype(font_file, FONT_SIZE)
    image = Image.new('RGB', IMAGE_SIZE, BG_COLOR)
    draw = ImageDraw.Draw(image)

    logo = Image.open(app_files_path(LOGO_FILE))
    logo_pos = (IMAGE_SIZE[0] - LOGO_MARGIN[0] - LOGO_SIZE[0],
            (IMAGE_SIZE[1] - LOGO_MARGIN[1] - LOGO_SIZE[1] - 158 * scale))
    image.paste(logo, logo_pos, logo)

    pos = (PADDING[0], PADDING[1] + 158 * scale)
    t = u"全城"
    ts = draw.textsize(t, font=font)
    draw.text(pos, t, LABEL_COLOR, font=font)

    pos = (pos[0] + ts[0], pos[1])
    t = field1
    ts = draw.textsize(t, font=font)
    draw.text(pos, t, USER_COLOR, font=font)

    draw.line((pos[0], pos[1]+ts[1]+8, pos[0]+ts[0], pos[1]+ts[1]+8), fill=0, width=LINE_WIDTH)

    pos = (pos[0] + ts[0], pos[1])
    t = u"!"
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
    t = u"!"
    ts = draw.textsize(t, font=font)
    draw.text((pos[0], pos[1]), t, LABEL_COLOR, font=font)

    author_font = ImageFont.truetype(font_file, AUTHOR_FONT_SIZE)
    pos = (PADDING[0], pos[1] + ts[1] + LINE_SPACING)
    t = author
    ts = draw.textsize(t, font=author_font)
    draw.text((pos[0], pos[1]), t, USER_COLOR, font=author_font)
    draw.line((pos[0], pos[1]+ts[1]+8, pos[0]+ts[0], pos[1]+ts[1]+8), fill=0, width=3 * scale)
    return image

def generate_image_png(*args, **kwargs):
    image = generate_image(*args, **kwargs)

    f = StringIO()
    image.save(f, format="PNG")
    f.seek(0)
    return f.read()

def main():
    open('/vagrant/boo1.png', 'w').write(generate_image_png(u"上水", u"元朗", u"屯門", scale=2))

if __name__=='__main__':
    main()
