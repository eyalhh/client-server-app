import socket
import threading

# Ensuring we are using the same protocol
HEADER = 15
FORMAT = "utf-8"
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR =  (SERVER, PORT)

# Setting up the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def handle_server_broadcast(conn):
    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length and msg_length!="":
            msg_length = int("".join(msg_length.split()))
            msg = conn.recv(msg_length).decode(FORMAT)
            print(msg)
    

        
thread_ = threading.Thread(target = handle_server_broadcast, args=(client,))
thread_.start()
while True:
    msg = input()
    send(msg)