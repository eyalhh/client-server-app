EXIT_MESSAGE = "!DISCONNECT"
LOG_MESSAGE = "!LOG"
REALIZE_MESSAGE = "!WHOIS"
LOG_MESSAGE_MAX = 25

def send(connection, msg, HEADER, FORMAT):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    connection.send(send_length)
    connection.send(message)
