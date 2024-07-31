#Functions
#approach4.py
# INPUT taken in Function Body
# PROCESSING done in Function Body
# RESULT gives to Function Call

def sumop():
	a=int(input("Enter First Value:"))
	b=int(input("Enter Second Value:")) # INPUT taken in Function Body
	c=a+b # here 'a','b' and 'c' are called Local Variables--Processing
	return c 


#main Program
res=sumop()
print("Sum={}".format(res))