import socket

HEADER = 5096

port = 5545
server = "192.168.1.17"
server_address = (server,port)

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(server_address)


while True:
	msg = client_socket.recv(HEADER).decode()
	print(msg)
	if msg[0] == "W": ## i.e welcome msg
		reply = input()
		while reply not in [1,2]:
			print("Invalid Option Selected!!")
			reply = input()
		client_socket.send(reply.encode())

# #read input from file
# file = open('dataset.csv', 'r')
# data = file.read()


# #send file name to server


# #send file content to server
 





