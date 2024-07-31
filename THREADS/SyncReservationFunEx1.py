#Program for Reserving a seat by using threading--
#SyncReservationFunEx1.py
import threading,time
def reservation(nos):
	L.acquire() #Step-2
	global seats
	if(nos>seats):
		print("\tDear Passenger {},---{} seats Booking Failed!----Total Available Number of seats={}".format(threading.current_thread().name,nos,seats))
		time.sleep(5)
	else:
		print("\tDear Passenger {},---{} seats Booking Successfull--Happy Journey".format(threading.current_thread().name,nos))
		seats=seats-nos
		print("\tNow available seats = {}".format(seats))
		print("-"*50)
	L.release() #Step-3


#main program
print("-"*50)
seats=20
print("Initial Total Number of seats={}".format(seats))
print("-"*50)
#creating Lock object
L=threading.Lock() #Step-1
#creating multiple sub threads
t1=threading.Thread(target=reservation,args=(5,))
t1.name="Nishitha"
t2=threading.Thread(target=reservation,args=(16,))
t2.name="Bunny"
t3=threading.Thread(target=reservation,args=(6,))
t3.name="Nilohitha"
t4=threading.Thread(target=reservation,args=(1,))
t4.name="Sudeep"
#dispatching the threads
t1.start()
t2.start()
t3.start()
t4.start()