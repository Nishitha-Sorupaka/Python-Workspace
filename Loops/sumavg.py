#Program for Reading list of values and display their sum and Average
#sumavg.py
n=int(input("Enter the Number of values you want to enter:"))
if(n<=0):
	print("{} is Invalid input ".format(n))
else:
	#Reading the values dynamically
	lst=list()
	for i in range(1,n+1):
		val=float(input("Enter {} value: ".format(i)))
		lst.append(val)
	else:
		print('---------------------------------')
		print("List of Elements = {} ".format(lst))
		print('---------------------------------')
		#find sum and average
		s=0
		for val in lst:
			print("\t{}".format(val))
			s=s+val
		else:
			print('---------------------------------')
			print("Sum of Elements = {} ".format(s))
			print("Average of Elements = {} ".format(s/n))
			print('---------------------------------')

	