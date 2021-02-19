# author:丑牛
# datetime:2020/9/25 11:53
import math
import random

# 算出低位0的个数
from redis._compat import xrange


def low_zeros(value):
    for i in xrange(1, 32):
        if value >> i << i != value:
            break
    return i - 1


# 通过随机数记录最大的低位0的个数
class BitKeeper(object):

    def __init__(self):
        self.maxbits = 0

    def random(self, m):
        bits = low_zeros(m)
        if bits > self.maxbits:
            self.maxbits = bits


class Experiment(object):

    def __init__(self, n, k=1024):
        self.n = n
        self.k = k
        self.keepers = [BitKeeper() for i in range(k)]

    def do(self):
        for i in range(self.n):
            m = random.randint(0, 1<<32-1)
            keeper = self.keepers[((m & 0xfff0000) >> 16) % len(self.keepers)]
            keeper.random(m)

    def estimate(self):
        subbits_inverse = 0
        for keeper in self.keepers:
            subbits_inverse += 1.0/float(keeper.maxbits)
        avgbits = float(self.k)/subbits_inverse
        return 2** avgbits * self.k


for i in range(100000, 1100000, 100000):
    exp = Experiment(i)
    exp.do()
    est = exp.estimate()
    print(i, '%.2f' % est, '%.2f' % (abs(est-i) / i))
