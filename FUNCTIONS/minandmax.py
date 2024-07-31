#Wap which will accept list of values and find their max and min
#minandmax.py

def readnumbers():
	n=int(input("Enter number of values you want to enter in list: "))
	if(n<=0):
		return None
	else:
		lst=list()
		for i in range(1,n+1):
			num=int(input("Enter the {} number: ".format(i)))
			lst.append(num)
		else:
			#print(lst)
			return lst

# Function to display numbers
def displaynumbers(num):
	print("-"*50)
	for name in num:
		print("\t{}".format(name))
	print("-"*50)


def minofnumbers(num):
	"""total = 0
	for x in num:
		total=total+x"""
	minimum=min(num)
	return minimum

def maxofnumbers(num):
	'''total = 0
	for x in num:
		total=total+x
	avg=total/len(num)'''
	maximum=max(num)
	return maximum




num = readnumbers()
if(num==None):
	print("Invalid Input, try again")
else:
	print("Original Numbers:")
	displaynumbers(num)
	minimum=minofnumbers(num)
	print("Min of Numbers: {}".format(minimum))
	maximum=maxofnumbers(num)
	print("Max of Numbers: {}".format(maximum))