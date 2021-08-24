# author:丑牛
# datetime:2021/5/28 16:53
# author:丑牛
# datetime:2021/5/28 15:27
import json
import random

import pymysql
import datetime

import requests
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
    # province = namespace[:3] + "000"
    # print(province)
    # wokeface = namespace[14:] + "0001"
    # print(wokeface)
    # time = datetime.datetime.now() - relativedelta(days=29)
    # print(time.date())
    n = 0
    id = 1
    req = requests.get('https://geo.datav.aliyun.com/areas_v2/bound/100000_full.json')
    req.encoding = 'utf-8'
    result = json.loads(req.text)
    print(result)
    while True:
        namespace = random.choice(result_list)
        province = namespace[:3] + "000"
        wokeface = namespace[14:] + "0001"
        longitude = random.uniform(0, 100)
        latitude = random.uniform(0, 100)
        time = datetime.datetime.now() - relativedelta(days=29) + relativedelta(days=n)
        grade = random.uniform(0, 100)
        sql = "INSERT INTO `timeseries_manage`.`t_workface_info` (`id`, `namespace`, `work_face_code`, `province`, `longitude`, `latitude`, `access_time`, `status`, `workface_offline_interval`) VALUES ( " \
              + str(id) + "," + namespace + "," + wokeface + "," + province + "," + longitude + "," + latitude + ",'" + str(time.date()) + "'," + "1" + "," + "10" + ");"
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


