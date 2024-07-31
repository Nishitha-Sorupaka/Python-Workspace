# Program for demonstrating Destructors
# destex7.py
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
e2 = e1 # Deep copy
e3 = e1 # Deep copy
print("No Longer Interrested in maintaining the memory space for e1 object")
time.sleep(5)
e1 = None  # GC calls Destrutor  forcefully--Forceful Garbage Collection
print("No Longer Interrested in maintaining the memory space for e2 object")
time.sleep(5)
del e2  # GC calls Destrutor  forcefully--Forceful Garbage Collection
print("No Longer Interrested in maintaining the memory space for e3 object")
time.sleep(5)
del e3  # GC calls Destrutor  forcefully--Forceful Garbage Collection
print("---------------------------------------------------------------")
print("Program Execution Ended")
time.sleep(5)