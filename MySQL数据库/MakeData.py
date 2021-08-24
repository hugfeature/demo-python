# author:丑牛
# datetime:2021/5/28 15:27
import random

import pymysql
import datetime
from dateutil.relativedelta import relativedelta

ip = "39.98.77.89"
user = "root"
passwd = "ZMJ@YYDK.67891289"
testDB = "timeseries_manage"
port = 13306
db = pymysql.connect(host=ip, port=port, user=user, password=passwd, database=testDB)
cursor = db.cursor()
result_list = []
seclect_sql = "select a.name_space,b.org_code,concat(substr(a.name_space,1,3),'000') as province,b.org_name from t_namespace_org a join t_namespace_org b on a.org_code = b.org_parent_code where a.org_parent_code =0; "
try:
    cursor.execute(seclect_sql)
    results = cursor.fetchall()
    for result in results:
        result_list.append(result[0])
    print(result_list)
    # grade = random.uniform(0, 100)
    # namespace = random.choice(result_list)
    # print(namespace)
    agg_type_list = [1, 2, 3]
    # agg_type = random.choice(agg_type_list)
    # province = namespace[:3] + "000"
    # print(province)
    # wokeface = namespace[14:] + "0001"
    # print(wokeface)
    # time = datetime.datetime.now() - relativedelta(days=29)
    # print(time.date())
    n = 0
    id = 1
    while True:
        namespace = random.choice(result_list)
        province = namespace[:3] + "000"
        wokeface = namespace[14:] + "0001"
        time = datetime.datetime.now() - relativedelta(days=29) + relativedelta(days=n)
        agg_type = random.choice(agg_type_list)
        grade = random.uniform(0, 100)
        if agg_type == 1:
            sql = "INSERT INTO `timeseries_manage`.`t_workface_grade_day` (`id`, `agg_type`, `province`, `namespace`, `workface`, `date`, `grade`) VALUES " \
                   "(" + str(id) + "," + str(agg_type) + "," + "100000" + "," + "NULL" + "," + "NULL" + ",'" + str(time.date()) + "'," + str(grade) + ");"
            print(sql)
            cursor.execute(sql)
        if agg_type == 2:
            sql = "INSERT INTO `timeseries_manage`.`t_workface_grade_day` (`id`, `agg_type`, `province`, `namespace`, `workface`, `date`, `grade`) VALUES " \
                   "(" + str(id) + "," + str(agg_type) + "," + province + "," + namespace + "," + "NULL" + ",'" + str(time.date()) + "'," + str(grade) + ");"
            print(sql)
            cursor.execute(sql)
        if agg_type == 3:
            sql = "INSERT INTO `timeseries_manage`.`t_workface_grade_day` (`id`, `agg_type`, `province`, `namespace`, `workface`, `date`, `grade`) VALUES " \
                   "(" + str(id) + ","+ str(agg_type) + "," + province + ","+ namespace + "," + wokeface + ",'" + str(time.date()) + "'," + str(grade) + ");"
            print(sql)
            cursor.execute(sql)
        db.commit()
        n += 1
        if n == 29:
            n = 0
        id += 1
        if id == 3000:
            break
except:
    db.rollback()
finally:
    db.close()


