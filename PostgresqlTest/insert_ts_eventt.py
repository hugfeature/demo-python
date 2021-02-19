# author:丑牛
# datetime:2020/7/21 8:43
import datetime
import random

from PostgresqlTest import postgres

if __name__ == "__main__":
    host = '192.168.175.196'
    db_password = 'postgres'
    connet = postgres.connect(host, db_password)
    num = 0
    while True:
        topic_list = ["260001", "260002", "260003", "260004", "260005"]
        topic = random.choice(topic_list)
        label = "010001000100010001" + "%06d" % num
        value = random.randint(0, 9999)
        timestamp = 1594283310597
        message_list = ["支柱压力过低预警 :支架号[3, 30, 34, 45, 71, 76, 81, 83, 85]",
                        "支架跳架预警: 跳架时间戳：1594364297489 跳架支架号：115",
                        "两端头使用记忆截割预警",
                        "乳化液浓度跳动幅度超过4%预警",
                        "两端头使用自动跟机预警",
                        "泵箱液位低于300mm预警"]
        message = random.choice(message_list)
        state = 1
        rule = 12
        starttime = datetime.datetime.now().timestamp() * 1000
        endtime = 1594283310597 + 1
        insert_sql = "insert into ts_event values" \
                     " ( " + '\'' + topic + '\'' + "," + '\'' + label + '\'' + "," + '\'' + \
                     str(value) + '\'' + "," + str(timestamp) + "," + '\'' + message + '\'' + "," + str(state) + "," \
                     + '\'' + str(rule) + '\'' + "," + str(starttime) + "," + str(endtime) + ")"
        postgres.exec_table(connet, insert_sql)
        connet.commit()
        num = num + 1
        if num == 10000:
            break
    connet.close()
