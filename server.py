import socket
import threading

# Importing the constants from the constants file (constants.py)
from my_constants import HEADER, FORMAT, PORT, SECRET_CODE_TO_ENTER
# Importing function 'send' from protocol.py
from protocol import EXIT_MESSAGE, LOG_MESSAGE, REALIZE_MESSAGE, LOG_MESSAGE_MAX, send

# Setting some variables
SERVER = socket.gethostbyname(socket.gethostname())
ADDR =  (SERVER, PORT)
client_buffer = []
message_buffer = []

# Creating the server object (actually a socket object)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def broadcast_message(msg):
    for client in client_buffer:
        send(client[1], msg, HEADER, FORMAT)


def add_to_message_buffer(msg):
    global message_buffer
    if len(message_buffer) < LOG_MESSAGE_MAX:
        message_buffer.append(msg)
    else:
        message_buffer = []
    

def handle_client(conn, addr):
    print(f"{addr} just connected.")
    
    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length and msg_length!="":
            msg_length = int("".join(msg_length.split()))
            msg = conn.recv(msg_length).decode(FORMAT)
            formatted_msg = f'{addr} {msg}'
            add_to_message_buffer(formatted_msg)
            print(formatted_msg)
            if msg == EXIT_MESSAGE:
                broadcast_message(f'{addr} requested !DISCONNECT.')
                client_buffer.remove((conn,addr))
                broadcast_message(f'{addr} disconnected.')
                break
            elif msg == LOG_MESSAGE:
                broadcast_message(f'{addr} requested !LOG.')
                send(conn, 'Messages are:', HEADER, FORMAT)
                for mess in message_buffer:
                    send(conn, mess, HEADER, FORMAT)
            elif msg == REALIZE_MESSAGE:
                broadcast_message(f'{addr} requested !WHOIS.')
                send(conn, 'Client are:', HEADER, FORMAT)
                for client in client_buffer:
                    send(conn, f'{client[0]}', HEADER, FORMAT)
            else: 
                broadcast_message(formatted_msg)

    conn.close()


def authenticate(conn):
    while True:
        send(conn, "whats the secret password?", HEADER, FORMAT)
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length and msg_length != "":
            msg_length = int("".join(msg_length.split()))
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == SECRET_CODE_TO_ENTER:
                send(conn, "Authentication Succeeded.", HEADER, FORMAT)
                break


def start():
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        authenticate(conn)
        client_buffer.append((addr, conn))
        broadcast_message(f'{addr} joined.')
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"There are {len(client_buffer)} active clients.")
        

print("The server is starting....")
start()