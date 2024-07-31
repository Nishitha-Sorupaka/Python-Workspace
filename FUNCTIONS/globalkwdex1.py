#globalkwdex1.py

a=10 #global variable
def increment():
	 print("Val of a in increment()={}".format(a))

#main program
print("Val of a before increment()--main program={}".format(a))
increment()