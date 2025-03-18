from pypresence import Presence
import time
name = input("Input Minecraft Name: ")
server = input("Input Server IP e.g cavepvp.org: ")
version = input("Minecraft Version e.g 1.8.9")

CLIENT_ID = "CLIENTID" # Replace this with your application's client ID from the Discord Developer Portal

RPC = Presence(CLIENT_ID)
RPC.connect()
# Update presence
RPC.update(
    state=f'{server}',  
    details="Playing LabyMod",  
    large_image="logo",
    large_text=f"Minecraft {version} - LabyMod v2.1.10",
    small_image="enderman",
    small_text=f'{name}',  
    start=time.time()  
)

print("Discord RPC is running...")
try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    print("Stopping RPC...")
    RPC.close()
