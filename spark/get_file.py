# author:丑牛
# datetime:2020/7/29 10:52
import os
from pyspark import SparkContext, SparkConf
from pyspark.sql.session import SparkSession
# 在服务器运行需指定运行环境
# os.environ["PYSPARK_PYTHON"]="/usr/bin/python3"
from PostgresqlTest import postgres

conf = SparkConf().setAppName("test_parquet")
sc = SparkContext("local", "test", conf=conf)
# sc = SparkContext("spark://192.168.175.230:7337", "test", conf=conf)
spark = SparkSession(sc)
remote_file_path = 'hdfs://192.168.175.231:8020/test/parquet/ns=37082600014020001005/d=20200828'
df = spark.read.parquet(remote_file_path)
df.show(10, truncate=False)
host = '127.0.0.1'
db_password = 'wzx670905'
# connect = postgres.connect(host, db_password)
df1 = df.toPandas()
# for store_time in df1['dqsj']:
#     print(store_time)
#     insert_sql = "INSERT INTO time_hbase(time_end) VALUES (" + str(store_time) + ")"
#     postgres.exec_table(connect, insert_sql)
#     connect.commit()
print(df.count())
# connect.close()
