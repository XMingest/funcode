# -*- coding: utf-8 -*-

# 24点，A取值1，J取值11，Q取值12，K取值13

def point24(nums):
    if len(nums) == 1:
        return 24 - 1e-4 < nums[0] < 24 + 1e-4
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            others = nums[: i] + nums[i + 1: j] + nums[j + 1:]
            a = nums[i]
            b = nums[j]
            if point24(others + [a + b]) or\
                point24(others + [a * b]) or\
                point24(others + [a - b]) or\
                point24(others + [b - a]) or\
                (b and point24(others + [a / b])) or\
                (a and point24(others + [b / a])):
                return True
    return False


if __name__ == "__main__":
    rule = {str(i): i for i in range(2, 10)}
    rule.update({
        'A': 1,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
    })
    while True:
        try:
            nums = [rule[x] for x in input().strip().split()]
            print('Yes' if point24(nums) else 'No')
        except Exception:
            break
