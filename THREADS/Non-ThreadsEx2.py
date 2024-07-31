#Program for demonstrating non-thread based applications (Contains only MainThread but not Sub Threads)
#Non-ThreadsEx2.py
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
squares(lst)
print("----------------------------------------------------------------")
cubes(lst)
print("----------------------------------------------------------------")
print("Program Execution ended by {}".format(threading.current_thread().name))
et=time.time()
print("total Execution Time by Non-Threading Prog={}".format(et-bt))