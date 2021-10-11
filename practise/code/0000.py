#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

img = Image.open('/Users/herry/Desktop/touxiang.jpeg')
width,length = img.size
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 36)
draw = ImageDraw.Draw(img)
draw.text((width*0.8,0),'99',fill=(255,0,0),font=font)

img.save('/Users/herry/Desktop/new.jpg','JPEG')