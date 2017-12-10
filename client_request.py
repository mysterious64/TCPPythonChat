from client_action import Client_Action

class Client_Request:
	def __init__(self, data):
		self.data = data

	def handle(self):
		command, parameters = self.data.split(";", 1)
		print('Handling Request Action: ', command, ' Parameters: ', parameters)
		action = Client_Action(command, parameters)
		response = action.handle() 
		print('Response: ', response)
		return response
