import socket
import threading
from SetSpeed import SetSpeed

class Network:
	def __init__(self, hostname, port, robot):
		self.socket = socket.socket()
		self.hostname = hostname
		self.port = port
		self.socket.connect((hostname, port))
		self.send = ""
		self.enable = False
		self.receive = ""
		self.robot = robot

	def loop_send(self):
		while(self.enable == True):
			if(self.send != ""):
				self.socket.send(self.send)
				self.send = ""
	def loop_recv(self):
		while(self.enable == True):
			buf = self.socket.recv(1024)
			print buf
			self.check_recv(buf)
			print ("After check: " + buf) 
			if(buf != ""):
				self.receive = buf
			if(buf.lower() == "start"):
				#self.robot.oi.gui.go_button_clicked()
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

	def check_recv(self, buffer):
		forwardChannel = 1
		rotateChannel = 2
		forwardTime = 2
		forward = 7000
		backward = 5000
		left = 7000
		right = 5000
		rotate90Time = 1
		rotate180Time = 2

		valid_direction = False
		for key in self.robot.navigation.location.options.keys():
			if key in buffer.lower():
				valid_direction = True


		if valid_direction == True:

			if("north" in buffer.lower()):
				self.robot.navigation.location = self.robot.navigation.location.options["north"]
				print self.robot.navigation.location.options

				if(self.robot.direction == "north"):
					self.robot.scheduler.addParallelCommand(SetSpeed(forwardChannel, forwardTime, forward))
				elif(self.robot.direction == "west"):
					#Turn left then forward
					self.robot.scheduler.addParallelCommand(SetSpeed(rotateChannel, rotate90Time, left))
					self.robot.scheduler.addParallelCommmand(SetSpeed(forwardChannel, forwardTime, forward))
				elif(self.robot.direction == "east"):
					#Turn right then forward
					self.robot.scheduler.addParallelCommand(SetSpeed(rotateChannel, rotate90Time, right))
					self.robot.scheduler.addParallelCommmand(SetSpeed(forwardChannel, forwardTime, forward))
				elif(self.robot.direction == "south"):
					#Turn 180 then forward
					self.robot.scheduler.addParallelCommand(SetSpeed(rotateChannel, rotate180Time, right))
					self.robot.scheduler.addParallelCommand(SetSpeed(forwardChannel, forwardTime, forward))
				self.direction = "north"

			elif("south" in buffer.lower()):
				self.robot.navigation.location = self.robot.navigation.location.options["south"]
				print self.robot.navigation.location.options

				if(self.robot.direction == "north"):

					#Turn 180 then forward
					self.robot.scheduler.addParallelCommand(SetSpeed(rotateChannel, rotate180Time, right))
					self.robot.scheduler.addParallelCommand(SetSpeed(forwardChannel, forwardTime, forward))

				elif(self.robot.direction == "west"):
					#Turn right then forward
					self.robot.scheduler.addParallelCommand(SetSpeed(rotateChannel, rotate90Time, right))
					self.robot.scheduler.addParallelCommmand(SetSpeed(forwardChannel, forwardTime, forward))
				elif(self.robot.direction == "east"):
					#Turn left then forward
					self.robot.scheduler.addParallelCommand(SetSpeed(rotateChannel, rotate90Time, left))
					self.robot.scheduler.addParallelCommmand(SetSpeed(forwardChannel, forwardTime, forward))
				elif(self.robot.direction == "south"):

					self.robot.scheduler.addParallelCommand(SetSpeed(forwardChannel, forwardTime, forward))
				self.direction = "south"
			elif("west" in buffer.lower()):
				self.robot.navigation.location = self.robot.navigation.location.options["west"]
				print self.robot.navigation.location.options

				if(self.robot.direction == "north"):

					#Turn right then forward
					self.robot.scheduler.addParallelCommand(SetSpeed(rotateChannel, rotate90Time, right))
					self.robot.scheduler.addParallelCommand(SetSpeed(forwardChannel, forwardTime, forward))

				elif(self.robot.direction == "west"):
					self.robot.scheduler.addParallelCommand(SetSpeed(forwardChannel, forwardTime, forward))

				elif(self.robot.direction == "east"):

					#Turn 180 then forward
					self.robot.scheduler.addParallelCommand(SetSpeed(rotateChannel, rotate180Time, right))
					self.robot.scheduler.addParallelCommand(SetSpeed(forwardChannel, forwardTime, forward))
				elif(self.robot.direction == "south"):

					#Turn left then forward
					self.robot.scheduler.addParallelCommand(SetSpeed(rotateChannel, rotate90Time, left))
					self.robot.scheduler.addParallelCommand(SetSpeed(forwardChannel, forwardTime, forward))

				self.direction = "west"

			elif("east" in buffer.lower()):
				self.robot.navigation.location = self.robot.navigation.location.options["east"]
				print self.robot.navigation.location.options

				if(self.robot.direction == "north"):

					#Turn left then forward
					self.robot.scheduler.addParallelCommand(SetSpeed(rotateChannel, rotate90Time, left))
					self.robot.scheduler.addParallelCommand(SetSpeed(forwardChannel, forwardTime, forward))

				elif(self.robot.direction == "west"):
					#Turn 180 then forward
					self.robot.scheduler.addParallelCommand(SetSpeed(rotateChannel, rotate180Time, right))
					self.robot.scheduler.addParallelCommand(SetSpeed(forwardChannel, forwardTime, forward))

				elif(self.robot.direction == "east"):
					self.robot.scheduler.addParallelCommand(SetSpeed(forwardChannel, forwardTime, forward))
				elif(self.robot.direction == "south"):

					#Turn right then forward
					self.robot.scheduler.addParallelCommand(SetSpeed(rotateChannel, rotate90Time, right))
					self.robot.scheduler.addParallelCommand(SetSpeed(forwardChannel, forwardTime, forward))
				self.direction = "east"
		else:
			self.send = "That is not a valid direction from here. " + "I see a path to the" + self.robot.navigation.optionsToString() + "which way do you want go?\n"
                        buf = ""
			pass
