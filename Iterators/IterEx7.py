#IterEx7.py
r=range(10,100,10)
#Convert Iterable object into Iterator object by using iter(Iterable object)
riter=iter(r)
print("-----------------------------------------------------------")
print("Type of r=",type(r)) # <class,range>
print("Type of riter=",type(riter)) #<class,range_iterator>
print("-----------------------------------------------------------")
for val in riter:
	print("\t{}".format(val))
print("-----------------------------------------------------------")

