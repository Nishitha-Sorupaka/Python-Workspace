#Program for demonstating Static Methods
#StaticMethodEx4.py
class Student:
    def getStudentData(self):
        self.sno=int(input("Enter Student Number: "))
        self.sname=input("Enter Student Name: ")
        self.marks=float(input("Enter Student Marks: "))

class Employee:
    def getEmployeeData(self):
        self.eno=int(input("Enter Employee Number: "))
        self.ename=input("Enter Employee Name: ")
class Teacher:
    def getTeacherData(self):
        self.tno=int(input("Enter Teacher ID: "))
        self.tname=input("Enter Teacher Name: ")
        self.subject=input("Enter Teacher Subject: ")
        self.exp=int(input("Enter Teacher Experience: "))
class Hyd:
    @staticmethod
    def dispData(obj,objinfo): # Static Method
        print("-"*50)
        print("Information about: {}".format(objinfo))
        print("-" * 50)
        for k,v in obj.__dict__.items():
            print("{}-->{}".format(k,v))
        print("-" * 50)

    @classmethod
    def dispInformation(cls,obj,objinfo):
        cls.dispData(obj,objinfo) #calling Static Method inside Class Method w.r.t cls

#main program
s=Student()
e=Employee()
t=Teacher()
print("-" * 50)
s.getStudentData()
print("-" * 50)
e.getEmployeeData()
print("-" * 50)
t.getTeacherData()
print("-" * 50)
Hyd.dispInformation(s,"Student") #calling Static Method w.r.t Object Name by passing any Class Object
Hyd.dispInformation(e,"Employee") #calling Static Method w.r.t Object Name by passing any Class Object
Hyd.dispInformation(t,"Teacher") #calling Static Method w.r.t Object Name by passing any Class Object