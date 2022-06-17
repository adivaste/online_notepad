from socket import *
import threading
import urllib.request
import json
import os
from mega import Mega
import time

def startNGROKServer():

    print("NGROK")
    
    # Searching for "ngrok" binary file
    currFolderFiles = os.listdir()
    if "ngrok" not in currFolderFiles:
        os.system("wget -q -c -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
        os.system("unzip -qq -n ngrok-stable-linux-amd64.zip")
        
    # Providing the execution permission to "ngrok"
    os.system("chmod 777 ngrok")
    
    # Setting up authentication token
    os.system("./ngrok authtoken 2AZ6Q4rkOlX4Lk8Wyl2p6LeSzm5_86zUyKaEBTBdMDf9nrQjV")
    
    # Starting TCP using NGROK on PORT:5050 
    os.system("./ngrok tcp 5050")

def storeResult():
    
    # Waiting for some time to start NGROK server 
    time.sleep(0.5)
    print("Result are storing...")

    host = ""
    port = ""

    with urllib.request.urlopen('http://localhost:4040/api/tunnels') as response:
        data = json.loads(response.read().decode())
        (host, port) = data['tunnels'][0]['public_url'][6:].split(':')
        with open("host_port.txt","w") as f:
            f.write(f"Host : {host}\n")
            f.write(f"Port : {port}")

        m = Mega()
        usr = m.login("online45notepad@yopmail.com","Online45note")
        usr.upload("host_port.txt")
        print("Uploaded Host_port.txt ...")

# Creating the two threads
x = threading.Thread(target=startNGROKServer)
y = threading.Thread(target=storeResult)
