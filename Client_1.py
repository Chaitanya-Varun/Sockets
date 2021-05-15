#Client is the thing which wants to communicate, where receiver 
#lies for the server

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

#When we connect to the server succesfully, the server sends a message
#msg=s.recv(1024)
#1024-her suggests the chunk size of data we receive at a time from the 
#SOCK_STREAM - TCP we are using

#Display the message
#print(msg.decode("utf-8")) #Not that we used utf-8 encoding

#Once the message is received, the server gets disconnected

#Here we are confing the data chunk and once we are out of it we lose the
#message, so we use a while loop to buffer through the stream
#comment lines 24 and 19 and uncomment below
full_msg=''#Start with empty string
while True:
	msg=s.recv(8)
	if len(msg)<=0:#Message is empty
		break
	full_msg+=msg.decode("utf-8")#Concatenate the broken message
#Obtain the full message
print(full_msg)