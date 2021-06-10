# -*- coding: utf-8 -*-

#       21 22……
#       20  7  8  9 10
#       19  6  1  2 11
#       18  5  4  3 12
#       17 16 15 14 13
# 看清楚以上数字排列的规律，设1点坐标为(0,0)，x方向向右为正，y方向向下为正。例如7的坐标为(-1,-1)，2的坐标为(1,0)，3的坐标为(1,1)。
# 编程实现输入任意坐标(x,y)，输出对应的数字。

def helix_to(x: int, y: int):
    ax = -x if x < 0 else x
    ay = -y if y < 0 else y
    dis = ay if ax < ay else ax
    if x > 0 and y < 0:
        if x + y > 0:
            dis -= 1
        return dis * dis * 4 + 1 + dis * 4 + x + y
    elif y < 0:
        return dis * dis * 4 + 1 + dis * 2 + x - y
    elif x > 0:
        return dis * dis * 4 + 1 - dis * 2 - x + y
    else:
        return dis * dis * 4 + 1 - x - y

if __name__ == "__main__":
    while True:
        try:
            x, y = map(int, input().strip().split())
            print(helix_to(x, y))
        except Exception as e:
            break
