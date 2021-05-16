# Sockets
The topic is dealt in steps
1. The first pair of Server-Client files, we just learn how to send data and receive data. We try to implement sharing data using a constant and reasonable data chunk size but will have to shut the connection between the sockets everytime we need to receive the message.
2. We overcome the problem by using a constant size header which gives the length of the message, which accordingly helps the Client to detect the end of the message. As a part of proving the existing connection between the Server and Client, we used time module to transfer the time data between server and client.
3. Now we try to further send more than texts themselves, any python object using pickles. We have import pickle which is an inbuilt python library and using ```pickle.dumps()``` and then receive it using ```pickle.loads()```.
By this method, we can serialise any data type and send to remote as well as local sockets.
4. Now using the concepts above we will implement a Chat room. We will use two files-ChatServer.py and ChatClient.py.
  * In ChatServer.py , we define '''function receive_message()''' to read the message and the corresponding header. Using '''select.select()''' we structure the instructions by organizing. For every new client we take the username and associate with its socket. When a noted client socket is notified, we collect the message and air it to all other sockets. 
  * In ChatClient.py, we first collect the username for every new client and notify it to server. Using a loop, we keep collecting the message to be sent and send it to the server. We then receive the message from server and display the username, message. 
 
 Go through the codes for much cleaner explanation.
 
However, I am not able to properly order the messages. I have been trying to arrange it, we can only receive the message after we send it. I am trying overcome that and also prepare a suitable gui.

Reference : [Sentdex](https://pythonprogramming.net/sockets-tutorial-python-3/)<br>
