__author__ = 'Raphael'

class CoucouGamin:
    "Hello world"
    status=0
    def fct(self):
        return "fonction"

    def fct2(self):
        print("in fct2")



x = CoucouGamin()
print(x.__doc__)
print(x.status)
x.status=1
print(x.status)
mystring=x.fct()
print(mystring)
x.fct2()