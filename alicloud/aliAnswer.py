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
    df = pd.read_excel(excelPath, usecols=[2, 4])
    data1 = df.values
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
    p_csrf = '3d51362a-fecc-444a-8c3a-e6e89e875f20'
    cookie_data = 'c_csrf=3d51362a-fecc-444a-8c3a-e6e89e875f20;p_cna=7v+HGOZYvEcCAX0uTqPzitLI; isg=BJWVx-vRWZ0HMH0nXMKI4is5p5FPkkmkMoHbGxc6yoxXbrFg3eHWdgVoPPJY9WFc; l=eBIFr4WejL0haV3ABO5CFurza77T0IRVGkPzaNbMiInca6tF_FFvUNCQ1BNM8dtfgtfc8exzpOD6ydUv7SUT5EMo2aFYGXMbMrpM-; _bl_uid=ppkq8k07dI2rd6x886005639vCIL; aliyun_choice=CN; _uab_collina=161216118882772450071245; _umdata=G881570C0ECFDEFB2EA112C921A1392D5B4D532; bs_n_lang=zh_CN; console_base_assets_version=3.24.2; currentRegionId=cn-shanghai; login_aliyunid_pk=1960265252395611; login_aliyunid_pks="BG+Knp/4ORTOK+0PHplGePsx7aliyunid="%E9%97%B2%E5%BA%AD%E5%82%B2%E5%89%91"; login_aliyunid_ticket=dHI6sgXZqg4XFWQfyKpeu*0vCmV8s*MT5tJl3_1$$w4lxdXbI7aI0ZsRDZF7tl03_naKw9lXFD8GjyGqPirDf_MNpoU_BOTwChTBoNM1ZJeedfK9zxYnbN5hossqIZCr6t7SGxRigm2Cb4fGaCdBZWmz0; login_aliyunid_luid="BG+6WW2NDn4b59215d31f888dceb7b381f0b0e4276d+QXH7PBRcCvL1MHdzIrgo4w=="; login_aliyunid_abi="BG+PGi2E4w941fdf3c27cf2e2258e03a096e7eebe8d+5X5EYnsSCYelnAj5ULilxipHbryOMvBEVkOBmcmQvWyaNGKkA8g="; hssid=1a-N7RwNtOWsR2s4RuxLeIQ1; hsite=6; aliyun_country=CN; aliyun_site=CN'
    # header = {'Cookie': cookie_data}
    # ID = '318465'
    # content = '服务器内部重定向必须使用 forward，否则会因线上采用 HTTPS 协议而导致浏览器提示\'不安全\'，并且还会带来 URL 维护不一致的问题。'
    # print(listQuestions(header))
    # print(submitAnswer(p_csrf, cookie_data, ID, content))
    data = readXlsX(path)
    for i in data:
        ID = str(i[1])
        print(ID)
        content = i[0]
        print(content)
        print(ID, submitAnswer(p_csrf, cookie_data, ID, content))
        time.sleep(20)


