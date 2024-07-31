#Program for demonstrating Destructors
#non-destex1.py
class Employee:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename
        print("-"*50)
        print("Employee Number: {}".format(self.eno))
        print("Employee Name: {}".format(self.ename))
        print("-" * 50)

#main program
print("Program execution started")
e1=Employee(eno=10,ename="Rossum")
e2=Employee(eno=20,ename="Travis")
print("Program execution ended")

