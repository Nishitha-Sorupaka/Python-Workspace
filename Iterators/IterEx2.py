#IterEx2.py
tpl=(10,"Rossum",45.67,True,2+3j) # here tpl is one of the Iterable object
#Convert Iterable object into Iterator object by using iter(Iterable object)
tpliter=iter(tpl)
print("-----------------------------------------------------------")
print("Type of tpl=",type(tpl)) # <class,tuple>
print("Type of tpliter=",type(tpliter)) #<class, tuple_iterator>
print("-----------------------------------------------------------")
while(True):
	try:
		print(next(tpliter))
	except StopIteration:
		print("-----------------------------------------------------------")
		break
