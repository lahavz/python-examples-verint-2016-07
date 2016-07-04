

print "Exercise # 4"

array = []

while True:  
    line = raw_input()
    if len(line) <= int(0): break
    array.append(line)       



for i in range((len(array)-1), -1 , -1):
    print array[i]
 
