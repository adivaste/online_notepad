from socket import *
import threading
import urllib.request
import json
import os
from mega import Mega
import time

def startNGROKServer():
    print("NGROK")
    # os.system("wget -q -c -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
    # os.system("unzip -qq -n ngrok-stable-linux-amd64.zip")
    os.system("chmod 777 ngrok")
    os.system("./ngrok authtoken 2AZ6Q4rkOlX4Lk8Wyl2p6LeSzm5_86zUyKaEBTBdMDf9nrQjV")
    os.system("./ngrok tcp 5050")

def storeResult():
    time.sleep(0.3)
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
        usr = m.login("coding01ninjas@yopmail.com","Bhaibhai45")
        usr.upload("host_port.txt")
        print("Uploaded..................")

x = threading.Thread(target=startNGROKServer)
y = threading.Thread(target=storeResult)
