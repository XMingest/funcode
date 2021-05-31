# -*- coding: utf-8 -*-
import numpy
from matplotlib import pyplot, widgets


class Mandelbrot:
    def __init__(self, escape_times=128, quantity=256):
        """
        曼德博集合
        :param escape_times: 逃逸时间，即对`c`验证的迭代次数
        :param quantity: 在实部和虚部分别选取渲染的数量
        """
        self.config(escape_times, quantity)
        return

    def config(self, escape_times=None, quantity=None):
        """
        配置参数
        :param escape_times:
        :param quantity:
        :return:
        """
        if isinstance(escape_times, int):
            self.__escp_tms = escape_times
        if isinstance(quantity, int):
            self.__qntt = quantity * 2 + 1
        return self

    def data(self):
        """
        返回集合数据
        :return:
        """
        dt = numpy.empty([self.__qntt, self.__qntt])
        for i in range(self.__qntt):
            for j in range(self.__qntt):
                dt[i, j] = self.get_escape_cost(i * 4 / self.__qntt - 2 + (j * 4 / self.__qntt - 2) * 1j)
        return dt

    def get_escape_cost(self, c):
        """
        检查该数是否能在指定时间内逃逸，返回逃逸所花时间占给定逃逸时间比例
        :param c:
        :return:
        """
        if abs(c) * 4 < 1:
            return 1
        z = c
        for i in range(self.__escp_tms):
            if abs(z) > 2:
                return i / self.__escp_tms
            z = z * z + c
        return 1


if __name__ == "__main__":
    mdata = Mandelbrot()
    im = pyplot.imshow(mdata.data(), cmap='GnBu', extent=[-2, 2, -2, 2])
    s_estm = widgets.Slider(pyplot.axes((0.25, 0.95, 0.5, 0.03,)), 'Escape Time',
                            8, 128, valinit=128, valstep=1)
    s_qntt = widgets.Slider(pyplot.axes((0.25, 0.91, 0.5, 0.03,)), 'Check Quantity',
                            64, 256, valinit=256, valstep=1)


    def main(val):
        mdata.config(s_estm.val, s_qntt.val)
        im.set_array(mdata.data())


    s_estm.on_changed(main)
    s_qntt.on_changed(main)
    pyplot.show()
