#ServerChat.py
import socket # Step-1
# Step-2
s=socket.socket()
s.bind(("127.0.0.1",8888))
s.listen(2) # Step -3
print("Server Side Program is Ready to Accept Request from Client Side Program")
while(True):
	cs,ca=s.accept() #Step-4
	#Step-5
	cMsg=cs.recv(1024).decode()
	print("Student--> {}".format(cMsg))
	sMsg=input("Professor-->")
	cs.send(sMsg.encode()) #Step-6