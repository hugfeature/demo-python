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
    p_csrf = '6f1a5b98-9b6e-464c-9f05-1204399e5c4c'
    cookie_data = 'c_csrf=6f1a5b98-9b6e-464c-9f05-1204399e5c4c;cna=7v+HGOZYvEcCAX0uTqPzitLI; isg=BIuLwlYtbwobgbMJNpAepPFrGS91IJ-iOPOVtf2JBkooHK9-h_OV88v68pzyJ_ea; l=eBIFr4WejL0hag2XBO5alurza779CIOVGkPzaNbMiInca6BhhFoWVNCQB5r9Vdtfgt5x6exzpOD6ydFW7bUU-EMo2aFYGXgk5TJwJe1..; _bl_uid=ppkq8k07dI2rd6x886005639vCIL; aliyun_choice=CN; _uab_collina=161216118882772450071245; _umdata=G881570C0ECFDEFB2EA112C921A1392D5B4D532; bs_n_lang=zh_CN; console_base_assets_version=3.24.2; currentRegionId=cn-shanghai; tfstk=ciYRBbxWbxDlM2hfI3n0OSbPNlgdaEMFLu6QJbIO99nnO2ag8scySFIqub1hMGcA.; UM_dtoken%22%3A%22Y2268cecfae8778983f9df67131ed4291%22%2C%22timestamp%22%3A%2240490987555C5D4951406D7A%22%7D; UC-XSRF-TOKEN=4c2b1b60-6658-4c57-8483-812ae4e48d9e; login_aliyunid_csrf=_csrf_tk_1538816382008813; login_aliyunid="%E9%97%B2%E5%BA%AD%E5%82%B2%E5%89%91"; login_aliyunid_ticket=U_BOTwChTBoNM1ZJeedfK9zxYnbN5hossqIZCr6t7SGxRigm2Cb4fGaCdBZWIzmgdHq6sXXZQg4KFWufyvpeV*0*Cm58slMT1tJw3_x$$b4ladXZI7DI07sR0ZFstl_jj5caL_HWv0OgSJrakJpof_pN0; hssid=1fGMExNmWg-4fwdTYfH-IIQ1; hsite=6; aliyun_country=CN; aliyun_site=CN'
    # header = {'Cookie': cookie_data}
    # ID = '318465'
    # content = '服务器内部重定向必须使用 forward，否则会因线上采用 HTTPS 协议而导致浏览器提示\'不安全\'，并且还会带来 URL 维护不一致的问题。'
    # print(listQuestions(header))
    # print(submitAnswer(p_csrf, cookie_data, ID, content))
    data = readXlsX(path)
    for i in data:
        ID = str(i[1])
        # print(ID)
        content = i[0]
        # print(content)
        print(ID, submitAnswer(p_csrf, cookie_data, ID, content))
        time.sleep(20)


