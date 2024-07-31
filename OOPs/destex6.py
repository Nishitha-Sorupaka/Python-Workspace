# Program for demonstrating Destructors
# destex6.py
import time, sys
class Employee:
    def __init__(self, eno, ename):
        print("I am from Constructor")
        self.eno = eno
        self.ename = ename
        print("--------------------------------------------------")
        print("Employee Number:{}".format(self.eno))
        print("Employee Name:{}".format(self.ename))
        print("--------------------------------------------------")

    def __del__(self):
        print("Garbage Collectors calls __del__(self) for De-allocating Mem Space")


# Main program
print("Program Execution Started")
e1 = Employee(10, "Rossum")
e2=e1 # Deep copy
e3=e1 # Deep copy
print(e1.__dict__,id(e1))
print(e2.__dict__,id(e2))
print(e3.__dict__,id(e3))
print("---------------------------------------------------------------")
print("Program Execution Ended")
time.sleep(5)