#ServerResultDataBaseEx.py
import socket
import mysql.connector
s=socket.socket()
s.bind(("localhost",8558))
s.listen(2)
print("SSP is ready to Accept any CSP Request")
while(True):
	try:
		csock,caddr=s.accept()
		stno=int(csock.recv(1024).decode())
		#PDBC Code
		con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="batch6pm")
		cur=con.cursor()
		cur.execute("select * from result where sno = %d" %stno)
		record=cur.fetchone()
		csock.send(str(record).encode())
	except ValueError:
		csock.send("Don't Enter alnums,strs and symbols for student Number".encode())
	except mysql.connector.DatabaseError as db:
		csock.send(("Problem in MySQL DB:"+db).encode())
	except :
		csock.send("Ooops Some thing went wrong".encode())



