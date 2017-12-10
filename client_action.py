class Client_Action:

	def __init__(self, action, data):
		self.action = action
		self.data = data
		self.action_map = {
                	'AUTHENTICATE': self.handle_authenticate
        	}

	def handle(self):
		print('Handling action')
		return self.action_map[self.action]()

	def handle_authenticate(self):
		username = input('Enter username: ')
		return 'AUTHENTICATE_USER;'+username
