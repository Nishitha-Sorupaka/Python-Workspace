#Program for demonstating Instance Methods
#InstanceMethodEx1.py
class Student:
    def getStudentData(self): # Instance Method
        print("id of current object in getStudentData()= {}".format(id(self)))
        self.sno=int(input("Enter Student Number: "))
        self.sname=input("Enter Student Name: ")
        self.marks=float(input("Enter Student Marks: "))
    def displayStudData(self): # Instance Method
        print("Student Number: {}".format(self.sno))
        print("Student Name: {}".format(self.sname))
        print("Student Marks: {}".format(self.marks))




#main program
s1=Student()
s2=Student()
#read the instance data to the object s1
print("-"*50)
print("id of s1 in main program: {}".format(id(s1)))
print("-"*50)
s1.getStudentData() #Calling Instance Method w.r.t Object Name
print("id of s2 in main program: {}".format(id(s2)))
print("-"*50)
s2.getStudentData() #Calling Instance Method w.r.t Object Name
print("-------------------------------------------------------")
print("First Object data")
print("-----------------------------")
s1.displayStudData() #Calling Instance Method w.r.t Object Name
print("-------------------------------------------------------")
print("Second Object data")
print("-----------------------------")
s2.displayStudData() #Calling Instance Method w.r.t Object Name
print("-----------------------------")
