#Functions
#approach4_1.py
# INPUT taking in Function Body
# PROCESSING done in Function Body
# RESULT gives to Function Call

def sumop():
	a=int(input("Enter First Value:"))
	b=int(input("Enter Second Value:")) # INPUT taken in Function Body
	c=a+b # here 'a','b' and 'c' are called Local Variables--Processing
	return a,b,c # here return statement can return one or more number of values


#main Program
n1,n2,n3=sumop() # Function call & RESULT gives to Function Call
print("sum({},{})={}".format(n1,n2,n3))
print("------------------OR------------------")
res=sumop() #here res is a variable of type <class, 'tuple'>
print("Sum({},{})={}".format(res[0],res[1],res[2]))