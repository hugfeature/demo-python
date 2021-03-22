# author:丑牛
# datetime:2020/12/29 15:34
import datetime
import json
import random
import time

import paho.mqtt.client as mqtt
from dateutil.relativedelta import relativedelta


def on_connet(client, userdata, flags, rc_connect):
    """
    构建mqtt连接信息
    :param client:
    :param userdata:
    :param flags:
    :param rc_connect:
    :return:
    """
    print("Connected with result code:" + str(rc_connect))


def send(client, host, topic):
    """
    向MQTT的topic中发消息
    :param client:
    :param host:
    :param topic:
    :return:
    """
    client = mqtt.Client(client)
    # Specify callback function
    client.on_connect = on_connet
    client.username_pw_set('whl', 'whl')
    client.connect(host, 1883, 60)
    client.loop_start()
    n = 0
    #构建消息体并一直发送
    while True:
        # 一个月之前的当天
        # msg_time = datetime.datetime.now() + relativedelta(years=0, months=-1, days=0)
        # 当前时间
        msg_time = datetime.datetime.now()
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
        n = n + 1
        client.publish(topic, payload=send_msg, qos=0)
        time.sleep(0.001)
        # if n == 1:
        #     break
