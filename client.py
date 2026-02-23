import socket
import sys
import random
import time

CLIENT_IP = "localhost"
CLIENT_PORT = 52964

BUFFER = 1024 # 1KB
FORMAT = "utf-8" # Encoding format

try : 
    # create socket
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket
    client_sock.bind((CLIENT_IP, CLIENT_PORT)) # bind to address and port # passing a tuple (IP, PORT) inside the socket.bind() method
    client_sock.listen(2)
    print("Server is up and running....")


except Exception as e:
    print(f"Error 1: {e}") # print the error message # formated string
    sys.exit()

try:
    while True:
        temp = round(random.uniform(20, 40), 2) # generate a random temperature value between 20 and 40 with 2 decimal places
        sensor_value = str(temp) # convert the temperature value to a string
        client_sock.send(sensor_value.encode(FORMAT)) # send the sensor value to the client encoded in the specified format
        ack_msg = client_sock.recv(BUFFER).decode(FORMAT) # receive the acknowledgment message from the client and decode it
        if not ack_msg:
            print("Server may be down")
            break
        print("Server response: ", ack_msg) # print the acknowledgment message received from the client

        client_sock, client_addr = client_sock.accept() # accept a connection from a client
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
    client_sock.close() # close the server socket
    sys.exit()
                                