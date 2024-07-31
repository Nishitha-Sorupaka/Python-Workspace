#Program for generating 1-n Numbers after each and every second
#NumGenOOPEx2.py
import threading,time
class Number:
	def generate(self,n):
		print("Name of Sub Thread in generate()=",threading.current_thread().name)
		if(n<=0):
			print("Invalid Input")
		else:
			print("-"*50)
			print("Numbers within : {}".format(n))
			print("-"*50)
			for i in range(1,n+1):
				print("\tValue of i={}".format(i))
				time.sleep(1)
			print("-"*50)

#main program
n=int(input("Enter How many numbers you want to generate? :"))
t1=threading.Thread(target=Number().generate,args=(n,))
t1.start()