"""
function that gets two paramets and check validity. (str and number)
"""
from types import *



def func(*args):
    parameters = { 'integers' : 0, 'strings' : 0 }

    for x in args:
        if type(x) is int: parameters['integers'] += 1
        if type(x) is str: parameters['strings'] += 1
        
    if (parameters['strings'] == 1) and (parameters['integers'] == 1):
        print parameters
        print 'ok'
    else:
        print parameters
        print 'Not ok'
        raise Exception("Wrong parameters")







    

func(5,"lahav")
func(5,"ksks","lahav")
 


            
    
