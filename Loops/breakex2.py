#breakex2.py
lst=[10,"nishu",34.56,True,"Hyd",2+3j]
i=0
while(i<=len(lst)):
	if(lst[i]=="Hyd"):
		break
	print(lst[i])
	i=i+1
else:
	print("I am from else.... while")

print("Other statements in the program")