from Maestro import Controller

# Define port mappings and create all hardware references, such as Maestro here

class RobotMap:

	controller = None
	drivetrainRotateChannel = 2
	drivetrainForwardChannel = 1
	waistChannel = 0
	headHorizontalChannel = 3
	headVerticalChannel = 4

	@staticmethod
	def init():
		RobotMap.controller = Controller()

