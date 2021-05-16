#Libraries required
import socket#for sockets
import select#gives the IO capabilities irrespective os OS
import errno #for handling specific errors
import sys #for control over the terminal
HEADER_LENGTH = 10#header length

#Ip and Port numebr
IP = "127.0.0.1"
PORT = 1234
#Grab the client username
myUsername = input("Enter your Username : ")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Socket object
client_socket.connect((IP,PORT))#Connect it to the server
client_socket.setblocking(False) #This allows the reciev functionality working

username = myUsername.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header+username)

while True:
	#Sending things
	message=input(f"{myUsername} > ")
	if message:
		message = message.encode('utf-8')
		message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
		client_socket.send(message_header+message)

	try:
		while True:
			#Receive things
			username_header = client_socket.recv(HEADER_LENGTH)
			if not len(username_header):
				print("Connection lost by the server")
				sys.exit()
			username_length = int(username_header.decode('utf-8').strip())
			username = client_socket.recv(username_length).decode('utf-8')
			message_header = client_socket.recv(HEADER_LENGTH)
			message_length = int(message_header.decode('utf-8').strip())
			message = client_socket.recv(message_length).decode('utf-8')
			print(f"{username} > {message}")

	except IOError as e:
		if e.errno != errno.EAGAIN and e.errno != erno.EWOULDBLOCK:
			print('Reading error',str(e))
			sys.exit()
		
	except Exception as e:
		print('General Error',str(e))
		pass


