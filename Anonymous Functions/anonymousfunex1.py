#anonymousfunex1.py
def sumop(a,b):
	c=a+b
	return c

addop = lambda a,b: a+b

#main program
result=sumop(10,20)
print("Type of sumop=",type(sumop)) #<class,'function'>
print("Sum by using normal function={}".format(result))
print("-"*60)
res=addop(10,20)
print("Type of addop=",type(addop)) #<class,'function'>
print("Sum by using anonymous function={}".format(res))