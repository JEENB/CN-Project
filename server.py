import socket
from _thread import *
import pandas as pd
from client import HEADER
from models import *

port = 5545
server_ip = "192.196.1.17"
server_ip = socket.gethostbyname(socket.gethostname())  #gethost name gets the local ip for the server
address = (server_ip, port)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(address)

print('Server is running! (IP Address: %s, Port: %s)' % (server_ip, port)) 

server.listen(4)


welcome_msg = "Welcome! You can start training your model. Enter 1 to proceed, 2 otherwise."


while True:
	client, addr = server.accept()
	print("Connection from: " + str(addr))

	client.send(welcome_msg.encode())
	msg = client.recv(HEADER).decode()
	print(msg)

	
	