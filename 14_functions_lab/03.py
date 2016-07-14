"""
function sums the tenth numbers
"""
from types import *



def func(*args):
    res = 0
    for x in args:
        if (type(x) is int) and (int(x) >= 10): res += x / 10 % 10
    print res


    

func(55,"lahav",43)
func(5,"ksks","lahav")
 


            
    
