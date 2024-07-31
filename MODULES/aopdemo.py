#aopdemo.py---main program
import sys
from aoperations import *
from aopmenu import menu
while(True):
	menu()
	ch=int(input("Enter your Choice:"))
	match(ch):
		case 1:
			addop()
		case 2:
			subop()
		case 3:
			mulop()
		case 4:
			divop()
		case 5:
			modop()
		case 6:
			expoop()
		case 7:
			print("Thanks for using this program!")
			sys.exit()
		case _:
			print("Your Selection of Operations is Wrong - Try again")
