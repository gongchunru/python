print "input your Chinese name:"
s=raw_input("Pess enter to be continued..");
print "Your name is...:"+s;
l=len(s)
print "Length of your Chinese name is asc codes is:"+str(l);
a=unicode(s,"GBK")
l=len(a)
print "I'm sorry we should use unicode char! Characters number of your Chinese \name in unicode is:"+str(l);

