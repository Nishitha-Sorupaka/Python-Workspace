#Program for withdrawing the amount from same account by multiple customers
#SyncBankTransOOPsEx1.py
import threading,time
class BankTransaction:
	@classmethod
	def getAccBal(cls):
		#create Lock Object
		cls.L=threading.Lock() # Step-1
		cls.bal=50000
		print("-"*50)
		print("Total Available Balance = {}".format(cls.bal))
		print("-"*50)

	def __init__(self,wamt):
		self.wamt=wamt

	def withdraw(self):
		BankTransaction.L.acquire() # Step-2
		if(self.wamt>BankTransaction.bal):
			print("Dear Customer: {}, Withdraw of {} amount Transaction Failed!--due to insufficient funds. Available Balance = {}".format(threading.current_thread().name,self.wamt,BankTransaction.bal))
			print("-"*50)
			time.sleep(3)
		else:
			BankTransaction.bal=BankTransaction.bal-self.wamt
			print("Dear Customer: {}, Withdraw of {} amount Transaction Successfull!. Now Available Balance = {}".format(threading.current_thread().name,self.wamt,BankTransaction.bal))
			time.sleep(4)
			print("-"*50)
		BankTransaction.L.release() # Step-3

#main program
BankTransaction.getAccBal()
t1=threading.Thread(target=BankTransaction(10000).withdraw)
t1.name="Nishitha"
t2=threading.Thread(target=BankTransaction(5000).withdraw)
t2.name="Shoaib"
t3=threading.Thread(target=BankTransaction(40000).withdraw)
t3.name="Sudeep"
t4=threading.Thread(target=BankTransaction(8000).withdraw)
t4.name="Chitti"
t5=threading.Thread(target=BankTransaction(1).withdraw)
t5.name="Nilohitha"
#dispatching the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()