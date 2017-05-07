# encoding=utf8

# 并将激活码保存到 MySQL 关系型数据库中。
import uuid
import pymysql


# 生成 num 个验证码，每个长度为length，可设置默认长度
def create_num(num, length=16):
    result = []
    while num > 0:
        uuid_id = uuid.uuid4()
        # 删去字符串中的'-',取出前length 个字符
        temp = str(uuid_id).replace('-', '')[:length]
        if temp not in result:
            result.append(temp)
            num -= 1

    return result


# 保存到MySQL数据库
def save_to_mysql(code):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password=None,
        db='test'
    )

    try:
        with conn.cursor() as cursor:

