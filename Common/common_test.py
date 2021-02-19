# author:丑牛
# datetime:2020/5/18 18:26


import datetime
import json
import random
import struct

from dateutil.relativedelta import relativedelta

if __name__ == "__main__":
    # 十六进制转十进制
    STRING = b'\x00\x00\x00\x00\x00\x00\x00\x01'
    num2 = struct.unpack('!d', STRING)[0]
    print(num2)
    # 数字和字符的转换
    # num1 = 4783
    # b1 = num1.to_bytes(2, "big")
    # num2 = int.from_bytes(b1, 'big')
    # 生成查询label
    # id_n = 1
    # while True:
    #     msg = {"sysCode": "19000010", 'deviceCode': "000100010001" + "%04d" % id_n,
    #            'dataID': "010001", 'nameSpace': "test202101"}
    #     id_n = id_n + 1
    #     print(json.dumps(msg))
    #     if id_n == 201:
    #         break
    # 插入test——event
    # num = 0
    # topic_list = ["260001", "260002", "260003", "260004", "260005"]
    # topic = random.choice(topic_list)
    # label = "010001000100010001" + "%06d" % num
    # value = random.randint(0, 9999)
    # timestamp = 1594283310597
    # message_list = ["支柱压力过低预警 :支架号[3, 30, 34, 45, 71, 76, 81, 83, 85]",
    #                 "支架跳架预警: 跳架时间戳：1594364297489 跳架支架号：115",
    #                 "两端头使用记忆截割预警",
    #                 "乳化液浓度跳动幅度超过4%预警",
    #                 "两端头使用自动跟机预警",
    #                 "泵箱液位低于300mm预警"]
    # message = random.choice(message_list)
    # state = 1
    # rule = 12
    # starttime = datetime.datetime.now().timestamp() * 1000
    # endtime = 1594283310597 + 1
    # insert_sql = "insert into ts_event values" \
    #              " ( " + '\'' + topic + '\'' + "," + '\'' + label + '\'' + "," + '\'' + str(value) + '\'' + "," + str(timestamp) + "," + '\'' + message + '\'' + "," + str(state) + "," + '\'' + str(rule) + '\'' + "," + str(starttime) + "," + str(endtime) + ")"
    # print(insert_sql)
