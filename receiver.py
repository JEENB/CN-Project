
import os
import socket
import time

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