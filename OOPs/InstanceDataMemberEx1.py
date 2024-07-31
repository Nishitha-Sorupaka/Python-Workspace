#InstanceDataMemberEx1.py
class Student:pass


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
print("Content of s1 after adding= ",s1.__dict__)
print("Content of s2 after adding= ",s2.__dict__)
print("-----------------------------------")
