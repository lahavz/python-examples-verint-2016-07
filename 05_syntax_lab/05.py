from random import randint

print "Exercise # 5"

"""Original Block
while True:
    num = randint(1, 1000000)
    print "Number is %d" % (num)
    if num % 7 == 0:
        if num % 13 == 0:
            if num % 15 == 0:
                print "Number %d is divided by 7,13,15" % (num)
                break
            else:
                print "Number %d is NOT divided by 15" % (num)
        else:
                print "Number %d is NOT divided by 13" % (num)
    else:
                print "Number %d is NOT divided by 7" % (num)
"""

#New Block (fix with less indentation)
while True:
    num = randint(1, 1000000)
    print "Number is %d" % (num)
    if num % 7 > 0:
        continue
    elif num % 13 > 0:
        continue
    elif num % 15 > 0:
        continue
    else:
        print "Number %d is divided by 7,13,15" % (num)
        break
                
        

