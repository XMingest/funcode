# -*- coding: utf-8 -*-
import gc
import json
import random
from pathlib import Path
from PIL import Image, ImageFilter


class RisePlanet:
    def __adh(self, x, y, dh):
        return self.__sth(x, y, self.__gth(x, y) + dh)

    def __gth(self, x, y):
        x, y = self.__pos(x, y)
        return self.height_map[self.size * x + y]

    def __init__(self, area=4, deep=512, size=512, speed=256):
        self.area = area
        self.deep = -abs(deep)
        self.height_map = [self.deep for _ in range(size * size)]
        self.size = size
        self.speed = speed

    def __ns(self):
        # 正态
        s = round(random.normalvariate(self.size / 2, self.size / 4))
        # s = int(random.random() * self.size)
        return s

    def __pos(self, x, y):
        while x < 0:
            x += self.size
        while x >= self.size:
            x -= self.size
        while y < 0:
            y += self.size
        while y >= self.size:
            y -= self.size
        return x, y

    def __sth(self, x, y, h):
        x, y = self.__pos(x, y)
        if x == 0 or y == 0 or x + 1 == self.size or y + 1 == self.size:
            self.height_map[self.size * x + y] = -self.deep if h > 0 else self.deep
            return self
        h = max(self.deep, h)
        h = min(-self.deep, h)
        self.height_map[self.size * x + y] = h
        return self

    def flattened(self):
        for i in range(self.area, self.size, self.area):
            for j in range(self.area, self.size, self.area):
                h_avg = 0
                for di in range(i - self.area, i + self.area):
                    for dj in range(j - self.area, j + self.area):
                        h_avg += self.__gth(di, dj)
                h_avg /= self.area * self.area * 4
                for di in range(i - self.area, i + self.area):
                    for dj in range(j - self.area, j + self.area):
                        h = self.__gth(di, dj)
                        h += (h_avg - h) / 2
                        self.__sth(di, dj, h)
        return self

    def info(self):
        hmin = -self.deep
        hmax = self.deep
        hover = 0
        for h in self.height_map:
            if h < hmin:
                hmin = h
            if h > hmax:
                hmax = h
            if h > 0:
                hover += 1
        return f'[{round(hmin)}, {round(hmax)}], {hover} / {self.size ** 2}'

    def load_json(self, file):
        with open(file, 'r') as input:
            self.height_map = json.load(input)
        return self

    def process(self, turn=256):
        for _ in range(turn):
            self.rise(self.__ns(), self.__ns())
        return self

    def rise(self, x, y):
        h = self.__gth(x, y)
        updt = random.random() * self.speed
        k = updt * 6 / ((self.area * 2 + 1) * (self.area + 1) * self.area)
        will_rise = 1 if random.random() > 0.5 else -1
        ha = -random.random() * self.deep / 2
        if h > ha:
            will_rise = -1
        elif -h > ha:
            will_rise = 1
        # 0
        self.__adh(x, y, will_rise * updt * 4)
        # dx = 0 or dy = 0
        for d in range(1, self.area):
            dis = will_rise * (updt * 4 + d * k)
            self.__adh(x, y + d, dis)
            self.__adh(x, y - d, dis)
            self.__adh(x + d, y, dis)
            self.__adh(x - d, y, dis)
        # other
        for dx in range(1, self.area):
            for dy in range(1, self.area):
                dis = will_rise * (updt * 4 + (dx + dy) * k)
                if dx + dy > self.area:
                    dis = -dis
                self.__adh(x + dx, y + dy, dis)
                self.__adh(x + dx, y - dy, dis)
                self.__adh(x - dx, y + dy, dis)
                self.__adh(x - dx, y - dy, dis)
        return self

    def save_img(self, des):
        with Image.new('RGB', (self.size, self.size)) as im:
            for i in range(self.size):
                for j in range(self.size):
                    h = self.__gth(i, j)
                    if h > 0:
                        im.putpixel((i, j), (
                            round(-h * 255 / self.deep),
                            round(255 + h * 128 / self.deep),
                            0,
                        ))
                    else:
                        im.putpixel((i, j), (
                            0,
                            0,
                            round(255 - h * 255 / self.deep),
                        ))
            try:
                im.save(des)
            except KeyboardInterrupt:
                print('保存图片中，请稍等...')
                im.save(des)
                exit()
            except PermissionError:
                pass
        return self

    def save_json(self, file):
        try:
            with open(file, 'w') as output:
                json.dump(self.height_map, output)
        except KeyboardInterrupt:
            print('保存JSON中，请稍等...')
            with open(file, 'w') as output:
                json.dump(self.height_map, output)
            exit()
        return self


if __name__ == "__main__":
    files = {
        'db': 'planet.json',
        'png': 'planet.png',
    }
    plnt = RisePlanet()
    if Path(files['db']).exists():
        plnt.load_json(files['db'])
    gc.enable()
    while True:
        plnt.process().flattened()
        print(plnt.info())
        plnt.save_json(files['db']).save_img(files['png'])
        gc.collect()
