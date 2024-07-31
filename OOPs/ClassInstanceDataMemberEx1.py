#ClassInstanceDataMemberEx1.py
class Student:
    crs="PYTHON" #here crs is a Class Level Data Member


#main program
s1=Student() #Here s1 is called object
s2=Student() #Here s1 is called object
print("-----------------------------------")
print("Content of s1 before adding= ",s1.__dict__)
print("Content of s2 before adding= ",s2.__dict__)
print("-----------------------------------")
#Adding Instance Data Members through an object to s1
s1.sno=10
s1.sname="RS"
s1.marks=33.33
#Adding Instance Data Members through an object to s2
s2.sno=20
s2.sname="TR"
s2.marks=63.33
print("First Object Data")
print("-----------------------------------")
print("Student Number: {}".format(s1.sno))
print("Student Name: {}".format(s1.sname))
print("Student Marks: {}".format(s1.marks))
print("Student Course: {}".format(Student.crs))
print("-----------------------------------")
print("Second Object Data")
print("-----------------------------------")
print("Student Number: {}".format(s2.sno))
print("Student Name: {}".format(s2.sname))
print("Student Marks: {}".format(s2.marks))
print("Student Course: {}".format(Student.crs))
print("-----------------------------------")
