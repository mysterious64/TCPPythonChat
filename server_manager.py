import _thread
from server_client import Server_Client

class Server_Manager:

	def __init__(self, socket):
		print('Server Initiated')
		self.socket = socket
		self.clients = []

	def connect_new_client(self, socket, addr):
		client = Server_Client(socket, addr, self)
		self.clients.append(client)
		client.start()

	def listen_for_connections(self):
		while True:
			conn, addr = self.socket.accept()
			_thread.start_new_thread(self.connect_new_client, (conn, addr))
		socket.close()

	def broadcast(self, text):
		print('Broadcasting ' , text)
		print('Clients ', self.clients)
		for client in self.clients:
			print('Checking ', client.username)
			if client.logged_in:
				print('Broadcasting to ', client.username)
				client.socket.send(text.encode('ascii'))
