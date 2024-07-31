#Program for generating N to 1 numbers where N is Positive(+ve)
#NumGenEx3.py
n=int(input("Enter how many Numbers you want to generate: ")) #n=10 -10   0
if(n<=0):
	print("{} is Invalid input ".format(n))
else:
	print("-------------------------")
	print("Numbers within:{} in reverse order ".format(n))
	print("-------------------------")
	while(n>0): # condition part
		print("\t{}".format(n),end="")
		n=n-1 # updation part
	else:
		print("\n-------------------------")
		print("I am from else block")
		print("-------------------------")


		# or
#	i=n # initialization part
#	while(i>=1): # condition part
#		print("\t{}".format(i),end="")
#		i=i-1 # updation part