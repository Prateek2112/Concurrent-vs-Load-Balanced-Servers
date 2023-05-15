
import sys
import time
import socket
import csv


IP = socket.gethostbyname(socket.gethostname())
PORT = int(sys.argv[1])
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
CSV_FILE = f"latency_{PORT}.csv"

# Function to handle the client request
def handle_client(conn: socket, addr):
    
    # Get the start time
    start_time = time.time()
    print(f"[NEW CONNECTION] {addr} connected.")

    # Receive the incoming data from client
    msg = conn.recv(SIZE).decode(FORMAT)
    print(f"[{addr}] {msg}")
    try:
        conn.send(msg.encode(FORMAT))
    except:
        # If client disconnects before receiving data
        # Then connect to client and try sending the data again
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(addr)
        conn.send(msg.encode(FORMAT))

    # Close the connection
    conn.close()

    # Get the latency of this client request
    latency = time.time() - start_time
    # Store the latency in csv
    with open(CSV_FILE, "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([latency])


def main():
    print("[STARTING] Server is starting...")
    # Setup the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Listen on port for incoming connections
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")
    while True:
        # Accept incoming connections
        conn, addr = server.accept()
        handle_client(conn, addr)


if __name__ == "__main__":
    main()