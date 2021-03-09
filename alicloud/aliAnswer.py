# author:丑牛
# datetime:2021/3/4 16:10
import time
from urllib.parse import urlencode

import requests
import pandas as pd


def readXlsX(excelPath):
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
    p_csrf = 'a23f4028-8632-4248-aa7a-e430d1f8de83'
    cookie_data = 'c_csrf=a23f4028-8632-4248-aa7a-e430d1f8de83;cna=7v+HGOZYvEcCAX0uTqPzitLI; isg=BLe3XYiOm8iRnh8NIryK6D3PRasBfIveRJf5sQlkPAbmuNL6E0-HLFfenpjmS2NW; l=eBIFr4WejL0ha553BO5anurza77O5IRVCkPzaNbMiInca1Wf_FAybNCQasWD8dtfgtfj4exzpOD6ydED77U_WEMo2aFYGxSpQ_vM-; _bl_uid=ppkq8k07dI2rd6x886005639vCIL; aliyun_choice=CN; _uab_collina=161216118882772450071245; _umdata=G881570C0ECFDEFB2EA112C921A1392D5B4D532; bs_n_lang=zh_CN; console_base_assets_version=3.24.2; currentRegionId=cn-shanghai; login_aliyunid_pk=1960265252395611; login_aliyunid_pks="BG+hxtHgt7YqVlWvTD4TLgT27jrT9ahySQodUSSLD4w=="; login_aliyunid_abi="BG+UWr74tiI5f5b5d493d58af398cbaf0bf748a3466+VSH/UKaPOWjvTBjVolCTbCFXuWfxz793GZw0Dw1QAlgSqqM8RW8="; aliyun_lang=zh; login_aliyunid_csrf=_csrf_tk_1623515249330760; login_aliyunid="%E9%97%B2%E5%BA%AD%E5%82%B2%E5%89%91"; login_aliyunid_ticket=t7SGxRigm2Cb4fGaCdBZWIzmgdHq6sXXZQg4KFWufyvpeV*0*Cm58slMT1tJw3_x$$b4ladXZI7DI07sR0ZFutlcDifnZ73cgInk08W8h0ncof_BNpwU_TOTNChZBoeM1KJexdfb9zhYnsN5Zos6qIrC0; hssid=1YzgIWwyVDlpoIVPU4Ipjfw1; hsite=6; aliyun_country=CN; aliyun_site=CN'
    # header = {'Cookie': cookie_data}
    # ID = '318465'
    # content = '服务器内部重定向必须使用 forward，否则会因线上采用 HTTPS 协议而导致浏览器提示\'不安全\'，并且还会带来 URL 维护不一致的问题。'
    # print(listQuestions(header))
    # print(submitAnswer(p_csrf, cookie_data, ID, content))
    data = readXlsX(path)
    for i in data:
        ID = str(i[1])
        content = i[0]
        print(ID, submitAnswer(p_csrf, cookie_data, ID, content))
        time.sleep(20)


