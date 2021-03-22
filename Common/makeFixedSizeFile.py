# coding=gbk
# author:丑牛
# datetime:2020/11/18 16:54

import os


def genSizeFile(fileName, fileSize):
    # file path
    filePath = "Data" + fileName + ".csv"
    text = "郑州煤矿机械集团股份有限公司(沪市上市公司601717)始建于1958年，是中国第一台液压支架的诞生地，前身为郑州煤矿机械厂(隶属煤炭部)，是国家\"一五\"计划重点项目，1998年划归河南省煤炭工业管理局管理。总资产30亿元，净资产约6.6亿元，下设9个生产分厂，生产区占地面积约45万平方米，拥有在岗员工4000余人，专业技术人员800余人，高级技术人员200余人，6人享受国家特殊津贴，已累计生产支护高度从0.55米到7米，支护强度从1600kN到16800kN的各型液压支架11万余架。产品遍布全国各大矿业集团，并出口俄罗斯、印度、土耳其等国家。"

    # 生成固定大小的文件
    # date size
    ds = 0
    with open(filePath, "w", encoding="utf8") as f:
        while ds < fileSize:
            f.write(text)
            f.write("\n")
            ds = os.path.getsize(filePath)
    # print(os.path.getsize(filePath))


# start here.
genSizeFile("test-2G", 2*1024 * 1024 * 1024)
