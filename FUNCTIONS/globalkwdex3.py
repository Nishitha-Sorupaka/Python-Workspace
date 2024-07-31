#globalkwdex3.py
a=10 #global variable
def increment():
	global a #refering Global Variable
	print("line--5-->Val of a in increment()={}".format(a)) #accessing Global variable--10
	a=a+1
	print("line--7-->Val of a in increment()={}".format(a)) #accessing Global variable--11

def updateval():
	global a
	print("line--11-->value of a in updateval()={}".format(a)) # 11
	a=a*2

#main program
print("line--15-->Val of a before increment()--main program={}".format(a)) #10
increment()
print("line--17-->Val of a after increment()--main program={}".format(a)) #11
updateval()
print("line--19-->Val of a after updateval()--main program={}".format(a)) #22
