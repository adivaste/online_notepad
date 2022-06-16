import json
import socket
import sys

IP = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)

    """ Opening and reading the file data. """
    #file = open("data/adi.txt", "r")
    #data = file.read()

    # USER INPUT
    note = input("Enter Your Message : ")

    if (note=="!SHOW"):
        client.send(note.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        msg = eval(msg)

        msg = msg["notes"]

        print("\nYour Messages : ")
        for i in msg:
           print(f"* {i}")

    else:
        note = "[STORE]" + note
        client.send(note.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(msg)

    """ Sending the file data to the server. """
    #client.send(data.encode(FORMAT))
    #msg = client.recv(SIZE).decode(FORMAT)
    #print(f"[SERVER]: {msg}")

    """ Closing the file. """
    #file.close()

    """ Closing the connection from the server. """
    client.close()


if __name__ == "__main__":
    main()
