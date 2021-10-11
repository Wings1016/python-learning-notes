#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用 Python 生成类似于下图中的字母验证码图片

import string,random
from PIL import Image,ImageFont,ImageDraw,ImageFilter

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)

# 随机颜色1:
def rndColor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)

# 随机颜色2:
def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

for t in range(4):
    value = random.choice(string.ascii_letters)
    draw.text((60*t+20, 10),value,font=font,fill=rndColor2())

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('./verifycode.jpg', 'jpeg')