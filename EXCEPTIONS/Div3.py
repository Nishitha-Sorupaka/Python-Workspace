#Program for accepting two integer values and find their division
#Div3.py
try:
	s1=input("Enter First Value: ")
	s2=input("Enter Second Value: ")
	#s3=s1/s2--invalid process
	a=int(s1) #------X
	b=int(s2) #------X
	c=a/b #----------X	
except (ZeroDivisionError,ValueError): #Multi exception handling block
	print("\nDo not enter Zero for Denominator")
	print("\nDo not enter strs / symbols / alphanumerics")

else:
	print('-'*20)
	print("Value of a=",a)
	print("VAlue of b=",b)
	print("Div=",c)
	print('-'*20)

finally:
	print("\nI am from finally block")