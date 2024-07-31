#ListAdding.py
n=int(input("Enter How many Numbers you want to add in a List: "))
if(n<=0):
	print("{} is invalid input".format(n))
else:
	lst=list()
	for i in range(1,n+1):
		num=input("Enter {} NUmber: ".format(i))
		lst.append(num)
	print(lst)
















