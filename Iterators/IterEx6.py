#IterEx6.py
s="PYTHON"
#Convert Iterable object into Iterator object by using iter(Iterable object)
siter=iter(s)
print("-----------------------------------------------------------")
print("Type of s=",type(s)) # <class,str>
print("Type of siter=",type(siter)) #<class, str_iterator>
print("-----------------------------------------------------------")
for val in siter:
	print("\t{}".format(val))
print("-----------------------------------------------------------")
