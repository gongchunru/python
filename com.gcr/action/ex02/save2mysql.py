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
        password='123456',
        db='test'
    )

    try:
        with conn.cursor() as cursor:
            # create a new record

            sql = "INSERT INTO codes(code) VALUES  (%s)"
            cursor.execute(sql, code)

            # connection is not autocommit by default. So you must commit to save
            # your changes.

            conn.commit()

        # 查询一条数据
        with conn.cursor() as cursor:
            # read a single record
            sql = "SELECT `code` FROM `codes` WHERE  code = %s"
            cursor.execute(sql, code)
            result = cursor.fetchone()
            print(result)

    finally:
        conn.close()

# 循环保存数据
for code in create_num(200):
    save_to_mysql(code)

