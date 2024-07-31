#areademo.py
import sys
from area import *
from areamenu import menu

while(True):
	menu()
	ch=int(input("Enter Your Choice:"))
	match(ch):
		case 1:
			circle()
		case 2: 
			rectangle()
		case 3:
			square()
		case 4:
			triangle()
		case 5: 
			print("Thank you for using this program!")
			sys.exit()
		case _:
			print("-"*50)
			print("Invalid choice, please try again!")