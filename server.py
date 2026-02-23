import socket
import sys

SERVER_IP = "localhost"
SERVER_PORT = 54321
BUFFER = 1024 # 1KB
FORMAT = "utf-8" # Encoding format

try : 
    # create socket
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket
    server_sock.bind((SERVER_IP, SERVER_PORT)) # bind to address and port # passing a tuple (IP, PORT) inside the socket.bind() method
    server_sock.listen(2)
    print("Server is up and running....")



except Exception as e:
    print(f"Error 1: {e}") # print the error message # formated string
    sys.exit()

try:
    while True:
        client_sock, client_addr = server_sock.accept() # accept a connection from a client
        print(f"Client connected from {client_addr[0]}:{client_addr[1]}") # print the client's IP and port number
        data = client_sock.recv(BUFFER).decode(FORMAT) # receive data from the client and decode it
        if not data:
            print("Client may be closed") 
            break
        print(f"Data received : {data}") # print the received data
        client_sock.send("OK".encode(FORMAT))
except Exception as e:
    print(f"Error 2: {e}") # print the error message
except KeyboardInterrupt:
    print("Server is closed")
    server_sock.close() # close the server socket
    sys.exit()
                                