#encoding=utf8

# 统计文本文件中单词的次数
# todo collections.Counter

import os
import re

def get_file_list(path):
    """
    遍历文件目录，返回文件路径列表
    :param path:
    :return:
    """

    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith('txt'):
                file_list.append(os.path.join(root,file))

    return file_list

def find_keyword(file_path):
    """
    根据文件路径，找到文件中的关键字
    :param file_path:
    :return:
    """

    keywords = {'other'}
    file_name = os.path.basename(file_path)
    with open(file_path,encoding='utf-8') as file:
        text = file.read()
        word_list = re.findall(r'[a-zA-Z]+', text.lower())
        for word in word_list:
            if word in keywords:
                keywords[word] += 1
            else:
                keywords[word] = 1

        keywords_sorted = sorted(keywords.items(), key=lambda  d: d[1])
    return file_name, keywords_sorted

for path in get_file_list(os.getcwd()):
    name, results = find_keyword(path)
    print(u"在 %s 文件中，%s 为关键词，共出现了%s次" % (name, results[-1][0], results[-1][1]))
