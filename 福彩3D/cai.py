# author:丑牛
# datetime:2020/7/28 16:30
import json

import requests
import pandas as pd

if __name__ == '__main__':
    # header = {'Referer': 'http://www.cwl.gov.cn/kjxx/fc3d/kjgg/'}
    # url = "http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=3d&issueCount=1000"
    header = {'Referer': 'https://www.zhcw.com/kjxx/3d/'}
    url = ' https://jc.zhcw.com/port/client_json.php?callback=jQuery112201886261735252588_1595926461637&transactionType=10001001&lotteryId=2&issueCount=1000&startIssue=&endIssue=&startDate=&endDate=&type=0&pageNum=1&pageSize=1000'
    response = requests.get(url, headers=header)
    body = response.text.split('(')[1].split(")")[0]
    json_res = json.loads(body)
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
    dataframe.to_csv('20200730.csv', index=False, header=False, sep=',')


