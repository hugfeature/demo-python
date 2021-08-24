# author:丑牛
# datetime:2021/2/4 14:14
import datetime
import json
import random
import time
from typing import List

# def kthLargestValue(matrix: List[List[int]], k: int) -> int:
#     m, n = len(matrix), len(matrix[0])
#     results = list()
#     for i in range(0, m):
#         for j in range(0, n):
#             a = matrix[i - 1][j - 1] + matrix[i][j]
#             print(a)
#             results.append(a)
#     results.sort(reverse=True)
#     print(results)
#     return results[k - 1]
# if __name__ == "__main__":
#     a = [[5,2],[1,6]]
#     k = 2
#     print(kthLargestValue(matrix=a, k=k))
import requests

req = requests.get('https://geo.datav.aliyun.com/areas_v2/bound/100000_full.json')
req.encoding = 'utf-8'
result = json.loads(req.text)
# print(result)
dict_area = dict()
features = result["features"]
i = 0
for province_feature in features:  # 循环各省
    adcode = str(province_feature["properties"]["adcode"])
    name = province_feature["properties"]["name"]
    center = province_feature["properties"]["center"]
    dict_area[adcode] = name
    print(center)
    print('name{0} is {1}, adcode is {2} '.format(i, name, adcode))
    i = i + 1
    if adcode[4:] != '00':  # 直辖市的下一级别直接是区，没有市级别
        continue
