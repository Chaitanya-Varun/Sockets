#Server is where the main sender lies
#Socket is an endpoint of port which are communicating
#Libraries required
import socket #Inbuilt python library

#Creating a socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET corresponds to IPV4,SOCK_STREAM is  corresponding to 
#TCP(Transmition Control Protocol)-streaming socket

#Bind the socket to some port on the server(local host)
s.bind((socket.gethostname(),1234))
#IP sockets the address that we bind to is a tuple of the 
#hostname and the port number.

#Now listen
s.listen(5)
#When there re multiple requests from incomimng connections but
#we can handle one connection at a time, so we can maintain some
#sort of queue for the incoming connections
#If someone wants to connect when queue is full, they will be denied

while True:
	clientsocket,address=s.accept()
	#Accept any connection and store its address
	print(f"Connection from {address} has been established!")
	#Confirmation
	clientsocket.send(bytes("Welcome to the server","utf-8"))
	#Send a string literal to the client using the socket obtained 
	#and send the message by converting to bytes through UTF-8 encoding
	clientsocket.close()#Close the connnection after sending the message
	#It helps in making other client connect,it is optional

#Generally after communicating, the sockets of both client and server are 
#closed.
