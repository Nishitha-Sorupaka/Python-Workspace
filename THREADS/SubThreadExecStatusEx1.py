#Program for creating sub thread, set name and get name of the threads, execution status and join
#SubThreadExecStatusEx1.py
import threading
def welcome(val):
	print("-"*50)
	print("Number of Threads after sub thread creation=",threading.active_count())
	print("Name of Sub Thread in welcome()=",threading.current_thread().name)
	print("{} Good Evening".format(val))
	print("-"*50)

#main program
#create sub thread
print("Name of the Main Thread=",threading.current_thread().name)
print("-"*50)
print("Number of threads in this program before creating sub threads=",threading.active_count())
t1=threading.Thread(target=welcome,args=("Rossum",))
print("Execution status of sub thread before start=",t1.is_alive()) #False
#dispatch or send the sub thread to targetted function
t1.start()
print("Execution status of sub thread after start=",t1.is_alive()) #True
print("Number of threads in this program during Execution=",threading.active_count())
t1.join()
print("Number of threads in this program after sub thread completion=",threading.active_count())
print("Execution status of sub thread after completion=",t1.is_alive()) #False
print("-"*50)