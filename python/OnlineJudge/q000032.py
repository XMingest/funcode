# -*- coding: utf-8 -*-

# The problem is, given an positive integer N, we define an equation like this:
#       N=a[1]+a[2]+a[3]+…+a[m];
#       a[i]>0,1<=m<=N;
# For example, assume N is 5, we can find:
#       5=1+1+1+1+1
#       5=1+1+1+2
#       5=1+1+3
#       5=1+2+2
#       5=1+4
#       5=2+3
#       5=5
# Note that "5 = 3 + 2" and "5 = 2 + 3" is the same in this problem. Now, you do it!"
# But now , you must output all the equations in lexicographical order;

nums_dict = {1: [[1]]}

def splito_nums(n: int):
    if n in nums_dict:
        return nums_dict[n]
    else:
        nums_dict[n] = []
    i = 1
    while i * 2 <= n:
        for nums in splito_nums(n - i):
            if nums[0] >= i:
                nums_dict[n].append([i] + nums)
        i += 1
    nums_dict[n].append([n])
    return nums_dict[n]

if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            for nums in splito_nums(n):
                print(f'{n}={"+".join(map(str, nums))}')
        except Exception as e:
            break
