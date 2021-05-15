#As we have seen in the earlier case, we have to shutdown the connection evrytime 
#to get the message, we will tackle that problem using a header
HEADER=10 #header length

#Libraries required
import socket #Inbuilt python library

#Creating a socket object for the client side
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET corresponds to IPV4,SOCK_STREAM is  corresponding to 
#TCP(Transmition Control Protocol)-streaming socket

#Now this socket has to be connected with the server
s.connect((socket.gethostname(),1234))
#here we areagain using socket.gethostname, as we are dealing with local
#server which means on the same system same IP
#Make sure you have the same ports


#EXAMPLE:
#When we connect to the server succesfully, the server sends a message
while True:#Server stays connected
	full_msg=''#Start with empty string
	new_msg=True
	while True:
		msg=s.recv(16)
		if new_msg:
			print(f"new message length: {msg[:HEADER]}")
			msglen = int(msg[:HEADER])
			new_msg = False 
		full_msg+=msg.decode("utf-8")#Concatenate the broken message
		if len(full_msg)-HEADER==msglen:
			print("full message received!")
			print(full_msg[HEADER:])
			new_msg=True
			full_msg=''
#Obtain the full message
print(full_msg)