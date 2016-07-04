print "Exercise # 1 "

num = 0
for i in range(10):
    print "Number # %d:" % (i+1)
    tmpnum = int(raw_input())
    if tmpnum >= num:
        num = tmpnum


print "Highest Number: %d" % num
