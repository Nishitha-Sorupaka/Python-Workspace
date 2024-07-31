#program for accepting a line of text and display the words  by using threads
#GenWordsFunEx1.py
import threading,time
def display(n):
	print("Name of Sub Thread in display()=",threading.current_thread().name)
	print("-"*50)
	words=n.split()
	print("Line of Text : {}".format(n))
	print("-"*50)
	for word in words:
		print("\t{}".format(word))
		for letter in word:
			print("\t\t{}".format(letter))
		print()
		time.sleep(1)
	print("-"*50)

#main program
n=input("Enter Line of Text :")
t1=threading.Thread(target=display,args=(n,))
t1.start()
