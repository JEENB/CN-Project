
import os
import socket
import time
from models import *
import pandas as pd

PORT = 2223
SERVER = socket.gethostname()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

while True:
    server.listen(5)
    print(f"[LISTENING] Server is listening on {SERVER}")
    conn, addr = server.accept()
    print("Connection established with " + str(addr[0]) + ", " + str(addr[1]))

    file_name = 'received.csv'
    file_size = conn.recv(100).decode()
    print(file_size)
    # Opening and reading file.
    # with open(file_name, "wb") as file:
    file = open(file_name, "wb")
    c = 0
    # Starting the time capture.
    start_time = time.time()

    # Running the loop while file is recieved.
    while c < int(file_size):
        data = conn.recv(1024)
        if not (data):
            break
        file.write(data)
        c += len(data)
    file.close()

    # Ending the time capture.
    end_time = time.time()


    print("File transfer Complete.Total time: ", end_time - start_time)


    #receive info about model training from client
    degree = conn.recv(100).decode()
    print(degree)
    training_ratio = conn.recv(100).decode()
    print(training_ratio)


    df = pd.read_csv(file_name)
    reg_training_model(df, degree = int(degree), split_ratio = int(training_ratio)/100 )
    

    # Closing the socket.
    conn.close()