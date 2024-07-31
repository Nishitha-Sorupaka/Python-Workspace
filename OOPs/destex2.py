#Program for demonstrating Destructors
#destex2.py
import sys
import time
class Employee:
    def __init__(self,eno,ename):
        print("I am from Constructor")
        self.eno=eno
        self.ename=ename
        print("-"*50)
        print("Employee Number: {}".format(self.eno))
        print("Employee Name: {}".format(self.ename))
        print("-" * 50)
    def __del__(self):
        print("Garbage Collector calls __del__(self) for De-Allocating Memory space")
        global totMemSpace
        totMemSpace=totMemSpace-sys.getsizeof(self)
        print("Now Available Memory Space:{}".format(totMemSpace))


#main program
print("Program execution started")
e1=Employee(10,"Rossum")
e2=Employee(20,"Travis")
e3=Employee(30,"Ritche")
#to find the memory space of any Object----sys.getsize(objname)
print("Memory Space of e1={}".format(sys.getsizeof(e1)))
print("Memory Space of e1={}".format(sys.getsizeof(e2)))
print("Memory Space of e1={}".format(sys.getsizeof(e3)))
totMemSpace=sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)
print("Total Memory Space(e1,e2,e3) = {}".format(totMemSpace))
print("-"*50)
print("Program execution ended")
time.sleep(5)
#By default after program execution completed,
# GC(Garbage Collector) calls its Destructor automatically for de-allocating the memonry space.
# The process is called Automatic Garbage Collection.


