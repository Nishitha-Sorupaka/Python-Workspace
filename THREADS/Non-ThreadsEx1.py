#Program for demonstrating non-thread based applications (Contains only MainThread but not Sub Threads)
#Non-ThreadsEx1.py
import threading
def hello():
	print("line 5: hello() executed by {}".format(threading.current_thread().name))

def hi():
	print("Line 8: hi() executed by {}".format(threading.current_thread().name))

def welcome():
	print("Line 11: welcome() executed by {}".format(threading.current_thread().name))

#main program
print("Line 14: Program Execution stated by {}".format(threading.current_thread().name))
print("----------------------------------------------------------------")
hello()
print("Line:17")
hi()
print("Line:19")
welcome()
print("----------------------------------------------------------------")
print("Line 21: Program Execution ended by {}".format(threading.current_thread().name))