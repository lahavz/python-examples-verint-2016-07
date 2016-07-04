from random import randint

print "Exercise # 3"

num = randint(1, 10000)
print "Number is %d" % (num)
sum = int(0)

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num / 10

print "Sum is %d" % (sum)

