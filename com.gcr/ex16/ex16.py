#encoding: utf-8
# • close – 关闭文件。跟你编辑器的 文件->保存.. 一个意思。
# • read – 读取文件内容。你可以把结果赋给一个变量。
# • readline – 读取文本文件中的一行。
#   truncate – 清空文件，请小心使用该命令。
# • write(stuff) – 将stuff写入文件
from sys import argv

script, filename=argv

print "We're going to erase %r." % filename
print "If you don't want that , hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file" 
target = open(filename, 'w') #以只写模式打开。若文件存在，则会自动清空文件，然后重新创建；若文件不存在，则新建文件。使用这个模式必须要保证文件所在目录存在，文件可以不存在。该模式下不能使用read*()方法

print "Truncation the file. Goodbyd!"
target.truncate() #truncate（）这个函数跟文件指针位置无关。每次执行都是从文件开始处执行

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()




