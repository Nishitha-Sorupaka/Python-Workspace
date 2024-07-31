#globalsfunex3.py
a,b,c,d=1,2,3,4
def fun2():
	a,b,c,d=10,20,30,40
	x=globals()
	print("Global Variable a={}".format(x.get('a')))
	print("Global Variable a={}".format(x.get('b')))
	print("Global Variable a={}".format(x['c']))
	print("Global Variable a={}".format(x['d']))
	print("Global Variable a={}".format(globals().get('a')))
	print("Global Variable b={}".format(globals().get('b')))
	print("Global Variable c={}".format(globals()['c']))
	print("Global Variable d={}".format(globals()['d']))
	print("==========================================")
	print("Local variable a={}".format(a))
	print("Local variable b={}".format(b))
	print("Local variable c={}".format(c))
	print("Local variable d={}".format(d))
	result=a+b+c+d+x.get('a')+x.get('b')+x['c']+x['d']
	print("-"*50)
	print("Result={}".format(result))
	return a,b,c,d


#main program
print(a,b,c,d)
k1,k2,k3,k4=fun2()
print("Value of k1={}".format(k1))
print("Value of k2={}".format(k2))
print("Value of k3={}".format(k3))
print("Value of k4={}".format(k4))
