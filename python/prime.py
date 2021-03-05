# coding=UTF-8
from singleton import singleton

@singleton
class Prime:
    K = 120  # 单个元素含有布尔标志位个数
    primes = []  # 质数计算列表

    def count_prime(self, n: int):
        """计算`n`以下的质数数量"""
        if n < 4:
            return [0, 0, 1, 2][n]
        length = (n - 3) // (self.K * 2) + 1
        self.gen(length)
        cnt = 1
        for i in range(length - 1):
            prime_flag = self.primes[i]
            while prime_flag:
                prime_flag &= prime_flag - 1
                cnt += 1
        pend = self.primes[length - 1]
        mask = ((n - 3) // 2 + 1) % self.K
        if mask:
            pend &= (1 << mask) - 1
        while pend:
            pend &= pend - 1
            cnt += 1
        return cnt

    def gen(self, l: int):
        """更新质数计算器至指定长度"""
        lo = len(self.primes)
        if l > lo:
            self.primes += [(1 << self.K) - 1] * (l - lo)
            for i in range(self.K * l):
                if i**2 * 2 + i * 6 + 4 > self.K * l:
                    break
                if not self.primes[i // self.K] & 1 << (i % self.K):
                    continue
                j = max(i, (self.K * lo - i * 3 - 5) // (i * 2 + 3) + 1)
                index = i * j * 2 + (i + j) * 3 + 3
                while index < self.K * l:
                    if self.primes[index // self.K] & 1 << (index % self.K):
                        self.primes[index // self.K] -= 1 << (index % self.K)
                    j += 1
                    index += i * 2 + 3
        return

    def is_prime(self, n: int):
        """判断是否是质数"""
        if n < 1:
            n = -n
        if n < 4:
            return True
        if n % 2:
            i = (n - 3) // 2
            self.gen(i // self.K + 1)
            return self.primes[i // self.K] & 1 << (i % self.K) > 0
        else:
            return False
