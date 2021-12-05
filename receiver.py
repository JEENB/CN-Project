<<<<<<< HEAD
# This file will be used for recieving files over socket connection.
=======

>>>>>>> a5eb0ee006fc01cb20802a3fe712408b920c3eb8
import os
import socket
import time

<<<<<<< HEAD
host = input("Host Name: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Trying to connect to socket.
try:
    sock.connect((host, 22222))
    print("Connected Successfully")
except:
    print("Unable to connect")
    exit(0)

# Send file details.
file_name = sock.recv(100).decode()
file_size = sock.recv(100).decode()

# Opening and reading file.
with open("./1" + file_name, "wb") as file:
    c = 0
    # Starting the time capture.
    start_time = time.time()

    # Running the loop while file is recieved.
    while c <= int(file_size):
        data = sock.recv(1024)
        if not (data):
            break
        file.write(data)
        c += len(data)

    # Ending the time capture.
    end_time = time.time()

print(file)

print("File transfer Complete.Total time: ", end_time - start_time)

# Closing the socket.
sock.close()
=======
PORT = 2223
SERVER = socket.gethostname()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))


while True:
    server.listen(5)
    print(f"[LISTENING] Server is listening on {SERVER}")
    conn, addr = server.accept()
    print("Connection established with " + str(addr[0]) + ", " + str(addr[1]))

    file_name = 'receivedfile.csv'
    file_size = conn.recv(100).decode()

    # Opening and reading file.
    with open(file_name, "wb") as file:
        c = 0
        # Starting the time capture.
        start_time = time.time()

        # Running the loop while file is recieved.
        while c <= int(file_size):
            data = conn.recv(1024)
            if not (data):
                break
            file.write(data)
            c += len(data)

        # Ending the time capture.
        end_time = time.time()

    print("File transfer Complete.Total time: ", end_time - start_time)

    # Closing the socket.
    conn.close()
>>>>>>> a5eb0ee006fc01cb20802a3fe712408b920c3eb8
