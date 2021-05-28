# -*- coding: utf-8 -*-
import random

from PIL import Image


def areas_exist(x, y, areas):
    """检查坐标是否存在于域内"""
    for area in areas:
        if area[0] <= x <= area[1] and area[2] <= y <= area[3]:
            return True
    else:
        return False


def contrast_ratio(r1, g1, b1, r2, g2, b2):
    """对比度"""
    rl1 = relative_luminance(r1, g1, b1)
    rl2 = relative_luminance(r2, g2, b2)
    return (rl1 + 0.05) / (rl2 + 0.05) if rl1 > rl2 else (rl2 + 0.05) / (rl1 +
                                                                         0.05)


def purple_star(path, size=128, noise=32):
    """紫色星球"""
    im = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    for i in range(size):
        for j in range(size):
            if abs(i - size // 2)**2 + abs(j - size // 2)**2 < size**2 // 4:
                pixel = (
                    i * 2 + random.randint(2, noise + 2) - noise // 2 + 2,
                    random.randint(0, noise),
                    j * 2 + random.randint(2, noise + 2) - noise // 2 + 2,
                    240,
                )
                im.putpixel((i, j), pixel)
    im.save(path)
    return


def relative_luminance(r, g, b):
    """相对亮度"""
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def remove_color_light(src, des, limit=200):
    """将亮度大于限制的颜色转换为透明色"""
    im = Image.open(src)
    im.convert('RGBA')
    w, h = im.size
    pixel = im.load()
    for i in range(w):
        for j in range(h):
            if min([rgba > limit for rgba in pixel[i, j]]):
                pixel[i, j] = (0, 0, 0, 0)
    im.save(des)
    return


def remove_color_rgb(src, des, red=255, green=255, blue=255):
    """将源图片中的rgb颜色转换为透明色并存储至目标文件"""
    im = Image.open(src)
    im = im.convert('RGBA')
    w, h = im.size
    pixel = im.load()
    for i in range(w):
        for j in range(h):
            if pixel[i, j][:-1] == (red, green, blue):
                pixel[i, j] = (0, 0, 0, 0)
    im.save(des)
    return


def rise_planet(des, area=2, deep=-1000, ground=0.5, size=256, speed=10):
    im = Image.new('RGB', (size, size), (0, 0, 0))
    planet = [deep for _ in range(size * size)]
    ratio = 0
    while ratio < ground:
        for i in range(area, size - area, area):
            for j in range(area, size - area, area):
                updt = random.random() * speed
                ctri = random.randint(-area, area)
                ctrj = random.randint(-area, area)
                planet[(i + ctri) * size + j + ctrj] += updt
        ratio = 0
        for h in planet:
            if h > 0:
                ratio += 1
        ratio /= size * size
    hmin = min(planet)
    hmax = max(planet)
    for i in range(size):
        for j in range(size):
            h = planet[i * size + j]
            im.putpixel((i, j), (
                round(h * 255 / hmax if h > 0 else 0),
                round(255 - h * 128 / hmax if h > 0 else 255 - h * 255 / hmin),
                round(0 if h > 0 else h * 255 / hmin),
            ))
    im.save(des)
    return


def sum_alpha_blend(src1, src2, des, alpha=0.5, width=None, height=None):
    """两张图片依照透明度叠加"""
    im1, im2 = Image.open(src1), Image.open(src2)
    im1 = im1.convert('RGBA')
    im2 = im2.convert('RGBA')
    w = width if width else min(im1.width, im2.width)
    h = height if height else min(im1.height, im2.height)
    im1 = im1.resize((w, h), Image.ANTIALIAS)
    im2 = im2.resize((w, h), Image.ANTIALIAS)
    Image.blend(im1=im1, im2=im2, alpha=alpha).save(des)
    return


def sum_back(src,
             back,
             des,
             alpha=0.75,
             blocks=None,
             height=None,
             margin=8,
             mask=200,
             width=None):
    """以`src`为主，设置blocks为范围，为其添加背景"""
    im1, im2 = Image.open(src), Image.open(back)
    im1 = im1.convert('RGBA')
    im2 = im2.convert('RGBA')
    w = width if width else min(im1.width, im2.width)
    h = height if height else min(im1.height, im2.height)
    pixel1 = im1.resize((w, h), Image.ANTIALIAS).load()
    pixel2 = im2.resize((w, h), Image.ANTIALIAS).load()
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    pixel = im.load()
    if not blocks:
        blocks = []
    for i in range(w):
        for j in range(h):
            if areas_exist(i, j, blocks):
                if pixel1[i, j][-1]:
                    pixel[i, j] = pixel1[i, j]
                else:
                    color = [255, 255, 255, 255]
                    for k in range(3):
                        color[k] = round(pixel2[i, j][k] * (1 - alpha) +
                                         mask * alpha)
                    pixel[i, j] = tuple(color)
            else:
                pixel[i, j] = pixel2[i, j]
    im.save(des)
    return
