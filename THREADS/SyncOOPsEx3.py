#Program demonstating Multiple threads enters into same function and avoid Dead Lock/Race Condition
#SyncOOPsEx3.py
import threading,time
class Table:
	
	@classmethod
	def getLock(cls):
		#creating Lock object
		cls.L=threading.Lock() #Step-1--create an object of Lock class--here L is Class Level data Member

	def __init__(self,n):
		self.n=n

	def multable(self):
		Table.L.acquire() #Step-2
		if(self.n<=0):
			print("{}--{} is invalid input".format(threading.current_thread().name,self.n))
		else:
			print("-"*50)
			print("{}---Multiplication table of {} ".format(threading.current_thread().name,self.n))
			print("-"*50)
			for i in range(1,11):
				print("\t{} X {} = {}".format(self.n,i,self.n*i))
				time.sleep(0.5)
			print("-"*50)
		Table.L.release() #Step-3


#main program

Table.getLock() # Call Class Level Method for initiating Lock Object
#creating multiple sub threads
t1=threading.Thread(target=Table(10).multable)
t2=threading.Thread(target=Table(-12).multable)
t3=threading.Thread(target=Table(9).multable)
t4=threading.Thread(target=Table(19).multable)
#dispatching the threads
t1.start()
t2.start()
t3.start()
t4.start()