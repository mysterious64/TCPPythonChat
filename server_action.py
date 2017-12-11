class Server_Action:

	def __init__(self, action, data, client):
		self.action = action
		self.data = data
		self.client = client
		self.action_map = {
			'AUTHENTICATE_USER': self.handle_authenticate_user,
			'AUTHENTICATE_PASS': self.handle_authenticate_pass,
			'BROADCAST': self.handle_broadcast,
			'DISCONNECT' : self.handle_disconnect,
			'JOIN' : self.handle_channel,
			'LIST' : self.handle_list,
			'MESSAGE' : self.handle_msg,
			'USER_LIST' : self.handle_online
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

	def handle_disconnect(self):
		self.client.disconnect('DISCONNECT;')

	def handle_channel(self):
		self.client.join(self.data)

	def handle_list(self):
		self.client.list(self.data)

	def handle_msg(self):
		self.client.msg(self.data)

	def handle_online(self):
		self.client.online(self.data)
