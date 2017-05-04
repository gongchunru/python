#encoding:utf-8

# this one is linke your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1,arg2)


def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothin!"

print_one("One")
print_none()
print_two("zed","Shaw")
print_two_again("zed","Ahaw")