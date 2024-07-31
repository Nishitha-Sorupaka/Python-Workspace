#IterEx3.py
sets={10,"Rossum",45.67,True,2+3j} # here tpl is one of the Iterable object
#Convert Iterable object into Iterator object by using iter(Iterable object)
setsiter=iter(sets)
print("-----------------------------------------------------------")
print("Type of sets=",type(sets)) # <class,set>
print("Type of setsiter=",type(setsiter)) #<class, set_iterator>
print("-----------------------------------------------------------")
while(True):
	try:
		print(next(setsiter))
	except StopIteration:
		print("-----------------------------------------------------------")
		break
