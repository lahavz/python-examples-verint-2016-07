"""
Using List comprehension and range functions - find the a-z letters
"""
 
x = [chr(x) for x in range(256)]

letters = [chr(j) for j in range(x.index('a'),x.index('z')+1)]

print [a+b+c for a in letters for b in letters for c in letters]



            
    
