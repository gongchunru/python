# encoding: utf-8
#使用 argv 和 raw_input 来从用户获取信息，从而之大哪些文件改被处理

from sys import argv #sys是一个代码库，从库中去除argv 这个功能来被我使用。

script, filename = argv #使用argv获取文件名

txt = open(filename) #打开文件

print "Here's your file %r:" % filename
print txt.read()

txt.close()

print "Type the filename again:"

file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()
