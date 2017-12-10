#!/usr/bin/env python

import socket

print('a')
TCP_IP = '127.0.0.1'
TCP_PORT = 4713
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)

conn, addr = s.accept()
#print('Connection address:', addr)
conn.send(b'AUTHENTICATE;')
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: continue
	print("received data: ", data.decode('ascii'))
	conn.send(data)  # echo

