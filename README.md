# Sockets
The topic is dealt in steps
1. The first pair of Server-Client files, we just learn how to send data and receive data. We try to implement sharing data using a constant and reasonable data chunk size but will have to shut the connection between the sockets everytime we need to receive the message.
2. We overcome the problem by using a constant size header which gives the length of the message, which accordingly helps the Client to detect the end of the message. As a part of proving the existing connection between the Server and Client, we used time module to transfer the time data between server and client.
3. 
