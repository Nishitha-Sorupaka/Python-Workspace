#Wap which will generate Even numbers within n where n must be positve integer
#even.py
n=int(input("Enter a Number: "))
if(n<=0):
	print("Invalid Input")
else:
	print("-------------------------")
	print("Even Numbers within:{} ".format(n))
	print("-------------------------")
	i=2
	while(i<=n):
		print("\t{}".format(i))
		i=i+2 # updation part
	else:
		print("\n-------------------------")
		print("I am from else block")
		print("-------------------------")