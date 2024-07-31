#atmoperations.py
import sys
from atmexceptions import *
bal=500.00 #Global Variable
def deposit():
    damt=float(input("Enter Deposit Amount: "))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Your Account is deposited with {} and your current bal: {}".format(damt,bal))


def withdraw():
    global bal
    wamt = float(input("Enter Withdraw Amount: "))
    if (wamt <= 0):
        raise WithDrawError
    elif((wamt+500)>bal):
        raise InsufficientFundError
    else:
        bal=bal-wamt
        print("Your Account is debited with {} and your current bal: {}".format(wamt, bal))


def balenq():
    print("Your Account Balance : {}".format(bal))
def exit():
    sys.exit()