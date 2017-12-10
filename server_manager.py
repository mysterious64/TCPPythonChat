import _thread
from server_request import Server_Request

class Server_Manager:

	def __init__(self, socket):
		print('Server Initiated')
		self.socket = socket

	def connect_new_client(self, socket, addr):
		socket.send(b'AUTHENTICATE;')
		while True:
			data = socket.recv(1024).decode('ascii')
			request = Server_Request(data)
			response = request.handle()
			socket.send(response.encode('ascii'))
		socket.close()

	def listen_for_connections(self):
		while True:
			conn, addr = self.socket.accept()
			_thread.start_new_thread(self.connect_new_client, (conn, addr))
		socket.close()
