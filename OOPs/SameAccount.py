#SameAccount.py-----file name and Module Name------Data Encapsulation
class Account:
    def __init__(self):
        self.__acno=1234
        self.cname="Naresh"
        self.__bal=3.4
        self.__pin=8989
        self.bname="SBI"
    def __samecustomer(self):
        print("-------------------------------")
        print("Current Customer Details")
        print("-------------------------------")
        print("Account Number:{}".format(self.__acno))
        print("Account Holder Name:{}".format(self.cname))
        print("Account Balance:{}".format(self.__bal))
        print("Account Pin:{}".format(self.__pin))
        print("Account Branch Name:{}".format(self.bname))
        print("-------------------------------")
    def show(self):
        Account.__samecustomer(self)

#main program
ao=Account() # Object Creation calls Default Constructor
ao.show()