#marksmemo.py
#accept student details such as stno, name
stno=int(input("Enter Student Number: "))
stname=input("Enter Student Name: ")
#validation of C Marks
while(True):
	cm=int(input("Enter Marks in C: "))
	if(cm>=0) and (cm<=100):
		break
#validation of CPP Marks
while(True):
	cppm=int(input("Enter Marks in CPP: "))
	if(cppm>=0) and (cppm<=100):
		break
#validation of Python Marks
while(True):
	pytm=int(input("Enter Marks in Python: "))
	if(pytm>=0) and (pytm<=100):
		break
#Calculate Total Marks
totmarks=cm+cppm+pytm
markspercent=(totmarks/300)*100
#Decide the Grade
if(cm<40) or (cppm<40) or (pytm<40):
	grade="FAIL"
else:
	if(totmarks<=300) and (totmarks>=250):
		grade="PASSED IN DISTINCTION"
	elif(totmarks<=249) and (totmarks>=200):
		grade="PASSED IN FIRST" 
	elif(totmarks<=199) and (totmarks>=150):
		grade="PASSED IN SECOND" 
	elif(totmarks<=149) and (totmarks>=120):
		grade="PASSED IN THIRD" 

#Display the marks memo
print("*"*50)
print("\tS T U D E N T  M A R K S  R E P O R T")
print("*"*50)
print("\tStudent Number: {} ".format(stno))
print("\tStudent Name: {} ".format(stname))
print("\tStudent Marks in C : {} ".format(cm))
print("\tStudent Marks in CPP : {} ".format(cppm))
print("\tStudent Marks in PYTHON : {} ".format(pytm))
print("-"*40)
print("\tTotal Marks: {}".format(totmarks))
print("\tPercentage of Marks: {}".format(markspercent))
print("-"*40)
print("\tStudent Result: {} ".format(grade))
print("*"*50)



