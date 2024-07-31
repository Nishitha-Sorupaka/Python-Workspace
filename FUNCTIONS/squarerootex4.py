#Functions
#squarerootex4.py

# INPUT taken in Function Body
# PROCESSING done in Function Body
# RESULT gives to Function Call

 #Function Definition
def squareroot():
	n=int(input("Enter a Number:"))
	result=n**0.5
	return n,result


#main Program
n,result=squareroot()
print("Square Roor of {} = {}".format(n,result))

print("------------OR-----------")

res=squareroot()
print("Square Root of {} = {}".format(res[0],res[1]))