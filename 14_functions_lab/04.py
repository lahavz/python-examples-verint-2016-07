"""
function return words greather than length
"""
from types import *



def func(length,*args):
    res = []
    for x in args:
        if (type(x) is str) and (len(x) >= length): res.append(x)
    print res

func(2,"lahav","l","lala","bb",5)
func(5,"ksks","lahav")
     


            
    
