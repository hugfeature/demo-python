# author:丑牛
# datetime:2021/5/14 11:27
import pytest


def test_add2():
    pytest.assume(1 + 4 == 5)
    pytest.assume(1 + 3 == 3)
    pytest.assume(2 + 5 == 7)
    pytest.assume(2 + 5 == 9)
    print("测试完成")