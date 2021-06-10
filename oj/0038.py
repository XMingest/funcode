# -*- coding: utf-8 -*-

# 存在s与集合nums，判断是否存在nums自己和为s

def fit(s, nums):
    if nums[0] == s:
        return True
    if nums[0] > s:
        return False
    if len(nums) < 2:
        return False
    return fit(s - nums[0], nums[1:])\
            or fit(s, nums[1:])

def func():
    numn, s = map(int, input().strip().split())
    nums = []
    num_sum = 0
    for x in input().strip().split():
        n = int(x)
        if n == s:
            print('YES')
            return
        elif n < s:
            num_sum += n
            i = 0
            while i < len(nums):
                if nums[i] > n:
                    break
                i += 1
            nums.insert(i, n)
    if num_sum > s:
        print('YES' if fit(s, nums) else 'NO')
    elif num_sum == s:
        print('YES')
    else:
        print('NO')
    return

if __name__ == "__main__":
    func()
