# -*- coding: utf-8 -*-

# Let's assume that we have a pair of numbers (a,b). We can get a new pair (a+b,b) or (a,a+b) from the given pair in a single step
# Let the initial pair of numbers be (1,1). Your task is to find number k, that is, the least number of steps needed to transform (1,1) into the pair where at least one number equals n

kbs = {1: (1, 1), 2: (2, -1), 3: (3, -5), 4: (3, -4)}
sum_arr = {'lv': 0, 'arr': [1, 1]}

def sum_arr_next():
    """构造列表至下一层级"""
    arr_old = sum_arr['arr']
    arr_new = []
    for i in range(0, len(arr_old), 2):
        s = arr_old[i] + arr_old[i + 1]
        if arr_old[i] == arr_old[i + 1]:
            arr_new.extend([arr_old[i], s])
        else:
            arr_new.extend([arr_old[i], s, arr_old[i + 1], s])
    sum_arr['arr'] = arr_new
    sum_arr['lv'] += 1
    return

def sum_arr_gen(n: int):
    """构造列表至n层级"""
    step = 2 ** (sum_arr['lv'] - n)
    if step < 1:
        step = (n - sum_arr['lv'])
        for _ in range(step):
            sum_arr_next()
        return sum_arr['arr']
    else:
        return sum_arr['arr'][::step]


def get_m_kb(m: int):
    """求取m个数的n层通项公式即$$k * n + b$$中的$$(k, b)$$"""
    if m % 2 == 1:
        k, b = get_m_kb((m + 1) // 2)
        return k, b - k
    index = (m + 2) // 4
    if index in kbs:
        return kbs[index]
    else:
        k1, b1 = get_m_kb(m // 2 - 1)
        k2, b2 = get_m_kb(m // 2)
        kb = (k1 + k2, b1 + b2 - k1 - k2)
        kbs[index] = kb
        return kb


def find_num(n: int):
    """求取数$$n$$最小层级
    很容易感受到一对数的顺序看上去有关系，实则不影响，所以在下文表述中按从小到大排列

    当目标数第一次出现的时候，一定是作为两个数的和出现的，也即在该层有$$(i, n)$$与$$(j, n)$$，其中$$i + j = n$$

    不妨设$$i < j$$，则上一层存在成对数$$(i, j)$$，再上一层存在$$(i, j - i)$$或者$$(j - i, i)$$

    所以可将$$(m, n)$$通过$$\lfloor \frac{n}{m} \rfloor$$次回溯到$$(n \equiv m, m)$$

    反复几次后会得到$$(0, \lambda)$$，这里多回溯了一步，下一步$$(\lambda, \lambda)$$才是起点

    易证当$$\lambda = 1$$时上述变化在本题成立，即到达$$(1, 1)$$存在，反之$$\lambda > 1$$不可能存在

    而回到刚开始，成对出现的$$i$$与$$j$$中取$$i(i \le \lfloor \frac{n}{2} \rfloor)$$会比取$$j$$快一步，所以遍历$$[2, \lfloor \frac{n}{2} \rfloor]$$找出成立的最小的回溯层级即可
    """
    if n < 5:
        return n - 1
    if n < 9:
        return [3, 5, 4, 4][n - 5]
    if n < 14:
        return 5
    min_gen = n - 1
    for i in range(2, (n + 1) // 2):
        gen = -1
        j = n
        while i:
            gen += j // i
            tmp = j % i
            j = i
            i = tmp
        if j == 1 and gen < min_gen:
            min_gen = gen
    return min_gen

if __name__ == "__main__":
    while True:
        try:
            print(find_num(int(input())))
        except Exception:
            break
