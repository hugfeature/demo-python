# author:丑牛
# datetime:2021/4/15 13:27
import json

msg_num = 20
num = 1
for i in range(msg_num):
    code_num = "26000101000100010001000101" + "%04d" % num
    code_num1 = "26000101000100010001000101" + "%04d" % (num + 1)
    code_num2 = "26000101000100010001000101" + "%04d" % (num + 2)
    info = {"ns": "test_KAFKA",
            "label":
                {
                    "code": code_num,
                    "name": "电机功率",
                    "dataType": "01",
                    "unit": "W",
                    "timestamp": "latest",
                    "frequency": 0,
                    "description": "计算电机功率"
                },
            "inputs":
                [
                    {
                        "code": code_num1,
                        "name": "电机电压",
                        "value": "current",
                        "description": "电压"
                    },
                    {
                        "code": code_num2,
                        "name": "电机电流",
                        "value": "current",
                        "description": "电流"
                    }
                ],
            "functionName": "power",
            "script": "function power (num1, num2) {return num1 * num2;}"
            }
    msg = json.dumps(info, ensure_ascii=False)
    print(msg + ",")
    num = num + 3
