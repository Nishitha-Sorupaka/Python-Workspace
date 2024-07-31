 #This program demonstrates the concept of Variable Length Arguments
 #varlenargsex1.py ----This program will not execute

def disp(x):
	print("{}".format(x))


def disp(x,y):
	print("{}\t{}".format(x,y))

def disp(x,y,z):
	print("{}\t{}\t{}".format(x,y,z))

def disp(x,y,z,k):
	print("{}\t{}\t{}\t{}".format(x,y,z,k))


 #main program
disp(10) #Function Call
disp(10,20)  #Function Call
disp(10,20,30) #Function Call
disp(10,20,30,40) #Function Call