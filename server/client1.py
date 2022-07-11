import socket
import json
import time
import sys
import os

# --------------------- A L L   C O N S T A N T S --------------------------

FORMAT = "utf-8"
DISCONNECTED_MSG = "! DISCONNECTED"
SIZE = 1024
TEMP_DATABASE = {}
CMDL_ARGS = sys.argv

# PORT AND IP 
PORT = 5050
IP =  "127.0.1.1"
ADDR = (IP,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# ----------------------- F U N C T I O N S -------------------------------
'''
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
'''
# ---------------------
def get():
    PROTOCALL = "GET"
    client.send(PROTOCALL.encode(FORMAT))
    string_of_json = client.recv(SIZE).decode(FORMAT)
    TEMP_DATABASE = json.loads(string_of_json)
    print(TEMP_DATABASE)
    return TEMP_DATABASE
def post(msg):
    PROTOCALL = "POST"
    client.send(PROTOCALL.encode(FORMAT))

    response1 = client.recv(SIZE).decode(FORMAT)
    if (response1 == "300"):
        client.send(msg.encode(FORMAT))
        response2 = client.recv(SIZE).decode(FORMAT)
        return (response2 == "201")
    else:
        return 0
def clear():
    PROTOCALL = "CLEAR"
    client.send(PROTOCALL.encode(FORMAT))
    response = client.recv(SIZE).decode(FORMAT)
    return (response == "202")

def disconnect():
    client.close()

def help():
    msg  = '''
----------------------------------------------------------------------------------------------
# COMMANADS :

* FORMAT -
note [-OPTIONS-] [-OPTIONS-]

* OPTIONS -
1. [String]             : Any String Within Double Quotes, that will be inserted into NOTEPAD

2. -r -a                : Remove All the notes from the "ONLINE NOTEPAD"
3. -r -no.              : Remove the perticular Note from NOTEPAD with given index

4. -s -a                : Show All the Notes present in the NOTEPAD
5. -s                   : Show 10 recent note (By Default)
6. -s -no.              : Show recent notes of given number

7. -up -filename.txt    : Upload the notes as a file.(*)
8. -help                : How to use the commnads

* EXTRA'S -
(*) - Coming Soon (Bulid In Progress)
----------------------------------------------------------------------------------------------

'''
    print(msg)

def getNotesArray(num=0):
    json_notes_obj = get()
    if json_notes_obj:
        notes_arr = json_notes_obj["notes"]
        notes_arr.reverse()
        notes_arr_len = len(notes_arr)

        if (num !=0):
            return notes_arr[:num]
        else:
            return notes_arr
    else:
        print("\n:: Notepad- Error In Retriving The Data !\n")
        return []
#-----------------------
def main():

    # If No argument passed 
    if (len(CMDL_ARGS) == 1):
        help()

    # Showing the notes
    elif ((len(CMDL_ARGS) >= 2) and (CMDL_ARGS[1]) == "-s" ):

        # Show All Notes
        notes_arr = []

        if (len(CMDL_ARGS) == 2):
            notes_arr_len = len(notes_arr)
        elif (CMDL_ARGS[2] == "-a"):
            notes_arr = getNotesArray()
        elif (CMDL_ARGS[2].isnumeric()):
            num = int(CMDL_ARGS[2])
            notes_arr = getNotesArray(num)
        else :
            print("\n:: Notepad - Please Enter The Commands Correctly !")
            return

        notes_arr_len = len(notes_arr)
        print("\n* Your Notes : \n")
        for i in range(notes_arr_len):
            print(str(i+1) + ") " + notes_arr[i])

    # Removing the notes
    elif ((len(CMDL_ARGS) == 3) and (CMDL_ARGS[1]) == "-r" ):
        if (CMDL_ARGS[2] == "-a"):
            clear()
        else:
            print("\n:: Notepad - Please Enter The Commands Correctly !")

    elif (CMDL_ARGS[1] == "-h"):
        help()

    # Giving Error Message 
    else:
        print("\n:: Notepad - Please Enter The Commands Correctly !")

    # Disconnect From Server
    disconnect()
main()
