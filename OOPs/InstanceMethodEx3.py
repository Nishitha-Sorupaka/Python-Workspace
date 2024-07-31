#Program for demonstating Instance Methods
#InstanceMethodEx3.py
class Student:
    def getStudentData(self): # Instance Method
        print("id of current object in getStudentData()= {}".format(id(self)))
        self.sno=int(input("Enter Student Number: "))
        self.sname=input("Enter Student Name: ")
        self.marks=float(input("Enter Student Marks: "))
        self.displayStudData()
    def displayStudData(self): # Instance Method
        print("Student Number: {}".format(self.sno))
        print("Student Name: {}".format(self.sname))
        print("Student Marks: {}".format(self.marks))

#main program
s1=Student()
s2=Student()
#read the instance data to the objects
print("-"*50)
s1.getStudentData() #Calling Instance Method w.r.t Class Name
#or Student.getStudentData(s1) #Calling Instance Method w.r.t Class Name
print("-"*50)
s2.getStudentData() #Calling Instance Method w.r.t Class Name
#or Student.getStudentData(s2) #Calling Instance Method w.r.t Class Name
print("-"*50)
