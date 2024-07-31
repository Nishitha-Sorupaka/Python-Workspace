#Program for demonstrating Destructors
#destex1.py
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
#main program
print("Program execution started")
e1=Employee(eno=10,ename="Rossum")
e2=Employee(eno=20,ename="Travis")
print("Program execution ended")
time.sleep(10)
#By default after program execution completed,
# GC(Garbage Collector) calls its Destructor automatically for de-allocating the memonry space.
# The process is called Automatic Garbage Collection.


