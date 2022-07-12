import os

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
    os.system("./ngrok authtoken 2Bo8nIhSv0NnDtMO07hTDpVwNMX_5Yfa7pJd4epFfRp3k6wCF")

    # Starting TCP using NGROK on Given PORT
    os.system("./ngrok tcp 5050")

portForwardNGROK()
