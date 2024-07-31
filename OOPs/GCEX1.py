#Program for demostrating Garbage Collector running process
#GCEX1.py
import gc
print("Program execution started")
print("Initially is GC Running: ",gc.isenabled()) #True
a=100
b=200
c=a+b
print("Value of a={}".format(a))
gc.disable()
print("Value of b={}".format(b))
print("Now is GC Running: {}".format(gc.isenabled())) #False
print("Sum={}".format(c))
gc.enable()
print("Now is GC Running: {}".format(gc.isenabled())) #True
print("Program execution ended")