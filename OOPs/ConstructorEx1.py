#ConstructorEx1.py
class Employee:
    def __init__(self): # Default Constructor
        print("i am from Constructor")
        self.eno=10
        self.ename="Rossum"

#main program
e1=Employee() # Object Creation----PVM calls Constructor
print("Content of e1=",e1.__dict__) # {}
e2=Employee() # Object Creation----PVM calls Constructor
print("Content of e2=",e2.__dict__) # {......}