#prime.py
n=int(input("Enter the number of Inputs you want to add in List: "))
if(n<=0):
	print("Invalid Input")
else:
	lst=list()
	for i in range(1,n+1):
		val=int(input("Enter the {} value: ".format(i)))
		lst.append(val)
	else:
		lst.sort()
		print(lst)
		print("-"*30)
		for n in lst:
			if(n<=1):
				print("{} is invalid input".format(n))
			else:
				print("-"*30)
				print("Number: {}".format(n))
				print("-"*30)
				res=False
				for i in range(2,n):
					if(n%i==0):
						res=True
						break
				if(res):
					print("{} is not a prime number".format(n))
				else:
					print("{} is a prime number".format(n))