#reduceex2.py
import functools
print("Enter list of words seperated by space:")
lst=[str(val) for val in input().split()]
res=functools.reduce(lambda x,y:x+" "+y,lst)
print("List of Words={}".format(lst))
print("Sentence =",res)