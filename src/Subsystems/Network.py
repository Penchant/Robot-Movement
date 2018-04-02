
class Network:
	def __init__(self, hostname, port):
		self.socket = socket.socket()
		self.hostname = hostname
		self.port = port
		self.socket.connect((host, port))
		self.send = ""
		self.enable = False

	def loop_send(self):
		while(self.enable == True):
			if(self.send != ""):
				self.socket.send(self.send)
				self.send = ""
	def loop_recv(self):
		while(self.enable == True):
			buf = self.socket.recv(1024)
			print buf
			pass

	def run(self):
		self.enable = True
		send = threading.Thread(None, self.loop_send)
		recv = threading.Thread(None, self.loop_recv)
		send.start()
		recv.start()
	def disable(self):
		self.enable = False
		self.socket.shutdown(0)
		self.socket.close()