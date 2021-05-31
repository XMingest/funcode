import math
from turtle import Screen, Turtle


class Point:
    x = 0
    y = 0


class AutoTurtle:
    def __init__(self):
        self.screen = Screen()
        self.center = Point()
        self.size = 128
        self.turtle = Turtle()
        self.turtle.pencolor('silver')
        self.turtle.pensize(4)
        self.turtle.speed(0)
        return

    def helical(self, offset):
        """从中心偏移外旋"""
        offset %= 90
        self.turtle.pu()
        self.turtle.goto(self.center.x, self.center.y)
        self.turtle.pd()
        for i in range(360):
            self.turtle.fd(self.size * i / 180)
            self.turtle.rt(offset)
        return self

    def polygon(self, n):
        """画圆内切多边形"""
        self.turtle.pu()
        self.turtle.goto(self.center.x - self.size, self.center.y)
        self.turtle.seth(90 - 180 / n)
        self.turtle.pd()
        for i in range(n):
            self.turtle.fd(math.sin(math.pi / n) * self.size * 2)
            self.turtle.rt(360 / n)
        return self

    def set_center(self, x, y):
        """改变中心"""
        self.center.x = x
        self.center.y = y
        return self

    def snow_draw(self, n):
        """雪花曲线"""

        def __action(n, length):
            if n == 0:
                self.turtle.fd(length)
            else:
                for i in [0, 60, -120, 60]:
                    self.turtle.left(i)
                    __action(n - 1, length / 3)

        self.turtle.pu()
        self.turtle.goto(self.center.x - self.size / 2, self.size * math.tan(math.pi / 6) / 2 + self.center.y)
        self.turtle.seth(0)
        self.turtle.pd()
        for i in range(3):
            __action(n, self.size)
            self.turtle.right(120)
        return self


if __name__ == "__main__":
    AutoTurtle().helical(73).set_center(-320, 0).polygon(16).set_center(280, 0).snow_draw(3).screen.exitonclick()
