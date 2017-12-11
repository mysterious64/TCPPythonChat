import os

class Client_Action:

	def __init__(self, action, data, client):
		self.action = action
		self.data = data
		self.client = client
		self.action_map = {
                	'AUTHENTICATE': self.handle_authenticate ,
			'AUTHENTICATE_PASS' : self.handle_authenticate_pass ,
			'AUTHENTICATE_USER' : self.handle_reauthenticate ,
			'AUTHENTICATE_USER_PASS' : self.handle_pass_fail ,
			'BAD_REQUEST' : self.handle_bad_request ,
			'BROADCAST' : self.handle_broadcast,
			'CLIENT_CLOSE' : self.handle_user_close ,
			'DISCONNECT' : self.handle_user_close ,
			'LIST' : self.handle_list ,
			'MESSAGE_R' : self.handle_message ,
			'NEW_ACTION' : self.handle_input ,
			'NOCHANNEL' : self.handle_no_channel,
			'USER_AUTHENTICATED' : self.handle_authenticated,
			'USER_LIST' : self.handle_online
        	}
		self.user_action_map = {
			'CHANNEL' : self.handle_user_channel,
			'HELP' : self.handle_user_help ,
			'JOIN' : self.handle_user_join ,
			'LEAVE' : self.handle_user_disconnect ,
			'LIST' : self.handle_user_list ,
			'MSG' : self.handle_user_msg ,
			'USERS' : self.handle_user_online
		}

	def handle(self):
		if self.action in self.action_map:
			return self.action_map[self.action]()
		else:
			return ''
	#Response Handler

	def handle_authenticate(self):
		username = input('Enter username: ')
		return 'AUTHENTICATE_USER;' + username

	def handle_reauthenticate(self):
		print('User not found')
		return self.handle_authenticate()

	def handle_authenticate_pass(self):
		password = input('Enter Password: ')
		return 'AUTHENTICATE_PASS;' + password

	def handle_pass_fail(self):
		print('Incorrect Password')
		return self.handle_authenticate()

	def handle_authenticated(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		self.client.connected = True
		print('You have successfully connected to the chatroom')
		return 'CLIENT_CONNECTED'

	def handle_bad_request(self):
		print('Bad action: ', self.action)
		print('Client Failure')
		return self.handle_close()

	def handle_close(self):
		return 'CLIENT_CLOSE'

	def handle_user_close(self):
		print('Server connection closed.')
		return self.handle_close()

	def handle_input(self):
		user_input = input('>')
		return self.handle_user_input(user_input)

	def handle_broadcast(self):
		print(self.data)

	def handle_no_channel(self):
		print('Not in any channel. Please join or create a channel before sending any messages')

	def handle_list(self):
		if self.data:
			print('Channel List:')
			print(self.data)
		else:
			print('No open channels')

	def handle_online(self):
		print('Online Users:')
		print(self.data)

	def handle_message(self):
		print(self.data)

	#User Handlers

	def handle_user_input(self, input):
		action = ' '
		text = ' '
		try:
			action, text = input.split(' ', 1)
			action = action.upper()
		except:
			action = input.upper()
		if action in self.user_action_map:
			return self.user_action_map[action](text)
		else:
			print('Unsupported action, type HELP for actions: ', action)
		return self.handle_input()

	def handle_user_help(self, text):
		print('Supported Commands:')
		for command in self.user_action_map:
			print(command)
		return self.handle_input()

	def handle_user_join(self, text):
		text = text.upper()
		return 'JOIN;' +text

	def handle_user_list(self, text):
		return 'LIST;' +text

	def handle_user_channel(self, text):
		return 'BROADCAST;' +text

	def handle_user_msg(self, text):
		return 'MESSAGE;' +text

	def handle_user_disconnect(self, text):
		return 'DISCONNECT;'

	def handle_user_online(self, text):
		return 'USER_LIST;'
