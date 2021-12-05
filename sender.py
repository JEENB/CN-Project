import os
import socket
import time


PORT = 2223
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), PORT))
print("[INFO] Connected to server")
file_name = "dataset.csv"
file_size = os.path.getsize(file_name)

print("[INFO] sending file")
client.send(str(file_size).encode())


# Opening file and sending data.
with open(file_name, "rb") as file:
    c = 0
    # Starting the time capture.
    start_time = time.time()

    # Running loop while c != file_size.
    while c <= file_size:
        data = file.read(1024)
        if not (data):
            break
        client.sendall(data)
        c += len(data)

    # Ending the time capture.
    end_time = time.time()

print("[INFO] File Transfer Complete.Total time: ", end_time - start_time)
# Closing the socket.
client.close()