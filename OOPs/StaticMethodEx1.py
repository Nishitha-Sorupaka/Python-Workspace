#Program for demonstating Static Methods
#StaticMethodEx1.py
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
    def dispData(obj): # Static Method
        print("-"*50)
        for k,v in obj.__dict__.items():
            print("{}-->{}".format(k,v))
        print("-" * 50)

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
Hyd.dispData(s) #calling Static Method w.r.t Class Name by passing any Class Object
Hyd.dispData(e)
Hyd.dispData(t)