#IterEx5.py
d={10:"Python",20:"Dsc",30:"Java",40:"DSA",50:"C++",60:"C"} # here tpl is one of the Iterable object
#Convert Iterable object into Iterator object by using iter(Iterable object)
diter=iter(d)
print("-----------------------------------------------------------")
print("Type of d=",type(d)) # <class,dict>
print("Type of diter=",type(diter)) #<class, dict_keyiterator>
print("-----------------------------------------------------------")
for k in diter:
	print("\t{}===>{}".format(k,d.get(k)))
print("-----------------------------------------------------------")
print("---------------------OR--------------------------------------")
diter=iter(d) # Re-building Dictdict_keyiterator
for k in diter:
	print("\t{}===>{}".format(k,d[k] ))
print("-----------------------------------------------------------")

