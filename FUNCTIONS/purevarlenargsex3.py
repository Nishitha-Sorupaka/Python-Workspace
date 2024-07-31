 #This program demonstrates the concept of Variable Length Arguments
 #purevarlenargsex3.py 
def disp(sname,*a,crs="PYTHON"): #here *a is called Variable length Parameter and type is tuple
	print("-"*50)
	print("Name of Student={}".format(sname))
	print("{} is doing {} course".format(sname,crs))
	s=0
	for val in a:
		print("{}".format(val),end=' ')
		s=s+val
	print()
	print("Sum={}".format(s))
	print("-"*50)



#main program
#disp() ----TypeError: disp() missing 1 required positional argument: 'sname'
disp("HYD",crs="DL")
disp(sname="Mohan",crs="Testing")
disp("ROSSUM")
disp("RS",10) #Function Call
disp("JG",10,20)  #Function Call
disp("TR",10,20,30) #Function Call
disp("MC",10,20,30,40) #Function Call 
disp("ZM",10,20,30,40,50) #Function Call
disp("DR",10,20,30,40,50,60) #Function Call
#disp(-10,-20,-30,sname="KVR") ---TypeError: disp() got multiple values for argument 'sname'
#disp("KVR",crs="DSC",4,5,-4,-5) ---SyntaxError: positional argument follows keyword argument
#disp("KVR",4,5,-4,-5,"JAVA") ----TypeError: unsupported operand type(s) for +: 'int' and 'str'
disp("KVR",4,5,-5,-4,crs="JAVA")
#disp(10,-10,crs="Django",sname="Dear Comrade") ---TypeError: disp() got multiple values for argument 'sname'
#disp("RW",crs="ML",a=10,20,30,40) ---SyntaxError: positional argument follows keyword argument
