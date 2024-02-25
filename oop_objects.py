class Main_calc:
    def __init__(self):
        print('welcome in our calculator')

    def sum(self,x,y):
        print(x+y)  
        
class Test:
    def sum(self,x,y):
        print('In Test')
        print(x+y) 

class Calculator(Test):
    def mul(self,x,y):
        print(x*y) 

class Sicentific(calculator , main_calc):
    def power(self,x,y):
        return x**y

x = Sicentific()
x.sum(5,6)
x.mul(2,3)           