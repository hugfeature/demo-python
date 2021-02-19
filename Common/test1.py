# author:丑牛
# datetime:2021/2/4 14:14
s = input()
t = input()


def isSubsequence(s: str, t: str) -> bool:
    end = len(s)
    start = 0
    for i in t:
        if start >= end:
            return False
        if i not in s[start:end]:
            return False
        else:
            start = s.index(i, start, end) + 1
    return True


result = isSubsequence(s, t)
if result:
    print("Yes")
else:
    print("No")
