#Program for displaying Multiplication table
#table.py
n=int(input("Enter Which Number table you want to generate: ")) #n=10 -10   0
if(n<=0):
	print("{} is Invalid input ".format(n))
else:
	print("-------------------------")
	print("Multiplication table of {} ".format(n))
	print("-------------------------")
	i=1
	while(i<=10): # condition part
		print("\t{} x {} = {}".format(n,i,n*i))
		i=i+1 # updation part
	else:
		print("\n-------------------------")
		print("Table Printed ")
		print("-------------------------")