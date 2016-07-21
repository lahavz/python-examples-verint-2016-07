"""
Fill the code to print the result
"""

class Summer(object):
    def __init__(self):
        self._temp = []

    def add(self, *args):
        for x in args:
            if (type(x) is int): self._temp.append(x)

    def total(self):
        sum = 0
        for x in self._temp:
            sum += x
        return sum


#Original Code
s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
print s.total()

# should print 50
print t.total()
