#Client Side Program sending Number to Server Side Program and getting Number Square as Response from Server Side Program
#ClientSquare.py
import socket # Step-1
s=socket.socket() # Step-2
s.connect(("localhost",8888))
print("Client Side Program Obtains Connection from Server Side Program")
print("-"*40)
#Step-3
n=input("Enter a Value for getting its Square: ")
s.send(n.encode())
#Step-4
res=s.recv(1024).decode()
print("Square({})={}".format(n,res))
print("-"*40)