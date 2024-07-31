#Program for demonstrating Class Level Methods
#ClassLevelMethodEx3.py
class Employee:
    @classmethod
    def getCompName(cls): # Class Level Method
        Employee.cname="NS"
        Employee.addr="HYD"   # here city,cname are called Class Level Data Members

    def getEmpDetails(self): # Instance Method
        self.eno=int(input("Enter Employee Number: "))
        self.ename=input("Enter Employee Name: ")
    def dispEmpDetails(self): # Instance Method
        Employee.getCompName() # Calling Class Level Method w.r.t Class Name
        print("Employee Number: ",self.eno)
        print("Employee Name: ",self.ename)
        print("Employee Company Name: ",Employee.cname)
        print("Employee City: ",Employee.addr)

#main program

e1=Employee()
e1.getEmpDetails()
e1.dispEmpDetails()
print("-"*50)
e2=Employee()
e2.getEmpDetails()
e2.dispEmpDetails()