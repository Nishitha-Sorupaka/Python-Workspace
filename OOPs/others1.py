#others1.py---Data Abstraction
from Account1 import Account

ac=Account()
print(ac.__dict__)
#print("Account Number: {}".format(ac.acno))
print("Account Holder Name: {}".format(ac.cname))
#print("Account Balance: {}".format(ac.bal))
#print("Account Pin: {}".format(ac.pin))
print("Account Branch Name: {}".format(ac.bname))