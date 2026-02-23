import socket
import sys
import random
import time

SERVER_IP = "localhost"
SERVER_PORT = 54321
BUFFER = 1024 # 1KB
FORMAT = "utf-8" # Encoding format

try : 
    # create socket
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket
    client_sock.connect((SERVER_IP, SERVER_PORT)) # bind to address and port # passing a tuple (IP, PORT) inside the socket.bind() method
    print("Client connected with the server")

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
        time.sleep(2)# wait for 5 seconds before sending the next sensor value
        
except Exception as e:
    print(f"Error 2: {e}") # print the error message
except KeyboardInterrupt:
    print("Server is closed")
    client_sock.close() # close the server socket
    sys.exit()
                                