# author:丑牛
# datetime:2021/3/16 14:42
from paho.mqtt import client as mqtt_client

from MQTTTest.mqttDemo import on_message

if __name__ == '__main__':
    # 连接MQTT服务器
    def on_connet(client, userdata, flags, rc_connect):
        print("Connected with result code:" + str(rc_connect))
        client.subscribe('/zmj/test')

    # 消息处理函数
    def on_message_come(lient, userdata, msg):
        print(msg.topic + " " + ":" + str(msg.payload))
    client = mqtt_client.Client('whl')
    client.username_pw_set('whl', 'whl')
    client.on_connect = on_connet
    client.on_message = on_message
    client.connect("192.168.175.228", 1883, 60)
    client.loop_forever()

    # subscribe 消息
    # def on_subscribe():
    #     mqtt_client.Client.subscribe("/zmj/test", 1)
    #     mqtt_client.Client.on_message = on_message_come  # 消息到来处理函数

