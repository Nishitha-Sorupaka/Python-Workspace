#DefaultParamConstEx1.py
class Test:
    def __init__(self,a=1,b=2): # Default Constructor
        print("i am from Constructor")
        self.a=a
        self.b=b
        print("-"*50)
        print("Value of a= ",self.a)
        print("Value of b= ", self.b)
        print("-" * 50)

#main program
t1=Test() # Object Creation---PVM calls Default Constructor
t2=Test(10,20) # Object Creation---PVM calls Parameterized Constructor
t3=Test(100) # Object Creation---PVM calls Parameterized Constructor
t4=Test(b=200) # Object Creation---PVM calls Parameterized Constructor
t5=Test(b=100,a=200) # Object Creation---PVM calls Parameterized Constructor