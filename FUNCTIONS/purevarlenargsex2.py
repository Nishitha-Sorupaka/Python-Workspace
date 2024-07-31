 #This program demonstrates the concept of Variable Length Arguments
 #purevarlenargsex2.py 
def disp(sname,*a,crs="PYTHON"): #here *a is called Variable length Parameter and type is tuple
	print("-"*50)
	print("Name of Student={}".format(sname))
	print("{} id doin {} course".format(sname,crs))
	s=0
	for val in a:
		print("{}".format(val),end=' ')
		s=s+val
	print()
	print("Sum={}".format(s))
	print("-"*50)



 #main program
disp("RS",10) #Function Call
disp("JG",10,20)  #Function Call
disp("TR",10,20,30) #Function Call
disp("MC",10,20,30,40) #Function Call 
disp("ZM",10,20,30,40,50) #Function Call
disp("DR",10,20,30,40,50,60) #Function Call
