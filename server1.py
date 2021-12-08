import os
import socket
import time
from models import *
import pandas as pd
from utils import *
from create_report import *
import re
import hashlib
from threading import *

PORT = 2223
SERVER = socket.gethostname()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))
HEADER = 1024

server_dir = "./server_data/"

user_dic = {}
live_table = []


def password_check(email, pswd):
    if email in user_dic:
        if user_dic[email] == pswd:
            live_table.append(email)
            return "Login"
        elif user_dic[email] != pswd:
            return "Error"
    else:
        user_dic[email] = pswd
        live_table.append(email)
        return "Signup"

while True:
    server.listen(5)
    print(f"[LISTENING] Server is listening on {SERVER}")
    conn, addr = server.accept()
    print("Connection established with " + str(addr[0]) + ", " + str(addr[1]))
    # email = conn.recv(HEADER).decode()
    # initial = email.split('@')[0]
    # password = conn.recv(HEADER).decode()
    login = False
    while login == False:
        email = conn.recv(HEADER).decode()
        initial = email.split('@')[0]
        password = conn.recv(HEADER).decode()
        password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        pswd_return = password_check(email, password)
        print(pswd_return)
        if pswd_return == "Login" or pswd_return == "Signup":
            conn.send("Thank You!".encode())
            login = True
            break
        else:
            conn.send("Error!".encode())
            login = False


    print(email+password)
    user_dir = os.path.join(server_dir, initial)
    if os.path.isdir(user_dir):
        pass
    else:
        os.mkdir(user_dir)

    

    file_name = f'./server_data/{initial}/received.csv'
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
    print("hello")
    training_ratio = conn.recv(100).decode()
    print(training_ratio)


    df = pd.read_csv(file_name)
    training_points = int(len(df)*int(training_ratio)/100)
    testing_points = len(df) - training_points
    reg_training_model(df, degree = int(degree), split_ratio = int(training_ratio)/100, user_dir = user_dir)

    tot, maxi, mini, mean, medi, sd = stats_summary(df)
    print("model training done......")

    #send 1 image to client
    file_path = f'./server_data/{initial}/fitting.png'
    file_size = os.path.getsize(file_path)
    print(file_size)
    conn.send(str(file_size).encode())


    with open(file_path, "rb") as file:
        c = 0
        # Starting the time capture.
        start_time = time.time()

        # Running loop while c != file_size.
        while c <= file_size:
            data = file.read(1024)
            if not (data):
                break
            conn.sendall(data)
            c += len(data)

        # Ending the time capture.
        end_time = time.time()
    file.close()
    print("[INFO] Fitting image Transfer Complete.Total time: ", end_time - start_time)


    #client "finalising report......"
    # conn.send("finalising report....".encode())

    #file report downloaded. Local path"receivedreport.pdf"


    c_report(tot, maxi, mini, mean, medi, sd, training_points, testing_points, degree, split = training_ratio, user_dir = user_dir)
    print(str(tot))
    print("report generated now")


    file_path = f'./server_data/{initial}/report.pdf'
    file_size = os.path.getsize(file_path)
    print(file_size)
    conn.send(str(file_size).encode())


    with open(file_path, "rb") as file:
        c = 0
        # Starting the time capture.
        start_time = time.time()

        # Running loop while c != file_size.
        while c <= file_size:
            data = file.read(1024)
            if not (data):
                break
            conn.sendall(data)
            c += len(data)

        # Ending the time capture.
        end_time = time.time()
    file.close()
    print("[INFO] Report file Transfer Complete.Total time: ", end_time - start_time)

    live_table.remove(email)
    # Closing the socket.
    conn.close()