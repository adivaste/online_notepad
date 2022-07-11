import socket
import json
from ngrokServer import x,y
from flaskApp import keep_alive

IP = "localhost"
PORT = 5050
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

# Threading functions
x.start()    # To start NGROK Server
y.start()    # Storing the Host and 
keep_alive()


def main():
    print("[STARTING] Server is starting.")
    # Staring a TCP socket.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the IP and PORT to the server.
    server.bind(ADDR)

    # Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
        #Server has accepted the connection from the client. 
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

     
        # Function to store data
        def storeData(note):
          notepadContent = ""
          with open("notepad.json","r") as f:
            notepadContent = json.load(f)
            
          notepadContent["username"]["notes"].append(note)
          
          with open("notepad.json","w") as f:
            json.dump(notepadContent,f)
            
          conn.send("Content Recieved ".encode(FORMAT))

        def sendData():
          sendingContent = ""
          with open("notepad.json","r") as f:
            sendingContent = json.load(f)
            sendingContent = str(sendingContent["username"])

          conn.send(sendingContent.encode(FORMAT))
          
          
        # Receving the content from client
        note = conn.recv(SIZE).decode(FORMAT)

        if (note.startswith("[STORE]")):
          storeData(note[7::])
        else:
          sendData()
          
        # Closing the connection from the client.
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")

if __name__ == "__main__":
    main()
