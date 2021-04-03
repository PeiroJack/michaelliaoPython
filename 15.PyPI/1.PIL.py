#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路劲：
im = Image.open(r'15.PyPI\test.jpg')
# 获得图片尺寸：
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%：
im.thumbnail((w//2,h//2))
print('Resize image to : %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保持：
im.save(r'15.PyPI\thumbnail.jpg', 'jpeg')

# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save(r'15.PyPI\blur.jpg', 'jpeg')
