import socket
import threading


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

#host = raw_input('Enter the hostname:')
host = '192.168.42.129'
#host = '10.152.227.236'
#host = '100.82.220.120'
#port = int(raw_input('Enter the port number: '))
port = 6000

network = Network(host, port)

network.run()
input = ""
while input != "quit":
    input = raw_input('Enter text to send')
    network.send = input + '\n'

print('Closing')
network.socket.close()
network.enable = False



