from random import randint

print "Exercise # 2"


for i in range(7):
    num = randint(1, 100)
    print "Number # %d is %d" % ((i+1),num)
    if num % 7 == 0:
        print "Booooommmmm"
        

