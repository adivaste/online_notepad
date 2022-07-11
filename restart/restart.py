import requests

url = "https://first-repo.itsadi45.repl.co/host"

try:
	print("\n :: Connecting to the Server...")
	urlObj = requests.get(url)
	host_port  = eval(urlObj.text)
except:
	print("\n :: Unable to connect the Server !")

host = host_port["host"]
port = int(host_port["port"])
print(" :: Connected !")

note_file = f'''#!/bin/bash
host="{host}"
port={port}

python3 client.py $host $port "$@"
'''

with open("note","w") as f:
	print(" :: Modifying Executable Files...")
	f.write(note_file)

