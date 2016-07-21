"""
Fill the code to print the result
"""

class Widget(object):

    widget_list = []
    
    def __init__(self,name = ""):
        self._name = name
        self._dependency = []

    def add_dependency(self, *args):
        for x in args:
            self._dependency.append(x)



    def create(self):     
        if (len(self._dependency) > 0):
            for a in self._dependency:
                if a._name not in Widget.widget_list:
                    a.create()
        else:
            if self._name not in Widget.widget_list:
               Widget.widget_list.append(self._name)

        if self._name not in Widget.widget_list:
               Widget.widget_list.append(self._name)
   



    def build(self):
        for x in self._dependency:
            x.create()

        for y in Widget.widget_list:
            print y + ',',



#Original Code

luke    = Widget("Luke")
hansolo = Widget("Han Solo")
leia    = Widget("Leia")
yoda    = Widget("Yoda")
padme   = Widget("Padme Amidala")
anakin  = Widget("Anakin Skywalker")
obi     = Widget("Obi-Wan")
darth   = Widget("Darth Vader")
_all    = Widget("All")


luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()


# code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda, Luke, Obi-Wan, Darth Vader
# (can print with newlines in between modules)
