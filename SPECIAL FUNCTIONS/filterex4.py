#filterex4.py



n=int(input("Enter how many elements you want to enter:"))
if(n<=0):
	print("Invalid Input")
else:
	lst=[]
	print("-"*50)
	print("Enter {} elements".format(n))
	print("-"*50)
	for i in range(1,n+1):
		val=int(input())
		lst.append(val)
	else:
		print("-"*50)
		print("Original Elements of list:{}".format(lst))
		print("-"*50)
		pslist=list(filter(lambda n:n>0,lst))
		nslist=set(filter(lambda k:k<0,lst))
		zerolist=tuple(filter(lambda k:k==0,lst))
		print("Positive ELements={}".format(pslist))
		print("Negative ELements={}".format(nslist))
		print("Zero ELements={}".format(zerolist))