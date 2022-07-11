import os
import time

def startNGROKServer():
    
    # Searching for "ngrok" binary file
    currFolderFiles = os.listdir()
    if "ngrok" not in currFolderFiles:
        os.system("wget -q -c -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
        os.system("unzip -qq -n ngrok-stable-linux-amd64.zip")
        print(" [ NGROK ] :: Installed NGROK Successfully !")
        
    # Providing the execution permission to "ngrok"
    os.system("chmod 777 ngrok")
    
    # Setting up authentication token
    os.system("./ngrok authtoken 2AZ6Q4rkOlX4Lk8Wyl2p6LeSzm5_86zUyKaEBTBdMDf9nrQjV")
    
    # Starting TCP using NGROK on PORT:5050 
    os.system("./ngrok tcp 5050")
    print(" [ NGROK ] :: Server is Running...")
