# author:丑牛
# datetime:2020/5/25 8:55
import psycopg2


def connect(host, db_password):
    # conn = psycopg2.connect(database="LongWall_Automation_Edge", user="postgres", password=db_password, host=host,
    #                         port="5432")
    conn = psycopg2.connect(user="postgres", password=db_password, host=host, port="5432")
    print("Opened database successfully")
    return conn


def exec_table(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    print("SQl  execute successfully")
