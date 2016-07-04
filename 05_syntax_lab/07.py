from random import randint

print "Exercise # 7"

num = randint(1, 100)

mistake_ratio = randint(5, 10)
i = int(0)

print "Number is: %d " % (num)


while True:
    print "What is your Guess?"
    guess = int(raw_input())

    if guess == num:
        print "Its a Hit - Well Done!!!"
        break
    if i < mistake_ratio: 
        if guess > num:
            print "Try smaller number"
        else:
            print "Try higher number"
            
    if i == mistake_ratio: 
        if guess > num:
            print "Try higher number"
        else:
            print "Try smaller number"
        i = int(-1)

    i=i+1
    
    
            
    
