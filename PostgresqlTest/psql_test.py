# author:丑牛
# datetime:2020/5/25 9:03
from PostgresqlTest import postgres

if __name__ == "__main__":
    host = '192.168.175.198'
    db_password = 'postgres'
    connet = postgres.connect(host, db_password)
    create_sql = 'CREATE TABLE use_kafa ( cpu float8,mem float8)'
    drop_sql = 'drop table if exists  time_tsts;'
    insert_sql = 'insert into ts_event(topic, label, value, timestamp, message, state, rule, starttime, endtime) ' \
                 'values (?,?,?,?,?,?,?,?,?) '
    select_sql = 'select * from ts_event'
    postgres.exec_table(connet, select_sql)
    connet.commit()
    connet.close()
