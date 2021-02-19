# author:丑牛
# datetime:2020/8/4 9:58
import time

import requests
from PostgresqlTest import postgres


def inner_get_avg(url):
    response = requests.get(url)
    # print(response.text)
    cpu = response.json()[1]["totalCores"]
    mem = response.json()[1]["memoryMetrics"]["totalOnHeapStorageMemory"]
    response.close()
    return cpu, mem


if __name__ == '__main__':
    spark_url = 'http://192.168.175.230:18088/api/v1/applications/application_1594110503511_0098/executors'
    host = '127.0.0.1'
    db_password = 'wzx670905'
    connect = postgres.connect(host, db_password)
    inner_get_avg(spark_url)
    n = 0
    while True:
        cpu_use, mem_use = inner_get_avg(spark_url)
        insert_sql = "INSERT INTO use(cpu, mem) VALUES (" + str(cpu_use) + "," + str(mem_use) + ")"
        postgres.exec_table(connect, insert_sql)
        connect.commit()
        time.sleep(1)
        n = n + 1
        if n == 60 * 5:
            break
    connect.close()
