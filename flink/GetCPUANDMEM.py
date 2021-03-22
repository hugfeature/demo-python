# author:丑牛
# datetime:2020/5/22 19:12
import requests
from PostgresqlTest import postgres
import time


def inner_get_avg(url):
    response = requests.get(url)
    # print(response.text)
    get_avg = response.json()[0]["avg"]
    print(get_avg)
    response.close()
    return get_avg


if __name__ == '__main__':
    cpu_url = 'http://cdh-1:8088/proxy/application_1615272298938_0050/taskmanagers/metrics?get=Status.JVM.CPU.Load'
    mem_url = 'http://cdh-1:8088/proxy/application_1615272298938_0050/taskmanagers/metrics?get=Status.JVM.Memory.Heap.Used'
    host = '127.0.0.1'
    db_password = 'wzx670905'
    connect = postgres.connect(host, db_password)
    # f = open("value.txt", "w")
    n = 0
    while True:
        cpu_avg_value = inner_get_avg(cpu_url)
        mem_avg_value = inner_get_avg(mem_url)
        # f.write(str(cpu_avg_value) + "\t" + str(mem_avg_value) + "\n")
        insert_sql = "INSERT INTO use(cpu, mem) VALUES (" + str(cpu_avg_value) + "," + str(mem_avg_value) + ")"
        postgres.exec_table(connect, insert_sql)
        connect.commit()
        time.sleep(1)
        n = n + 1
        if n == 60 * 5:
            break
    connect.close()
