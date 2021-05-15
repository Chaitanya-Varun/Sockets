#As we have seen in the earlier case, we have to shutdown the connection evrytime 
#to get the message, we will tackle that problem using a header
HEADER=10 #header length

#Libraries required
import socket #Inbuilt python library
import time #For sake of the example

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
	msg="Welcome to the server!"
	msg=f"{len(msg):<{HEADER}}"+msg
	#print(f"{len(msg):<20}"+msg)
	#Confirmation
	clientsocket.send(bytes(msg,"utf-8"))
	#Send a string literal to the client using the socket obtained 
	#and send the message by converting to bytes through UTF-8 encoding
	#Now no need for closing the socket, after getting enough length it 
	#client would automatically end the message

	#As the server client conection is retained,we can still keep communicating
	while True:
		time.sleep(3)
		msg = f"the time is : {time.time()}"
		msg=f"{len(msg):<{HEADER}}"+msg
		clientsocket.send(bytes(msg,"utf-8"))