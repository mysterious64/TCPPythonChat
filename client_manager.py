from client_request import Client_Request
import _thread
import threading
import select

class Client_Manager:

	def __init__(self, socket):
		self.socket = socket
		self.connected = False
		self.exit = False

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
			if exit:
				print('Disconnecting from server')
				return
			data = self.socket.recv(1024)
			if not data:
				print('Disconnected')
				return
			print('New Data ', data)
			request = Client_Request(data.decode('ascii'), self)
			response = request.handle()
			if response == '':
				continue
			elif response == None:
				continue
			if response == 'CLIENT_CLOSE':
				continue
			self.socket.send(response.encode('ascii'))
		self.socket.close()

	def listen_for_user_input(self):
		print('Waiting input')
		while True:
			request = Client_Request('NEW_ACTION;', self)
			response = request.handle()
			if response == 'DISCONNECT;':
				exit = True
				break
			self.socket.send(response.encode('ascii'))
