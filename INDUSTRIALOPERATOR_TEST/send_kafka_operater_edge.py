import json
import multiprocessing
import random
import datetime

# from dateutil.relativedelta import relativedelta
from kafka import KafkaProducer
from kafka.errors import KafkaError
# 云侧
# producer = KafkaProducer(bootstrap_servers='192.168.175.234:9092,192.168.175.235:9092,192.168.175.236:9092')
# topic = 'whl_test'
# 边缘侧
producer = KafkaProducer(
    bootstrap_servers='192.168.175.228:9092,192.168.175.228:9093,192.168.175.228:9094')
topic = 'wzx_test'


def test():
    try:
        n = 0
        num = 0
        while True:
            # 特殊时间处理
            # msg_time = datetime.datetime.now() + relativedelta(years=1, months=1, days=0)
            # 获取当前时间
            msg_time = datetime.datetime.now()
            value = random.randint(0, 9999)
            num = num + 1
            dataId = '01' + "%04d" % num
            # 消息体
            msg = {'Value': value, 'SysCode': '26000101', 'ChannelCode': "001001",
                   'DeviceCode': '0001000100010001', 'DataID': dataId, 'UpdateCount': 1, 'State': 1,
                   'Timestamp': int(msg_time.timestamp() * 1000)}
            # 消息数控制
            n = n + 1
            # 消息体转为json格式
            send_msg = "[" + json.dumps(msg) + "]"
            print(str(n) + "====>" + send_msg)
            # 发送消息
            producer.send(topic, send_msg.encode())
            if num == 60:
                num = 0
            if n == 200000:
                break
            # time.sleep(0.002)
    except KafkaError as e:
        print(e)
    finally:
        producer.close()
        print('done')


if __name__ == '__main__':
    time_start = datetime.datetime.now().timestamp()
    print(time_start)
    p0 = multiprocessing.Process(target=test)
    p1 = multiprocessing.Process(target=test)
    p0.start()
    p1.start()
    # test()
    time_end = datetime.datetime.now().timestamp()
    print(time_end)
    print('耗时：' + str(time_end - time_start) + '秒')
