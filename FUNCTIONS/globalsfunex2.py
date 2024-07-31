#globalsfunex2.py
a=10
b="Python"
c=23.45
d=2+3j
def fun2():
	obj=globals()
	print("Type of obj=",type(obj))
	for k,v in obj.items():
		print("{}-->{}".format(k,v))
	print("---------------------------")
	print("Value of global variable a=",obj['a'])
	print("Value of global variable b=",obj.get('b'))
	print("Value of global variable c=",globals()['c'])
	print("Value of global variable d=",globals().get('d'))
	



#main program
fun2()