#sort.py
n=int(input("Enter the number of Inputs you want to add in List: "))
if(n<=0):
	print("Invalid Input")
else:
	lst=list()
	for i in range(1,n+1):
		val=int(input("Enter the {} value: ".format(i)))
		lst.append(val)
	else:
		print(lst)
		lst.sort()
		
		print("-"*30)
		print("-"*30)
		print("Ascending Order: {}".format(lst[::]))
		print("Descending Order: {}".format(lst[::-1]))
		print("-"*30)
		'''
		for n in lst:
			if(n<=1):
				print("{} is invalid input".format(n))
			else:
				print("-"*30)
				print("Ascending Order: {}".format(lst[::]))
				print("Descending Order: {}".format(lst[::-1]))
				print("-"*30)
				'''