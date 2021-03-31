# author:丑牛
# datetime:2021/3/4 16:10
import time
from urllib.parse import urlencode

import requests
import pandas as pd


def readXlsX(excelPath):
    """
    读取Excel文件获取文件中数据
    :param excelPath:
    :return:
    """
    df = pd.read_excel(excelPath, usecols=[1, 2])
    data1 = df.values
    # print(data1)
    return data1


def submitAnswer(csrf, cookie, qustionId, strings):
    """
    提交回答
    :param csrf:
    :param cookie:
    :param qustionId:
    :param strings:
    :return:
    """
    url_submitMyAnswer = 'https://developer.aliyun.com/developer/api/my/ask/submitMyAnswer?p_csrf='
    re_url = url_submitMyAnswer + csrf
    data = {
        "questionId": qustionId,
        "content": strings
    }
    re_data = urlencode(data)
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               'Cookie': cookie, 'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}
    re = requests.post(url=re_url, headers=headers, data=re_data)
    return re.text


def listQuestions(head):
    """
    获得问题
    :param head:
    :return:
    """
    pageNum = 1
    url_listQuestion = 'https://developer.aliyun.com/developer/api/my/ask/listMyQuestions?pageNum=1' \
                       + "&pageSize=20"
    re = requests.get(url_listQuestion, headers=head)
    return re.text, re


if __name__ == '__main__':
    path = 'C:\\Users\\wangzhaoxian\\Desktop\\QA.xlsx'
    p_csrf = '09185291-f5d6-44d8-843c-f0552646d033'
    cookie_data = 'c_csrf=09185291-f5d6-44d8-843c-f0552646d033;cna=7v+HGOZYvEcCAX0uTqPzitLI; isg=BLq6zdu_jmw-QQLWLwvf46gACODcaz5FkShECsSzBM0Yt1jxrPrOVAeBA8NrPLbd; l=eBIFr4WejL0hatZvBOfalurza779GIO4YuPzaNbMiOCP_cWX5rAVW6w1ZtxWCn1VnsCXR3ydIATJB2Y3cyzHljHOO9VjZ0pYBdTh.; _bl_uid=ppkq8k07dI2rd6x886005639vCIL; aliyun_choice=CN; _uab_collina=161216118882772450071245; _umdata=G881570C0ECFDEFB2EA112C921A1392D5B4D532; bs_n_lang=zh_CN; console_base_assets_version=3.24.2; currentRegionId=cn-shanghai; tfstk=cg6ABg1fTz4m2QZW-sFofavfywwOZSayySt-BodMjMw7H_kdisWhp9RicU-JtuC..; UM_distic7bb2b6be48+BmL/TKOaxAQqfmgJN9+psA=="; login_aliyunid_abi="BG+wKnj4Est1db350938080640daf859cbe4397ba81+7quBAjl+H8iOyFq2hNBTUG+tAlYH0XArw7IkcNUojpA6AhIFhI8="; login_aliyunid_csrf=_csrf_tk_1473516493001733; login_aliyunid="%E9%97%B2%E5%BA%AD%E5%82%B2%E5%89%91"; login_aliyunid_ticket=58slMT1tJw3_x$$b4ladXZI7DI07sR0ZFktlaCdYDDMhVShMWs6OmiUuFof_BNpwU_TOTNChZBoeM1KJexdfb9zhYnsN5Zos6qISCrRt7mGxbigG2Cd4fWaCmBZHIzsgdZq64XXWQgyKFeuf0vpmV*C*0; hssid=1VpmOoYBqkEIlwbaE-9xlfw1; hsite=6; aliyun_country=CN; aliyun_site=CN'
    # header = {'Cookie': cookie_data}
    # ID = '318465'
    # content = '服务器内部重定向必须使用 forward，否则会因线上采用 HTTPS 协议而导致浏览器提示\'不安全\'，并且还会带来 URL 维护不一致的问题。'
    # print(listQuestions(header))
    # print(submitAnswer(p_csrf, cookie_data, ID, content))
    data = readXlsX(path)
    for i in data:
        # print(i)
        ID = str(i[1])
        # print(ID)
        content = i[0]
        # print(content)
        print('[' + content + ']' + '(' + ID + ')' + '\n')
        # print(ID, submitAnswer(p_csrf, cookie_data, ID, content))
        # time.sleep(20)


