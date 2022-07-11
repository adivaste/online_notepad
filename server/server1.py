import socket
import threading
import time
import os
import json

# --------------------- A L L   C O N S T A N T S --------------------------

FORMAT = "utf-8"
DISCONNECTED_MSG = "! DISCONNECTED"
SIZE = 1024

# PORT AND IP 
PORT = 5050
IP =  socket.gethostbyname(socket.gethostname())
ADDR = (IP,PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#-------------------------- F U N C T I O N S ------------------------------

# NGROK Server for PORT FORWARDING
def portForwardNGROK():

    # Checking for existing NGROK file, if not downloading it.
    currDir = os.listdir()
    if "ngrok" not in currDir:
        os.system("wget -q -c -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
        os.system("unzip -qq -n ngrok-stable-linux-amd64.zip")

    # Furnishing the Required Permissions
    os.system("chmod 777 ngrok")

    # Authenticating the Tokens
    os.system("./ngrok authtoken 2AZ6Q4rkOlX4Lk8Wyl2p6LeSzm5_86zUyKaEBTBdMDf9nrQjV")

    # Starting TCP using NGROK on PORT:5050 
    os.system("./ngrok tcp 5050")

# Create the "notepad.json" file to store the notes
def createNotepadFile():

    if "notepad.json" in os.listdir():
        return

    notepadFileContent = {
        "username" : "admin",
        "password" : "pass@123",
        "notes" : []
    }
    with open("./notepad.json","w") as f:
        json_object = json.dumps(notepadFileContent)
        f.write(json_object)

# Clear All Notes from server 
def clearAllNotes():

    # Creating the TRASH Folder and moving NOTES to TRASH file before removing it 
    if "server_trash" not in os.listdir():
        os.mkdir("./server_trash")

    with open("./server_trash/notepad.json","w") as f:
        f.write("")

    os.rename("./notepad.json","./server_trash/notepad.json")

    # Regenerating the "notepad.json" file 
    createNotepadFile()

# File Operations on the SERVER 
def fileOperations(operationType,data=None):
    if (operationType == "POST"):
        with open("notepad.json","r+") as f:
            json_object = json.load(f)
            json_object["notes"].append(data)
            f.seek(0)
            f.write(json.dumps(json_object))
            return "201"        # Success [OK]
    elif (operationType == "GET"):
        with open("notepad.json","r+") as f:
            json_object = json.load(f)
            requested_data = json.dumps(json_object)
            return requested_data
    elif (operationType == "CLEAR"):
        clearAllNotes()
        return "202"            # Success [OK]
    else:
        return "400"            # Bad Request

# Send the data to client 
def sendDataToClient(conn,addr,msg):
    print()
# Recieve the data from client
def recieveDataFromClient():
    print()

# Handle the Client 
def handleClient(conn,addr):
    print(f"[ NEW CONNECTION ] Server is Connected to {addr}")

    isConnected  = True
    while isConnected:
        msg = conn.recv(SIZE).decode(FORMAT)
        createNotepadFile()
        if msg:
            print(f"{addr} : {msg}")

            if (msg == DISCONNECTED_MSG):
                isConnected = False
                conn.send("100".encode(FORMAT))
            elif (msg == "POST"):
                conn.send("300".encode(FORMAT))
                note = conn.recv(SIZE).decode(FORMAT)
                response = fileOperations(msg,note)
                conn.send(response.encode(FORMAT))
            elif (msg == "GET"):
                note = fileOperations(msg)
                conn.send(note.encode(FORMAT))
            elif (msg == "CLEAR"):
                response = fileOperations(msg)
                conn.send(response.encode(FORMAT))
            else:
                conn.send("400".encode(FORMAT))

    conn.close()
    print(f"[ END CONNECTION ] Server Securely Disconnected from {addr}")

# Start the Server 
def Start():

    # Listening on the SERVER 
    print(f"\n[ LISTENING ] Server Is Listening On {IP} : {PORT} \n")
    server.listen()

    while True :
        # Accepting the Connection from Client and storing that Info 
        conn, addr = server.accept()

        # Creating the THREAD for each Client
        thread  = threading.Thread(target=handleClient, args=(conn,addr))
        thread.start()
Start()


'''
# CODES :

1] 100 : Server Disconnected from Client Successfully
2] 200 : Operation Done Successfully (In that case client did not need to send extra message in order to complete the conversation)
3] 201 : Operation Executed Successfully (Data Recieved and Stored Successfully)
4] 202 : Operation Executed Successfully (Cleared all the Notes from server)
4] 300 : POST Request Recieved and all resources are checked, now you can send the data to store.
5] 400 : Bad Request/Command

'''

