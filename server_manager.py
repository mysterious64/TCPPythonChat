import _thread
from server_client import Server_Client

class Server_Manager:

	def __init__(self, socket):
		print('Server Initiated')
		self.socket = socket
		self.clients = []

	def connect_new_client(self, socket, addr):
		client = Server_Client(socket, addr)
		client.start()
		self.clients.push(client)

	def listen_for_connections(self):
		while True:
			conn, addr = self.socket.accept()
			_thread.start_new_thread(self.connect_new_client, (conn, addr))
		socket.close()
