#voterex2.py

while(True):
	age=int(input("Enter the age of the Citizen: "))
	if(age>=18):
		break
print("Your age is {} and you are eligible to vote".format(age))