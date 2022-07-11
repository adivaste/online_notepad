import socket
import time
import os

# --------------------- A L L   C O N S T A N T S --------------------------

FORMAT = "utf-8"
DISCONNECTED_MSG = "! DISCONNECTED"
SIZE = 1024

# PORT AND IP
PORT = 5050
IP =  "127.0.1.1"
ADDR = (IP,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

msg = True
while msg!= DISCONNECTED_MSG:
    msg  = input()
    client.send(msg.encode(FORMAT))
    msg2  = client.recv(SIZE).decode(FORMAT)
    print(msg2)
    if msg2 == "300":
        client.send("Hello".encode(FORMAT))
        msg3 = client.recv(SIZE).decode(FORMAT)
        print(msg3 + "...")

#client.send(DISCONNECTED_MSG.encode(FORMAT))
