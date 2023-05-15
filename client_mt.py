import socket
import sys
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 5569
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def connection_client(msg = None):
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

    connected = True
    while connected:

        client.send(msg.encode(FORMAT))

        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER] {msg}")
        connected = False
            
    client.close()
    

def main():
    number_of_connections = int(sys.argv[1])
    threads = []
    for i in range(number_of_connections):

        i = str(i)
        thread = threading.Thread(target=connection_client, args=(i, ))
        thread.start()
        threads.append(thread)

    for x in threads:
        x.join()
    

if __name__ == "__main__":
    main()

