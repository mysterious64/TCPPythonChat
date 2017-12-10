from server_request import Server_Request

class Server_Client:

	def __init__(self, socket, addr):
		self.socket = socket
		self.addr = addr
		#user properties
		self.logged_in = False
		self.username = ''
		self.people_map = {
			'John' : 'joe',
			'Jill' : 'jane'
		}

	def start(self):
		self.socket.send(b'AUTHENTICATE;')
		while True:
			data = self.socket.recv(1024).decode('ascii')
			request = Server_Request(data, self)
			response = request.handle()
			self.socket.send(response.encode('ascii'))
		self.socket.close()
