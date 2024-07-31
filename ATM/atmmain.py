#atmmain.py
from atmmenu import atmmenu
import sys
from banking import *
from atmexceptions import *
def sbi():
	while(True):
		atmmenu()
		try:
			ch=int(input("Enter your Choice: ")) #value error
			bal=500
			match(ch):
				case 1:
					try:
						deposit()
					except ValueError:
						print("Don't enter strs/symbols/alpha-numerics for Deposit Amount ! ")
					except DepositError:
						print("Don't enter zero or Negative amount for Deposit Amount !")
						
				case 2:
					try:
						withdraw()
					except ValueError:
						print("Don't enter strs/symbols/alpha-numerics for WithDraw Amount ! ")
					except WithdrawError:
						print("Don't enter zero or Negative amount for Withdraw Amount !")
					except InsufficientFundError:
						print("You don't have sufficient funds in your current !")
					
				case 3:
					balenquiry()
				case 4:
					print("\nThanks for using ATM App!")
					sys.exit()
				case _:
					print("Your Selection of Operation is Wrong-Try Again!")
			
		except ValueError:
			print("\nDon't Enter strs/symbols/alpha-numerics for your choice!")
