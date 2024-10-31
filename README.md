# learning about sockets in python

Building a messaging service with sockets in python, constructed based on this model:
We have the client-side code which will be on the client.py file - basically any client that wants to connect to our server needs to run this file.
We will also have the server-side code which will be on the server.py file - which will run only on a single machine of our choosing.

The procedure is very simple:
1. A client establishes a secure and reliable connection via the socket with the server
2. The server enlists the client in his 'client' buffer
3. The client sends a message
4. The server gets the message and enlists it in his buffer
5. The server broadcasts the message to all the other clients enlisted in his 'client' buffer

A possibal expension for this project:
Clients may want to send messages privatly, and not to everyone, meaning instead of like a message board, it will be sortof a sms-style app, in which case, the code would need to be changed and configured for that process.

UPDATE: for more flexibily, I also added a protocol.py code - defines the protocol the clients and server use, and constants.py code - a bunch of constants that we export to make our server functional like a disconnect message.
IF YOU LIKE, DOWNLOAD THE CODE AND TRY IT WITH YOUR FRIEND IN A LAN, IT WONT WORK PUBLICLY OF COURSE BUT IT WILL PROVIDE A SECURE CONNECTION IF YOU ARE ON THE SAME NETWORK.
