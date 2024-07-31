#Wap which will find sum of Cubes of n natural numbers
#SumOfCubesOfNumbers.py
n=int(input("Enter the Number for which you want to generate sum of Cubes of Numbers: ")) #n=10 -10   0
if(n<=0):
	print("{} is Invalid input ".format(n))
else:
	print("-------------------------")
	print("Numbers within:{} ".format(n))
	print("-------------------------")
	i,s=1,0 # initialization part
	while(i<=n): # condition part
		print("\t{}".format(i))
		s=s+i**3
		i=i+1 # updation part
	else:
		print("\n-------------------------")
		print("Sum = {} ".format(s))
		print("-------------------------")