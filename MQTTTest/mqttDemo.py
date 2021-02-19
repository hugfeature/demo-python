# author:丑牛
# datetime:2020/12/29 14:48
import datetime
import json
from datetime import time
import random

import paho.mqtt.client as mqtt

from dateutil.relativedelta import relativedelta


# Connection success callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    client.subscribe('/zmj/test')


# Message receiving callback
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client('zmj3')

# Specify callback function
client.on_connect = on_connect
client.on_message = on_message

# Establish a connection
client.username_pw_set('zmj3', 'zmj123456')
client.connect('192.168.175.228', 1883, 60)
client.loop_start()
# Publish a message
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
       'DeviceCode': label[8:24], 'DataID': label[24:30], 'UpdateCount': 2, 'State': 1,
       'Timestamp': int(msg_time.timestamp() * 1000)}
send_msg = "[" + json.dumps(msg, ensure_ascii=False) + "]"
client.publish('/zmj/test', payload=send_msg, qos=0)
# client.loop_forever()

