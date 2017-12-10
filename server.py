#!/usr/bin/env python

import socket
from server_manager import Server_Manager

#print('a') Test for server operation
TCP_IP = '127.0.0.1'
TCP_PORT = 4713

#create basic socket
socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_s.bind((TCP_IP, TCP_PORT))
#set server to only listen for 10 people
socket_s.listen(10)
#instantiate server management
server = Server_Manager(socket_s)
server.listen_for_connections()
