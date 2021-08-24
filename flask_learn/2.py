# author:丑牛
# datetime:2021/8/6 14:31
import requests
body = {
    'd1': 'hello',
    'd2': 'flask'
}
req = requests.post('http://127.0.0.1:9090/', json=body)
print(req)
