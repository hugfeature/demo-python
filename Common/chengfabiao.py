# author:丑牛
# datetime:2020/9/2 15:53
# i = 0
# while i < 9:
#     i += 1
#     j = 0
#     while j < i:
#         j += 1
#         print(f"{j}x{i} = {i*j} ", end="")
#     print()
import random


for i in range(30):
    client = "wzxtest" + str(i)
    topic = "/zmj/test" + str(i)
    print(client, topic)
