# author:丑牛
# datetime:2020/5/18 10:23
import datetime

import multiprocessing

from MQTTTest import mqtt_edge_msg

if __name__ == "__main__":
    time_start = datetime.datetime.now().timestamp()
    print(time_start)
    mqtt_hosts = '192.168.175.228'
    client = "wzxtest"
    topic = "pingmeijituan/shoushanyikuang/zstest"
    pool = multiprocessing.Pool(25)
    pool.apply_async(func=mqtt_edge_msg.send_edge, args=(client, mqtt_hosts, topic))
    pool.close()
    pool.join()
    print("The number of CPU is %d:" % (multiprocessing.cpu_count()))     # 打印CPU核数
    for p in multiprocessing.active_children():         # 循环打印子进程的名称和pid
        print("子进程名称：%s，子进程pid：%d" % (p.name, p.pid))
    print("ending....")
    time_end = datetime.datetime.now().timestamp()
    print('耗时：' + str(time_end - time_start) + '秒')
