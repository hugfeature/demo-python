# author:丑牛
# datetime:2020/8/24 20:26
import datetime
import json
import random

from paho.mqtt import client as mqtt_client
import time

if __name__ == '__main__':
    def on_connet(userdata, flags, rc_connect):
        print("Connetct returned" + str(rc_connect))


    def on_publish(rc_publis):
        print('publish success' + str(rc_publis))

    # 延迟发送
    # topic = '$delayed/300/zaokuang/fucun/222'
    topic = 'zaokuang/fucun/222'
    client_id = 'wzx'
    client = mqtt_client.Client(client_id)
    client.username_pw_set('wzx', '123456')
    client.connect("192.168.175.196", 1883, 60)
    client.on_connect = on_connet
    client.loop_start()
    n = 0
    while True:
        timeStamp = int(time.time() * 1000)
        data_list = ["电液控.方向", "电液控.煤机位置", "电液控.跟机状态", "电液控.急停架号", "电液控.闭锁架号",
                     "电液控.支架集.123.前溜行程", "电液控.支架集.123.立柱压力", "采煤机.通讯", "采煤机.远控",
                     "采煤机.手动割煤", "采煤机.记忆割煤", "采煤机.学习割煤", "采煤机.干预割煤", "采煤机.牵引上电",
                     "采煤机.牵引状态", "采煤机.加速状态", "采煤机.加速状态", "采煤机.位置米", "采煤机.位置架", "采煤机.牵引速度",
                     "采煤机.倾角", "采煤机.左滚筒.状态", "采煤机.左滚筒.电流", "采煤机.左滚筒.电压", "采煤机.左滚筒.温度",
                     "采煤机.左滚筒.高度", "采煤机.左滚筒.卧底", "采煤机.左滚筒.上升", "采煤机.左滚筒.下降", "采煤机.右滚筒.状态",
                     "采煤机.右滚筒.电流", "采煤机.右滚筒.电压", "采煤机.右滚筒.温度",
                     "采煤机.右滚筒.高度", "采煤机.右滚筒.卧底", "采煤机.右滚筒.上升", "采煤机.右滚筒.下降", "采煤机.左牵引.状态",
                     "采煤机.左牵引.状态", "采煤机.左牵引.电流", "采煤机.左牵引.电压", "采煤机.左牵引.温度",
                     "采煤机.右牵引.状态", "采煤机.右牵引.电流", "采煤机.右牵引.电压", "采煤机.右牵引.温度",
                     "采煤机.主泵.状态", "采煤机.主泵.电流", "采煤机.主泵.电压", "采煤机.主泵.温度",
                     "三机.通讯", "三机.远控", "三机.模式", "三机.破碎机.运行", "三机.破碎机.电流", "三机.转载机.运行", "三机.转载机.电流",
                     "三机.前部运输机.机头水平部.电流", "三机.前部运输机.机尾部.运行", "三机.前部运输机.机尾部.电流", "泵站.通讯", "泵站.远控", "泵站.模式", "泵站.乳化泵闭锁",
                     "泵站.喷雾泵闭锁", "泵站.液箱.液位", "泵站.液箱.浓度", "泵站.液箱.温度", "泵站.油箱.油位", "泵站.过滤站.进口压力", "泵站.过滤站.出口压力",
                     "泵站.水箱1.水位", "泵站.水箱2.水位", "泵站.液泵1.运行"]
        data = random.choice(data_list)
        if data == "电液控.方向":
            value_list = [1, 1.0, 2, 1.0]
            value = random.choice(value_list)
        else:
            value = random.randrange(1, 1000)
        msg = {"DataPoint": random.choice(data_list), "Value": str(value), "Timestamp": timeStamp}
        send_msg = "[" + json.dumps(msg, ensure_ascii=False) + "]"
        print(send_msg)
        n = n + 1
        print(n)
        rc, mid = client.publish(topic, payload=send_msg, qos=1)
        on_publish(rc)
        if n == 400000:
            break
        # time.sleep(1)
    print(datetime.datetime.now())
