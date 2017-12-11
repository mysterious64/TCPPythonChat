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
		socket.shutdown(SHUT_RWDR)
		socket.close()

	def broadcast(self, text, channel, name):
		print('Broadcasting ' , text)
		action, message = text.split(';', 1)
		response = action + ';' +  channel + '/ ' + name + ': ' + message
		print('Clients ', self.clients)
		for client in self.clients:
			print('Checking ', client.username)
			if client.logged_in:
				if client.channel == channel:
					print('Broadcasting to ', client.username)
					client.socket.send(response.encode('ascii'))

	def message(self, text, sender, reciever):
		print('Messaging ' , text)
		print('Clients ', self.clients)
		action, message = text.split(';',1)
		for client in self.clients:
			print('checking ', client.username)
			if client.logged_in:
				if client.username in reciever:
					print('Messaging to ', client.username)
					response = action + ';' + sender + ' -> ' + client.username + ' ' + message
					client.socket.send(response.encode('ascii'))


	def list(self):
		channels = []
		for client in self.clients:
			print('checking client: ' +client.username)
			if client.channel:
				print(client.username + ' is in ' + client.channel)
				if client.channel not in channels:
					channels.append(client.channel)
		return channels

	def users(self):
		users = []
		for client in self.clients:
			print('checking client: ' + client.username)
			if client.logged_in:
				users.append(client.username)
		return users
