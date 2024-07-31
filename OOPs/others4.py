#others4.py---Data Abstraction
from Account4 import Account #will get error bcoz Account made as Encapsulated __Account

ac=Account()
print(ac.__dict__)
ac.getAccDetails()
print(ac.__dict__)
print("Account Number: {}".format(ac.acno))
print("Account Holder Name: {}".format(ac.cname))
print("Account Balance: {}".format(ac.bal))
print("Account Pin: {}".format(ac.pin))
print("Account Branch Name: {}".format(ac.bname))