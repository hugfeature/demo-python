# author:丑牛
# datetime:2021/7/19 14:55
# 利用flask编写一个简单接口
import json

from flask import Flask,request

# 实例化一个web 服务对象
app = Flask(__name__)


# 创建方法处理请求
# 定义一个路由
@app.route('/')
def hello():
    return "hello flask"


# 构造post请求响应
@app.route('/post', methods=['post'])
def test_post():
    d1 = request.form['d1']
    d2 = request.form['d2']
    return "post chenggong"
# 处理
@app.route('/trade/pu', methods=['POST'])
def pur():
    res = json.loads(request.get_data())
    da1 = res['K值']
    return 'success'

if __name__ == '__main__':
    app.run('127.0.0.1', '9090')
