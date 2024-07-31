#Program for finding name of main thread
#DefaultThreadEx.py
import threading
t=threading.current_thread()
print(t)
print("Default Name of thread=",t.name)