from server_action import Server_Action

class Server_Request:
	def __init__(self, data, client):
		self.data = data
		self.client = client

	def handle(self):
		command, parameters = self.data.split(';', 1)
		print('Handling Server Action: ',  command, ' Parameters: ', parameters)
		action = Server_Action(command, parameters, self.client)
		response = action.handle()
		print('Response: ', response)
		return response
