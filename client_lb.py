
import socket
import sys
import threading
import json

# If IP address is not passed in the command line argument 
# Then use local machine address
IP = socket.gethostbyname(socket.gethostname())
if len(sys.argv) > 2:
    IP = sys.argv[2]

PORT = 8080
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"


# Function for connection and communication to and from server
def connect_server(addr, msg = None):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

    client.send(msg.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER] '{msg}'")

    client.close()


def main():
    # If number of connections is not passed in command line argument 
    # Then default to 10 connections
    number_of_connections = 10
    if ((len(sys.argv) > 1) and int(sys.argv[1]) > 0):
        number_of_connections = int(sys.argv[1])
    
    threads = []
    for i in range(number_of_connections):

        # Setup socket for server connection
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the load-balancing server
        client.connect(ADDR)

        # Receive the alternate address
        json_string = ""
        while True:
            data = client.recv(SIZE)
            if not data:
                break
            json_string += data.decode()
        addr = tuple(json.loads(json_string))
        client.close()
        
        i = str(i)
        # Send request to server on a new thread
        thread = threading.Thread(target=connect_server, args=(addr, i))
        thread.start()
        threads.append(thread)


    for x in threads:
        x.join()

if __name__ == "__main__":
    main()

