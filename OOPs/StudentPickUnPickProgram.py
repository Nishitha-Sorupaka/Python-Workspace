#StudentPickUnPickProgram.py
from StudentPickMenu import Menu
from StudentPickle import StudentPickle
from StudentUnPickle import StudentUnPickle
while(True):
	Menu().menu()
	try:
		ch=int(input("Enter Ur Choice:"))
		match(ch):
			case 1:
				so=StudentPickle()
				so.saveStudData()
			case 2:
				sp=StudentUnPickle()
				sp.readStudRecords()
			case 3:
				print("Thx for this Program")
				break
			case _:
				print("Ur Selection Operation is wrong-try again")
	except ValueError:
		print("Don't Enter alnums,strs and symbols for Choice")