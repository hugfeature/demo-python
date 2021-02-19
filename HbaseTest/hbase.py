# author:丑牛
# datetime:2020/5/17 8:41
import happybase


def connect(host):
    """
    建立连接
    """
    connection = happybase.Connection(host=host, protocol='compact', transport='framed')
    connection.open()
    return connection


def tables(host):
    """
    获取所有的表
    """
    conn = connect(host)
    table_list = conn.tables()
    return table_list


def scan_table_row(host, table_name, row_key):
    """
    行键搜索
    :param host:
    :param table_name:
    :param row_key: b'row-key'
    :return:
    """
    conn = connect(host)
    table = conn.table(table_name)
    for key, data in table.scan(row_prefix=row_key):
        print(key)
        print(data)
        return key, data


def put_table(host, table_name, row_key, family_quail1, value):
    """
    :param host:
    :param table_name:
    :param row_key: b'row-key'
    :param family_quail1: b'family:quail1'
    :param value: b'value2'
    :return:
    """
    conn = connect(host)
    table = conn.table(table_name)
    table.put(row_key, {family_quail1: value})
    row = table.row(row_key)
    print(row[family_quail1])
    # prints row key and data for each row
    for key, data in table.rows([b'row-key-1', b'row-key-2']):
        print(key, data)


def scan_table(host, table_name):
    """
    整表遍历
    :param host:
    :param table_name:
    :return:
    """
    conn = connect(host)
    table = conn.table(table_name)
    keys = table.scan(include_timestamp=True, sorted_columns=True, reverse=True)
    return keys


def delete_row(host, table_name, row_key):
    """
    删除某行
    :param host:
    :param table_name:
    :param row_key:
    :return:
    """
    conn = connect(host)
    table = conn.table(table_name)
    table.delete(row_key)


def delete_table(host, table_name):
    """
    删除整个表，先disable，然后delete
    :param host:
    :param table_name:
    :return:
    """
    conn = connect(host)
    conn.disable_table(table_name)
    conn.delete_table(table_name)


def count_row(host, table_name):
    conn = connect(host)
    table = conn.table(table_name)
    keys = table.scan()
    row_count = 0
    for key in keys:
        row_count += 1
    return row_count


def get_value(host, table_name):
    conn = connect(host)
    table = conn.table(table_name)
    keys = table.scan()
    row_count = 0
    for key in keys:
        row_count += 1
    return row_count

