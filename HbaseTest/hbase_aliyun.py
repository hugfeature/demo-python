# author:丑牛
# datetime:2020/9/22 15:28
import happybase
#连接habse(服务端需打开habse thrift)
host = ""
connection = happybase.Connection(host=host, protocol='compact', transport='framed')
connection.open()
# 创建namespace

#向TS_CONVERT_META插入数据
