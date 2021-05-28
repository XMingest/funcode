import math

import numpy as np
from matplotlib import pyplot as plt


def normfun(x, mu, sigma):
    """正态分布"""
    pdf = np.exp(-(x - mu)**2 /
                 (2 * sigma**2)) / (math.sqrt(2 * math.pi) * sigma)
    return pdf


if __name__ == "__main__":
    # 3D子图1
    fig = plt.figure(figsize=plt.figaspect(0.4))
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    Z = np.absolute(X) + np.absolute(Y)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    # 子图2
    plt.subplot(122)
    area = 16
    size = 512
    x = np.linspace(area, size - area)
    y_sig = normfun(x, size / 2, size / 8)
    plt.plot(x, y_sig)
    # 显示
    plt.show()
