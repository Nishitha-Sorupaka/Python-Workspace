#Program for obtaining default Thread(MainThread)
#CurrentThreadEx1.py
import threading
t=threading.current_thread()
#tname=t.getName()---Not recommended because  DeprecationWarning: getName() is deprecated, get the name attribute instead
tname=t.name
print("Default Thread Name=",tname)
print("=======OR================")
print("Default Thread Name=",threading.current_thread().name)