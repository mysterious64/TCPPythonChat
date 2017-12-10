class Server_Action:

	def __init__(self, action, data):
		self.action = action
		self.data = data
		self.action_map = {
			
		}

	def handle(self):
		print('Handling action')
