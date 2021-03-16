# author:丑牛
# datetime:2020/8/24 20:26
import datetime
import json
import random

from dateutil.relativedelta import relativedelta
from paho.mqtt import client as mqtt_client

if __name__ == '__main__':
    # 连接MQTT服务器
    def on_connet(client, userdata, flags, rc_connect):
        print("Connected with result code:" + str(rc_connect))


    # 发送MQTT消息
    def on_publish(rc_publis):
        print('Publish with result code:' + str(rc_publis))


    # 延迟发送
    # topic = '$delayed/300/zaokuang/fucun/222'
    topic = '/zmj/test'
    # client_id = 'zmj2'
    client = mqtt_client.Client('zmj2')
    client.username_pw_set('', 'zmj123456')
    client.connect("192.168.175.228", 1883, 60)
    client.on_connect = on_connet
    client.loop_start()
    n = 0
    while True:
        msg_time = datetime.datetime.now() + relativedelta(years=1, months=1, days=0)
        value = random.randint(0, 9999)
        label_list = ['260001010001000100010001010001', '260001010001000100010002010001',
                      '260001010001000100010003010001', '260001010001000100010006010001',
                      '260001010001000100010004010001', '260001010001000100010005010001',
                      '260001010001000100010007010001', '260001010001000100010008010001',
                      '260001010001000100010009010001', '260002010000000000000000040001',
                      '260001010000000000000000040001', '260001040019000100010001010004',
                      '260001040019000100010001010002', '260001010000000000000000020003',
                      '260001010000000000000000040005', '260001020002000100010001050009']
        label = random.choice(label_list)
        msg = {'Value': value, 'SysCode': label[0:8], 'ChannelCode': "001001",
               'DeviceCode': label[8:24], 'DataID': label[24:30], 'UpdateCount': n, 'State': 1,
               'Timestamp': int(msg_time.timestamp() * 1000)}
        send_msg = "[" + json.dumps(msg, ensure_ascii=False) + "]"
        print(send_msg)
        n = n + 1
        print(n)
        rc, mid = client.publish(topic, payload=send_msg, qos=0)
        on_publish(rc)
        # if n == 2:
        #     break
        # time.sleep(1)
    # 保持连接
    # client.loop_forever()
