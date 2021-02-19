# author:丑牛
# datetime:2020/7/28 16:30
import json

import requests
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    header = {'Referer': 'https://www.zhcw.com/kjxx/3d/'}
    url = ' https://jc.zhcw.com/port/client_json.php?callback=jQuery112201886261735252588_1595926461637&transactionType=10001001&lotteryId=2&issueCount=1&startIssue=&endIssue=&startDate=&endDate=&type=0&pageNum=1&pageSize=1'
    response = requests.get(url, headers=header)
    body = response.text.split('(')[1].split(")")[0]
    json_res = json.loads(body)
    # print(json_res)
    nums = []
    for data in json_res['data']:
        # print(data)
        qihao = data.get("issue")
        openTime = data.get('openTime')
        win_num = data.get("frontWinningNum")
        # print(len(win_num))
        # print(win_num)
        nums.append(win_num)
    print(nums)

    nums_0, nums_1, nums_2 = [], [], []
    count_0, count_1, count_2 = 0, 0, 0
    for num in nums:
        nums_0.append(int(num[0]))
        nums_1.append(int(num[2]))
        nums_2.append(int(num[4]))
    print(nums_0)
    print(nums_1)
    print(nums_2)
    dataframe = pd.DataFrame({'百位': nums_0, '十位': nums_1, '个位': nums_2})
    dataframe.to_csv('test.csv', index=False, mode='a', sep=',', header=False, encoding="gb2312")
    # s_nums_0 = Series(nums_0)
    # s_nums_0 = s_nums_0.value_counts()
    # s_nums_1 = pd.Series(nums_1)
    # s_nums_1 = s_nums_1.value_counts()
    # s_nums_2 = Series(nums_2)
    # s_nums_2 = s_nums_2.value_counts()


    # def autolabel(rects):
    #     for rect in rects:
    #         height = rect.get_height()
    #         plt.text(rect.get_x(), 1.02 * height, "%s" % height)

    # labels_0 = s_nums_0.index.tolist()
    # sizes_0 = s_nums_0.values.tolist()
    # rect_0 = plt.bar(range(len(sizes_0)), sizes_0, tick_label=labels_0)
    # autolabel(rect_0)

    # labels_1 = s_nums_1.index.tolist()
    # sizes_1 = s_nums_1.values.tolist()
    # rect_1 = plt.bar(range(len(sizes_1)), sizes_1, tick_label=labels_1)
    # autolabel(rect_1)

    # labels_2 = s_nums_2.index.tolist()
    # sizes_2 = s_nums_2.values.tolist()
    # rect_2 = plt.bar(range(len(sizes_2)), sizes_2, tick_label=labels_2)
    # autolabel(rect_2)
    #
    # plt.show()


