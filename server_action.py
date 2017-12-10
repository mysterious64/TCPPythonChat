class Server_Action:

	def __init__(self, action, data, client):
		self.action = action
		self.data = data
		self.client = client
		self.action_map = {
			'AUTHENTICATE_USER': self.handle_authenticate_user,
			'AUTHENTICATE_PASS': self.handle_authenticate_pass,
			'BROADCAST': self.handle_broadcast
		}

	def handle(self):
		if self.action in self.action_map:
			return self.action_map[self.action]()
		else:
			print(self.action, ' is an unsupported action')
			return 'BAD_REQUEST;' 

	def handle_authenticate_user(self):
		if self.data in self.client.people_map:
			self.client.username = self.data
			return 'AUTHENTICATE_PASS;'
		else:
			return 'AUTHENTICATE_USER;'

	def handle_authenticate_pass(self):
		if self.client.username in self.client.people_map:
			password = self.client.people_map[self.client.username]
			if self.data == password:
				self.client.logged_in = True
				return 'USER_AUTHENTICATED;'
			else:
				return 'AUTHENTICATE_USER_PASS;'
		else:
			return 'AUTHENTICATE_USER_PASS;'

	def handle_broadcast(self):
		self.client.broadcast('BROADCAST;' +self.data)
