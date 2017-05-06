#encoding:utf-8
#作为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？

# 使用python 的uuid模块，uuid有4个算法，这里采用uuid4
import uuid
def generate_acctivation_code(count):
    code_list = []
    for i in xrange(count):
        #删除字符串中的-
        code = str(uuid.uuid4()).replace('-','').upper()
        #uuid4的算法有一定的重复概率，所以下面做了判断
        if not code in code_list:
            code_list.append(code)

    return code_list

#设置默认的长度，
def  generate_acctivation_code2(count,length=6):
    code_list = []
    while count > 0:
        uuid_id = uuid.uuid1()
        #删除字符串中的'-' 取出前length个字符
        temp = str(uuid_id).replace('-','')[:length]
        if temp not in code_list:
            code_list.append(temp)
            count -= 1

    return code_list


# if __name__ == '__main__':
#     code_list = generate_acctivation_code(200)
#     for code in code_list:
#         print code

print generate_acctivation_code2(200)