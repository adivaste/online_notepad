import json
import socket
import sys

IP = "6.tcp.ngrok.io"	#sys.argv[1]
PORT = 17788		#int(sys.argv[2])
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

# Function Can Be performed on notpad
def clearAll(client):

    cmd = "[CLEARA]"
    # Confirming the deletion
    confirm = input("\n:: Are you really want to DELETE All Your Notes ? (y/n)")

    if ((confirm.lower() == "y") or (confirm.lower() == "yes")):   
        client.send(cmd.encode(FORMAT))
   
        response = client.recv(SIZE).decode(FORMAT)
        if response:
            print(":: Deleted All the Notes Successfully")
    elif ((confirm.lower() == "y") or (confirm.lower() == "no")):
        print("\n:: Your Files are SAFE :) ")
    else :
        print("\n:: Please Choose the correct option (yes/y/no/n) ")

def displayAll(client):
    
    cmd = "[SENDCLI]"
    # Sending the request to the server for retriving content on client side
    client.send(cmd.encode(FORMAT))
    
    # Getting a response from Server
    strObj = client.recv(SIZE).decode(FORMAT)		# Response is in the format of JSON-String
    strObj = eval(strObj)				# Single Quoted key, JSON-String is converted to python dictionary ( Python Dict. Support Single Quoted Keynames but JSON requires only Double Quoted Strings so 'eval()' is used to convert into PYTHON DICT.

    strObj = strObj["notes"]				# Accessing the "Notes" Array from Python Dictionary (msg)
    strObj = strObj[::-1]				# Reversing that array to show recent notes to client

    # Printing all the notes
    print("\nYour Notes : ")
    for i in range(len(strObj)):
        print(f"{i+1}) {strObj[i]}")
    print()

def main():
    #Staring a TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connecting to the server.
    client.connect(ADDR)

    # USER INPUT from command line
    if (len(sys.argv) == 2):
        note = sys.argv[1] 
    else:
        print("\n:: Notepad :error : Please Enter Your Note In Double Quotes (\" \")  ")
        print("\n:: Use [ note -h ] command for help.")
        return

    # Checking the inputs and performing various operations accordingly
    if (note=="-a"):
        displayAll(client)
    elif (note=="-ca"):
        clearAll(client)
    else:
        note = "[STORE]" + note
        client.send(note.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        if msg:
            print("\n:: Your Note Saved Successfully !")

    #Closing the connection from the server.
    client.close()

if __name__ == "__main__":
    main()
