class Client_Action:

	def __init__(self, action, data):
		self.action = action
		self.data = data
		self.action_map = {
                	'AUTHENTICATE': self.handle_authenticate ,
			'AUTHENTICATE_PASS' : self.handle_authenticate_pass ,
			'AUTHENTICATE_USER' : self.handle_reauthenticate ,
			'AUTHENTICATE_USER_PASS' : self.handle_pass_fail ,
			'BAD_REQUEST' : self.handle_bad_request ,
			'USER_AUTHENTICATED' : self.handle_authenticated
        	}
		self.user_action_map = {
			'HELP' : self.handle_user_help ,
			'JOIN' : self.handle_user_join ,
			'USERS' : self.handle_user_list ,
			'CHANNEL' : self.handle_user_channel,
			'MSG' : self.handle_user_msg
		}

	def handle(self):
		return self.action_map[self.action]()

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
		os.system('cls')
		print('You have successfully connected to the chatroom')
		return self.handle_input()

	def handle_bad_request(self):
		print('Bad action: ', self.action)
		print('Client Failure')
		return 'CLIENT_CLOSE'

	def handle_input(self):
		input = Input('>')
		return self.handle_user_input(input)

	def handle_user_input(self, input):
		action, text = input.split(' ', 1)
		action = action.upper
		if action in self.user_action_map:
			return self.user_action_map[action](text)
		else:
			print('Unsupported action, type HELP for actions')
		return self.handle_input()

	def handle_user_help(self, text):
		print('Supported Commands:')
		for command in self.user_action_map:
			print(command)
		return self.handle_input()
