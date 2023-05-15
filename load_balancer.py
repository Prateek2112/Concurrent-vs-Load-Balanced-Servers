
import socket
import json
import pandas as pd


IP = socket.gethostbyname(socket.gethostname())
PORT = 8080
ADDR = (IP, PORT)
AVAIL_PORTS = [8000, 8001, 8002]
SIZE = 1024
FORMAT = "utf-8"

current_port = 0

# Setup server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP, PORT))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Listen port for incoming connections
sock.listen(5)
print(f"[LISTENING] Server is listening on {IP}:{PORT}")

try:
    while True:
        # Accept incoming connection
        client_sock, client_addr = sock.accept()
        print("Received connection from", client_addr)

        # Select the server based on round robin approach
        current_port = (current_port + 1) % len(AVAIL_PORTS)
        new_addr = (IP, AVAIL_PORTS[current_port])
        
        # Convert the address tuple to json
        new_addr_json = json.dumps(new_addr)
        # Send the json to the client
        client_sock.sendall(new_addr_json.encode())

        # Close the connection
        client_sock.close()
finally:
    # Calculate average latency of all servers before exiting the program
    avg = []
    try:
        for port in AVAIL_PORTS:
            df = pd.read_csv(f"latency_{port}.csv", header = None)
            avg.append(df[0].mean())
        print(f"\nThe average latency is: {(sum(avg)/len(avg))*1000} ms\n")
    except:
        pass