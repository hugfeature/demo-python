# author:丑牛
# datetime:2020/10/14 8:43
import pymysql

ip = "192.168.175.216"
user = "root"
passwd = "123456"
testDB = "data_model_analysis"
db = pymysql.connect(ip, user, passwd, testDB)
cursor = db.cursor()
num = 75001
while True:
    sql = "INSERT INTO `data_model_analysis`.`algorithm_choreography_management`(`id`, `name`, `filename`, `filepath`, `description`, `parameter`, `created_time`, `updated_time`) VALUES (" + \
          str(num) \
          + ", 'test2', NULL, NULL, '2', '{\"nodes\": [{\"id\": \"1\",\"type\": \"datatable\",\"datatable\": 1,\"dependencies\": []},{\"id\": \"2\",\"type\": \"algorithm\",\"algorithm\": 10,\"parameters\": null,\"dependencies\": [{\"node\": \"1\"}]},{\"id\": \"3\",\"type\": \"algorithm\",\"algorithm\": 15,\"parameters\": {\"colNames\": \"_c0\"},\"dependencies\": [{\"node\": \"2\"}]},{\"id\": \"4\",\"type\": \"algorithm\",\"algorithm\": 14,\"parameters\": null,\"output\": [{\"node\": \"5\"},{\"node\": \"6\"}],\"dependencies\": [{\"node\": \"3\"}]},{\"id\": \"5\",\"type\": \"algorithm\",\"algorithm\": 9,\"parameters\": {\"inputCols\": \"sepal_length,sepal_width,petal_length,petal_width\"},\"dependencies\": [{\"node\": \"4\"}]},{\"id\": \"6\",\"type\": \"algorithm\",\"algorithm\": 9,\"parameters\": {\"inputCols\": \"sepal_length,sepal_width,petal_length,petal_width\"},\"dependencies\": [{\"node\": \"4\"}]},{\"id\": \"7\",\"type\": \"algorithm\",\"algorithm\": 22,\"parameters\": {\"labelCol\": \"target\"},\"dependencies\": [{\"node\": \"5\"}]},{\"id\": \"8\",\"type\": \"algorithm\",\"algorithm\": 34,\"parameters\": {\"modelType\": \"LogisticRegressionModel\"},\"dependencies\": [{\"node\": \"7\"},{\"node\": \"6\"}]},{\"id\": \"9\",\"type\": \"algorithm\",\"algorithm\": 37,\"parameters\": {\"modelType\": \"LogisticRegressionModel\",\"labelCol\": \"target\"},\"dependencies\": [{\"node\": \"8\"}]},{\"id\": \"10\",\"type\": \"dataresult\",\"outputfile\": \"result\",\"dependencies\": [{\"node\": \"9\"}]}]\r\n}', NULL, NULL); "
    try:
        cursor.execute(sql)
        db.commit()
        num += 1
        if num == 75005:
            break
    except Exception as e:
        print(e)
        db.rollback()
        break
cursor.close()
db.close()
