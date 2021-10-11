#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
# iphone5分辨率：1136x640

import os
from PIL import Image

imagefilelist = []
(width, height) = (640, 1136)
# 找出图片类型文件名放入list
for root, dirs, name in os.walk('./image/'):
    for filename in name:
        if filename.endswith('jpg') or filename.endswith('jpeg') or filename.endswith('png'):
            imagefilelist.append(filename)
# 循环处理每张照片
for imagefile in imagefilelist:
    with Image.open('./image/%s' % imagefile) as img:
        # w, h = img.size
        # n = w/1136 if (w/1136) >= (h/640) else h/640  # 宽高没有超过屏幕即不变
        img_new = img.resize((width, height))
        img_new.convert('RGB')
        img_new.save(imagefile)
