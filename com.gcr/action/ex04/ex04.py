# encoding=utf8

"""
任一个英文的纯文本文件，统计其中的单词出现的个数。
"""

import re

def count_words(filePath):
    with open(filePath) as file:
        text = file.read()
        words = re.findall(r'[a-zA-Z]+',text)
        count = len(words)
    return count

print(count_words('text.txt'))
