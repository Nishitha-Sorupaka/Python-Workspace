#ClientResultDataBaseEx1.py
import socket
s=socket.socket()
s.connect(("localhost",8558))
print("CSP got Connection from SSP")
print("------------------------------------------------")
#Accept student number from KBD
sno=input("Enter Student Number:")
print("------------------------------------------------")
s.send(sno.encode())
record=s.recv(1024).decode()
print(record)
print("------------------------------------------------")
