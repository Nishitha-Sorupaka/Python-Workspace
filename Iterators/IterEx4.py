#IterEx4.py
d={10:"Python",20:"Dsc",30:"Java",40:"DSA",50:"C++"} # here tpl is one of the Iterable object
#Convert Iterable object into Iterator object by using iter(Iterable object)
diter=iter(d)
print("-----------------------------------------------------------")
print("Type of d=",type(d)) # <class,dict>
print("Type of diter=",type(diter)) #<class, dict_keyiterator>
print("-----------------------------------------------------------")
while(True):
	try:
		k=next(diter)
		v=d[k]  # OR   v=d.get(k)
		print("\t{}--->{}".format(k,v))
	except StopIteration:
		print("-----------------------------------------------------------")
		break

