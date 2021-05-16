#Libraries required
import socket#for sockets
import select#gives the IO capabilities irrespective os OS


HEADER_LENGTH = 10 #Length of the header
IP = "127.0.0.1"
PORT = 1234
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET--->AddressFamilyOnInterNET
#To overcome the port number problems,where we had to change and use again, 
#we use the foolowing code to set it automatically
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#SOL means SocketOptionLevel
#SO means SocketOption
#This allows to reconnect

server_socket.bind((IP,PORT))
#Bind the socket

server_socket.listen()

#Manage the list of sockets we are handling
sockets_list = [server_socket ]
#We will add the client sockets to the list as we manage
#We will maintain a dictionary for clients, who will have username as keys to the 
clients = {}


#Function for receiving message from the clients
def receive_message(client_socket):
	try:
		message_header = client_socket.recv(HEADER_LENGTH)
		if not len(message_header):#Client closed the connection
			return False
		message_length = int(message_header.decode("utf-8").strip())#Finding message len
		return{"header":message_header,"data":client_socket.recv(message_length)}
	except:
		return False

while True:
	read_sockets,_,exception_sockets=select.select(sockets_list,[],sockets_list)
	#three parameters select uses is read list,write list, sockets on which we air on
	for notified_socket in read_sockets:
		if notified_socket == server_socket:#Means a new client asking to get added
			client_socket,client_address = server_socket.accept()#Allow to bind
			user = receive_message(client_socket)#Get the header and message
			if user is False:#Client left
				continue
			#Manage this client
			sockets_list.append(client_socket)
			#Clients dictionary is invoked
			clients[client_socket]=user 
			print(f"Accepted new connection from {client_address[0]}:{client_address[1]}\
			 username:{user['data'].decode('utf-8')}")
		else:#Some client has sent message
			message = receive_message(notified_socket)
			if message is False:#Lost connection--More like exceptional socket
				print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
				sockets_list.remove(notified_socket)
				del clients[notified_socket]#remove it
				continue
			#find the user for the corresponding client socket
			user = clients[notified_socket]
			#prints User : message
			print(f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")
			#Send message to the rest of the clients except the notified client
			for client_socket in clients:
				if client_socket!=notified_socket:
					client_socket.send(user['header']+user['data']+message['header']+message['data'])
	
	for notified_socket in exception_sockets:
		sockets_list.remove(notified_socket)
		del clients[notified_socket]
