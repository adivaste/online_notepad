import threading
import time
import os

os.system("cd server")

def runNGROK():
    os.system("python3 ngrokServer.py")
def runFile():
    os.system("python3 server.py")

thread1 = threading.Thread(target=runFile)
thread2 = threading.Thread(target=runNGROK)

thread1.start()
time.sleep(5)
print("NGROK GOINF TOSTART")
thread2.start()
