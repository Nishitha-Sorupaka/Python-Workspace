#RegExp1.py
import re
gd="Python is an oop Lang.Python is also Fun Prog Lang"
sd="Python"
res=re.search(sd,gd) # here res is an object of re.Match Class or None Type
if(res!=None):
	print("Search is Successful")
	print("Begin Index = {}".format(res.start()))
	print("End Index = {}".format(res.end()))
	print("Match = {}".format(res.group()))
else:
	print("Search is Successful")
