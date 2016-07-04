from random import randint

print "Exercise # 6"

num1 = randint(1, 10)
num2 = randint(1, 10)

print "Random numbers are: %d , %d" % (num1,num2)

i=int(1)

while True:
    if ((i*num1) % num2) == 0:
        print "Smallest multiply is %d" % (i*num1)
        break
    else:
        i = i+1
        


