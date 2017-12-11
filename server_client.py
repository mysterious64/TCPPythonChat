from server_request import Server_Request

class Server_Client:

	def __init__(self, socket, addr, server):
		self.socket = socket
		self.addr = addr
		self.server  = server
		#user properties
		self.logged_in = False
		self.username = ''
		self.people_map = {
			'John' : 'joe',
			'Jill' : 'jane'
		}
		self.channel = None

	def start(self):
		self.socket.send(b'AUTHENTICATE;')
		while True:
			data = self.socket.recv(1024).decode('ascii')
			request = Server_Request(data, self)
			response = request.handle()
			if response == None:
				continue
			if response == 'CLIENT_CLOSE;':
				self.socket.send(response.encode('acsii'))
				break
			self.socket.send(response.encode('ascii'))
		self.socket.shutdown(SHUT_RWDR)
		self.socket.close()

	def broadcast(self, text):
		if self.channel != None:
			self.server.broadcast(text, self.channel, self.username)
		else:
			response = 'NOCHANNEL;'
			return self.socket.send(response.encode('ascii'))

	def msg(self, text):
		try:
			name, message = text.split(' ', 1)
			self.server.message(message, self.username, name)
		except:
			response = 'NOPERSON;'
			return self.socket.send(response.encode('ascii'))

	def join(self, text):
		self.channel = text

	def list(self, text):
		channels = self.server.list()
		response = 'LIST;' + (', '.join(channels))
		print('channel list ' +response)
		return self.socket.send(response.encode('ascii'))

	def disconnect(self, text):
		self.logged_in == False
		response = 'CLIENT_CLOSE;'
		return response

	def online(self, text):
		users = self.server.users()
		response = 'USER_LIST;' + (', '.join(users))
		print('user list ' + response)
		return self.socket.send(response.encode('ascii'))
