#Program for Reading list of values and display them
#listvalues.py
n=int(input("Enter the Number of values you want to enter:"))
if(n<=0):
	print("{} is Invalid input ".format(n))
else:
	lst=list()
	for i in range(1,n+1):
		val=input("Enter {} value: ".format(i))
		lst.append(val)
	else:
		print('---------------------------------')
		print("List of Elements = {} ".format(lst))
		print('---------------------------------')
	