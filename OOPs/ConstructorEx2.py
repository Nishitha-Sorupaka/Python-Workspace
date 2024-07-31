#ConstructorEx1.py
class Employee:
    def __init__(self,eno,ename): # Default Constructor
        print("i am from Constructor")
        self.eno=eno
        self.ename=ename

#main program
e1=Employee(100,"Rossum") # Object Creation----PVM calls Constructor
print("Content of e1=",e1.__dict__) # {}
e2=Employee(200,"Travis") # Object Creation----PVM calls Constructor
print("Content of e2=",e2.__dict__) # {......}