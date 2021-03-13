# -*- coding: utf-8 -*-

#     1  2  3  4  5  6  7  8  9  10
#     27 28 29 30 31 32 33 34 11
#     26 45 46 47 48 49 35 12
#     25 44 54 55 50 36 13
#     24 43 53 51 37 14
#     23 42 52 38 15
#     22 41 39 16
#     21 40 17
#     20 18
#     19
# (这是一个10阶的螺旋三角)看清楚以上图的数字排列的规律了吧，你的任务就是给定任意的n，输出n阶的螺旋三角

def get_rotate_trangle(i: int, j: int, n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return [[1, 2], [3]][i][j]
    if n == 3:
        return [[1, 2, 3], [6, 4], [5]][i][j]
    if i == 0:
        return j + 1
    if j == 0:
        return n * 3 - i - 2
    if i + j + 1 == n:
        return n + i
    return get_rotate_trangle(i - 1, j - 1, n - 3) + n * 3 - 3

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print(' '.join([str(get_rotate_trangle(i, j, n)) for j in range(n - i)]))
