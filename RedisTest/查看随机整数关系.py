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

    def random(self):
        value = random.randint(0, 2 ** 32 - 1)
        bits = low_zeros(value)
        if bits > self.maxbits:
            self.maxbits = bits


class Experiment(object):

    def __init__(self, n):
        self.n = n
        self.keeper = BitKeeper()

    def do(self):
        for i in range(self.n):
            self.keeper.random()

    def debug(self):
        print(self.n, '%.2f' % math.log(self.n, 2), self.keeper.maxbits)


for i in range(1000, 100000, 100):
    exp = Experiment(i)
    exp.do()
    exp.debug()
