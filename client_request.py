from client_action import Client_Action

class Client_Request:
	def __init__(self, data, client):
		self.data = data
		self.client = client

	def handle(self):
		command = ' '
		parameters = ' '
		try:
			command, parameters = self.data.split(";", 1)
		except:
			command = self.data
		print('Handling Request Action: ', command, ' Parameters: ', parameters)
		action = Client_Action(command, parameters, self.client)
		response = action.handle() 
		print('Response: ', response)
		return response
