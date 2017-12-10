from client_request import Client_Request
import _thread
import threading

class Client_Manager:

	def __init__(self, socket):
		self.socket = socket
		self.connected = False

	def start(self):
		self.listen_for_user_authentication()

	def listen_for_user_authentication(self):
		while True:
			if self.connected:
				self.handle_connected()
				break
			else:
				data = self.socket.recv(1024)
				request = Client_Request(data.decode('ascii'), self)
				response = request.handle()
				if response == 'CLIENT_CONNECTED':
					continue
				self.socket.send(response.encode('ascii'))

	def handle_connected(self):
		#_thread.start_new_thread(self.listen_for_server_messages())
		threading.Thread(target=self.listen_for_server_messages, name='Message_stream').start()
		#_thread.start_new_thread(self.listen_for_user_input())
		threading.Thread(target=self.listen_for_user_input, name='User_stream').start()

	def listen_for_server_messages(self):
		print('Listening')
		while True:
			data = self.socket.recv(1024)
			print('New Data ', data)
			request = Client_Request(data.decode('ascii'), self)
			response = request.handle()
			if response == '':
				continue
			elif response == None:
				continue
			elif response == 'CLIENT_CLOSE':
				break
			self.socket.send(response.encode('ascii'))
		self.socket.close()

	def listen_for_user_input(self):
		print('Waiting input')
		while True:
			request = Client_Request('NEW_ACTION;', self)
			response = request.handle()
			self.socket.send(response.encode('ascii'))
			if response == 'CLIENT_EXIT;':
				break
