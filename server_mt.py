import socket
import threading
import time
import csv

IP = socket.gethostbyname(socket.gethostname())
PORT = 5569
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"


CSV_FILE = "latency.csv"

def log_latency(latency_avg):
    with open(CSV_FILE, mode="a+", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([latency_avg])



def handle_client(conn, addr):
    start_time = time.time()
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        print(f"[{addr}] {msg}")
        msg = f"Msg received: {msg}"
        conn.send(msg.encode(FORMAT))
        connected = False

    conn.close()
    latency = (time.time() - start_time)
    print("AVG:",latency)
    log_latency(latency)
    

def main():
    
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")
    max_active = 0

    while True:
        conn, addr = server.accept()
        
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        if max_active < threading.activeCount() - 1:
            max_active = threading.activeCount() - 1
        
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        print("Max Active connections:", max_active)

        #save to csv file and show an active server graph

if __name__ == "__main__":
    main()