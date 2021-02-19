# author:丑牛
# datetime:2020/5/17 11:03
import struct

import happybase

from HbaseTest import hbase
from PostgresqlTest import postgres

if __name__ == "__main__":
    host = "192.168.175.230"
    # row_key = b'2:12'
    table_name = '37082600014020001002:event-202109'
    # host1 = '127.0.0.1'
    # db_password = 'wzx670905'
    # connect_postgres = postgres.connect(host1, db_password)
    keys = hbase.scan_table(host, table_name)
    for key, data in keys:
        print(key.decode("utf-8"))
        # print(data)
        # 读取event表
        for k, value in data.items():
            print(value[0].decode("utf-8"))
        # if 'v' in key.decode("utf-8"):
        #     print(key.decode("utf-8"))
        #     print(data)
            # for k, v in data.items():
            #     k_str = k.decode("utf-8")
            #     print(k_str)
            #     if k_str != 'v:+':
            #         print(k_str)
            #         if k_str == 'a:c':
            #             value = int.from_bytes(v[0], 'big')
            #         else:
            #             value = struct.unpack('!d', v[0])[0]
            #         print(value)
            #         store_time = v[1]
            #         print("存储时间为:" + str(store_time))
                    # insert_sql = "INSERT INTO time_hbase(time_end) VALUES (" + str(store_time) + ")"
                    # postgres.exec_table(connect_postgres, insert_sql)
                    # connect_postgres.commit()
    count = hbase.count_row(host, table_name)
    print("共有：" + str(count))
