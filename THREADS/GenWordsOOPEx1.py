#program for accepting a line of text and display the words  by using threads
#GenWordsOOPEx1.py
import threading,time
class Display:
	def __init__(self):
		self.n=input("Enter Line of Text :")

	def display(self):
		print("Name of Sub Thread in display()=",threading.current_thread().name)
		print("-"*50)
		words=self.n.split()
		print("Line of Text : {}".format(self.n))
		print("-"*50)
		for word in words:
			print("\t{}".format(word))
			for letter in word:
				print("\t\t{}".format(letter))
			print()
			time.sleep(1)
		print("-"*50)

#main program

t1=threading.Thread(target=Display().display)
t1.start()
