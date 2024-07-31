#Program for finding Number of Threads in program
#ActiveThreadCountEx.py
import threading
print("Default Thread Name=",threading.current_thread().name)
print("By Default, Number of Active Threads=",threading.active_count())
