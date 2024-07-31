#Program for demonstrating thread based applications (Contains MainThread and Sub Threads)
#MainSubThreadsEx2.py
import threading,time
def squares(lst):
	for val in lst:
		print("{}--squares({})={}".format(threading.current_thread().name,val,val**2))
		time.sleep(1)
def cubes(lst):
	for val in lst:
		print("{}--cubes({})={}".format(threading.current_thread().name,val,val**3))
		time.sleep(1)

#main program
bt=time.time()
print("Program Execution stated by {}".format(threading.current_thread().name))
print("----------------------------------------------------------------")
lst=[12,4,15,-5,16,19,25,8]
#Creating 2 sub threads
t1=threading.Thread(target=squares,args=(lst,)) # Here t1 is object of Thread-sub thread and its default name is Thread-1
t2=threading.Thread(target=cubes,args=(lst,)) # Here t2 is object of Thread-sub thread and its default name is Thread-2
t1.start()
t2.start()
print("Number of threads after sub threads start=",format(threading.active_count()))
#join the sub threads
t1.join()
t2.join()
print("----------------------------------------------------------------")
print("Number of threads after sub threads completes=",format(threading.active_count()))
print("Program Execution ended by {}".format(threading.current_thread().name))
et=time.time()
print("total Execution Time by Non-Threading Prog={}".format(et-bt))