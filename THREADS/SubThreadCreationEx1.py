#Program for creating sub thread, set name and get name of the threads
#SubThreadCreationEx1.py
import threading
def welcome(val):
	print("-"*50)
	print("Number of Threads after sub thread creation=",threading.active_count())
	print("Name of Sub Thread in welcome()=",threading.current_thread().name)
	print("{} Good Evening".format(val))
	print("-"*50)





#main program
n=input("Enter the Name: ")
t1=threading.Thread(target=welcome,args=(n,))
print("Name of the Sub Thread in main program before setting=",t1.name)
#t1.setName(n)--Not recommended bcoz setName() is decprecated on "name" attribute
t1.name="Rajesh" #--Recommended to use
print("Name of the sub thread in main program after setting=",t1.name)
#dispatch or send the sub thread to targetted function
t1.start()