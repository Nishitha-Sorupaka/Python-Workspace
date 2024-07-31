#Non-Const.ex.py
class Employee:
    def getEmpData(self):
        self.eno=10
        self.ename="Rossum"

#main program
e1=Employee() # Object Creation
print("Content of e1=",e1.__dict__) # {}
e1.getEmpData() # we are calling the method explicitly
print("Content of e1=",e1.__dict__) # {......}