#RegExp3.py
import re
gd="Python is an oop Lang.Python is also Fun Prog Lang"
sd="Python"
res=re.findall(sd,gd) # here res is type of List
print("'{}' found {} Times".format(sd,len(res)))
print(res)
