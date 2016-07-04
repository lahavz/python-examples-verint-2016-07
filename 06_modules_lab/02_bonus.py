import sys

num1 = int(0)
num2 = int(0)

try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print "Sum is %d" % (num1+num2)
except:
    print "Problematic Agruments"
