#Program for demonstrating Class Level Methods
#ClassLevelMethodEx1.py
class Employee:

    @classmethod
    def getCompName(cls): # Class Level Method
        Employee.cname="IBM"
        Employee.addr="HYD"   # here city,cname are called Class Level Data Members

    def getEmpDetails(self): # Instance Method
        self.eno=int(input("Enter Employee Number: "))
        self.ename=input("Enter Employee Name: ")
    def dispEmpDetails(self): # Instance Method
        print("Employee Number: ",self.eno)
        print("Employee Name: ",self.ename)
        print("Employee Company Name: ",Employee.cname)
        print("Employee City: ",Employee.addr)



#main program
Employee.getCompName() #calling Class Level Method w.r.t Class Name
e1=Employee()
e1.getEmpDetails()
e1.dispEmpDetails()