#bigsmall.py
import functools
print("Enter the elements seperated by space:")
lst=[int(x) for x in input().split()]
big=functools.reduce(lambda x,y: x if x>y else y,lst)
small=functools.reduce(lambda x,y: x if x<y else y,lst)
print("-"*50)
print("Original List:{}".format(lst))
print("-"*50)
print("Biggest Number in the List:{}".format(big))
print("Smallest Number in the List:{}".format(small))