"""
Using List comprehension and range functions - find the a-z letters
"""
 
x = [chr(x) for x in range(256)]

print [chr(j) for j in range(x.index('a'),x.index('z')+1)]


            
    
