#ClassInstanceDataMemberEx2.py
class Student:
    crs="PYTHON" #here crs is a Class Level Data Member
    city="HYD" #here city is a Class Level Data Member

#main program
s1=Student() #Here s1 is called object
s2=Student() #Here s1 is called object
print("-----------------------------------")
print("Content of s1 before adding= ",s1.__dict__)
print("Content of s2 before adding= ",s2.__dict__)
print("-----------------------------------")
#Adding Instance Data Members through an object to s1
s1.sno=int(input("Enter First Student Number: "))
s1.sname=input("Enter First Student Name: ")
s1.marks=float(input("Enter First Student Marks: "))
#Adding Instance Data Members through an object to s2
s2.sno=int(input("Enter Second Student Number: "))
s2.sname=input("Enter Second Student Name: ")
s2.marks=float(input("Enter Second Student Marks: "))
print("-----------------------------------")
print("First Object Data")
print("-----------------------------------")
print("Student Number: {}".format(s1.sno))
print("Student Name: {}".format(s1.sname))
print("Student Marks: {}".format(s1.marks))
print("Student Course: {}".format(Student.crs)) #Accessing class level Data Members by using Class Name
print("Student City: {}".format(Student.city)) #Accessing class level Data Members by using Class Name
print("-----------------------------------")
print("Second Object Data")
print("-----------------------------------")
print("Student Number: {}".format(s2.sno))
print("Student Name: {}".format(s2.sname))
print("Student Marks: {}".format(s2.marks))
print("Student Course: {}".format(Student.crs)) #Accessing class level Data Members by using Class Name
print("Student City: {}".format(Student.city)) #Accessing class level Data Members by using Class Name
print("-----------------------------------")
