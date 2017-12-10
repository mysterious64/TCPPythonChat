class Server_Request:
	def __init__(self, data):
		self.data = data

	def handle(self):
		print('Handling Server Request')
