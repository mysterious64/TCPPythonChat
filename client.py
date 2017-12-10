#!/usr/bin/env python

import socket
from client_request import Client_Request

TCP_IP = '127.0.0.1'
TCP_PORT = 4713
BUFFER_SIZE = 1024

socket_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_c.connect((TCP_IP, TCP_PORT))
#text = input("Enter Username: ")
#socket_c.send(text.encode('ascii'))
data = socket_c.recv(BUFFER_SIZE)
request = Client_Request(data.decode('ascii'))
#print("received data:", request.data)
request.handle()
