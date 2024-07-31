#ReduceEx1.py
import functools
print("Enter list of values seperated by space: ")
lst=[int(val) for val in input().split()]
sum=int(functools.reduce(lambda a,b:a*b,lst))
print("Entered List of Numbers: {}".format(lst))
print("Sum of Numbers in the List = {}".format(sum))