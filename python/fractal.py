from matplotlib import cm
from matplotlib import pyplot as pl
import numpy as np


def iter_point(c):
    z = c
    for i in range(1, 100):  # 最多迭代100次
        if abs(z) > 2: break  # 半径大于2则认为逃逸
        z = z * z + c
    return i  # 返回迭代次数


def draw_mandelbrot(cx, cy, d):
    """
    绘制点(cx, cy)附近正负d的范围的Mandelbrot
    """
    x0, x1, y0, y1 = cx - d, cx + d, cy - d, cy + d
    y, x = np.ogrid[y0:y1:200j, x0:x1:200j]
    c = x + y * 1j
    mandelbrot = np.frompyfunc(iter_point, 1, 1)(c).astype(float)
    pl.imshow(mandelbrot, cmap=cm.jet, extent=[x0, x1, y0, y1])
    pl.gca().set_axis_off()
    return pl


if __name__ == "__main__":
    draw_mandelbrot(-0.5, 0, 1.5).show()
