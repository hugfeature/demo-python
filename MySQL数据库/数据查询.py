# author:丑牛
# datetime:2020/10/14 9:03
# author:丑牛
# datetime:2020/10/14 8:43
import pymysql

ip = "192.168.175.216"
user = "root"
passwd = "123456"
testDB = "data_model_analysis"
db = pymysql.connect(ip, user, passwd, testDB)
cursor = db.cursor()
sql = "select * from algorithm_choreography_management "
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.commit()
except:
    db.rollback()
finally:
    db.close()
