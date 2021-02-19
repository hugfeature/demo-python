# author:丑牛
# datetime:2020/9/11 11:28
import pandas
from PostgresqlTest import postgres

host = '127.0.0.1'
db_password = 'wzx670905'
connet = postgres.connect(host, db_password)
file_path = 'C:\\Users\\wangzhaoxian\\Desktop\\ts_170000_20200901_20200930.csv'
df = pandas.read_csv(file_path, names=['label', 'value', 'createtime', 'update', 'state', 'storetime'])
print(len(df['storetime']))
lenth = int(len(df['storetime'])) - 1
i = 0
while True:
    starttime = df['createtime'][i]
    endtime = df['storetime'][i]
    i = i + 1
    print(starttime, endtime)
    time_use = endtime - starttime
    insert_sql = "INSERT INTO time(time_end, time_start, time_use) VALUES " \
                 "(" + str(endtime) + "," + str(starttime) + "," + str(time_use) + ")"
    postgres.exec_table(connet, insert_sql)
    connet.commit()
    if i > lenth:
        break