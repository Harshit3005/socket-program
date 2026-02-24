# TCP Server

import socket
import threading
import json
from datetime import datetime

# server credential 
SERVER_IP = "localhost"
SERVER_PORT = 54321

# variables 
BUFFER = 1024
FORMAT = "utf-8"
LOG_FILE = "sensor_log.txt"

# client handler thread
def handle_client(client_sock, client_addr):
    try:
        while True:
        # receive data from client 
            data = client_sock.recv(BUFFER)
            if data:
                payload = json.loads(data.decode(FORMAT))
                client_id = payload["client_id"]
                timestamp = payload["timestamp"]
                avg_value = payload["average_value"]
                log_entry = (
                    f"{datetime.now()}, "
                    f"ClientIP={client_addr[0]}, "
                    f"Port={client_addr[1]}, "
                    f"ClientID={client_id}, "
                    f"AvgValue={avg_value}\n"
                )
            with open(LOG_FILE, "a") as f:
                f.write(log_entry)
            print("Logged:", log_entry.strip())
            client_sock.send("OK".encode(FORMAT))
    except Exception as e:
        print("Client handling error:", e)
    finally:
        client_sock.close()

# server socket creation 
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((SERVER_IP, SERVER_PORT))
server_sock.listen(15)

print(f"Server running on port {SERVER_PORT}...")

try:
    while True:
        # accept client connection 
        client_sock, client_addr = server_sock.accept()
        # create and start the client thread
        thread = threading.Thread(
            target=handle_client,
            args=(client_sock, client_addr)
        )
        thread.start()
except Exception as e:
    print(f"Error in client connection: {e}")
except KeyboardInterrupt:
    print("server is closed")
    server_sock.close()