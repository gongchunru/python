#encoding:utf-8
from sys import argv
script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0) #每次运行该行的时候，就回到了初始位置

#readline() 函数返回的内容中包含文件本来就有的 \n，而 print 在打印时又会添加一个 \n，这样一来就会多出一个空行了
#解决方法是在 print 语句结尾加一个逗号 ,，这样 print 就 不会把它自己的 \n 打印出来了。
def print_a_line(line_count, f):
    print line_count, f.readline(),


current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a type."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line+1
print_a_line(current_line, current_file)

current_line = current_line+1
print_a_line(current_line,current_file)
