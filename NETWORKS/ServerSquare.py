#Server Program Accepts the Value from Client Side Program and give its Square
#ServerSquare.py
import socket # Step-1
# Step-2
s=socket.socket()
s.bind(("localhost",8888))
s.listen(2) # Step -3
print("Server Side Program is Ready to Accept Request from Client Side Program")
while(True):
	try:
		cs,ca=s.accept() #Step-4
		#Step-5
		num=float(cs.recv(1024).decode())
		print("Value of Client = {}".format(num))
		square=num**2
		cs.send(str(square).encode()) #Step-6
	except ValueError:
		cs.send("Dont enter strs, symbols and alpha numerics".encode())