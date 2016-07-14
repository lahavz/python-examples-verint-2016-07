"""
Two fucntions: 1st is sum , 2nd is multiply.
"""

from types import *

def sum(*args):
    res = 0
    for x in args:
        if type(x) is int: res += x
    return res

def multiply(*args):
    res = 1
    for x in args:
        if type(x) is int: res *= x
    return res


print sum(5,6,7,"lahav")
print multiply(5,6,7,"lahav")
 


            
    
