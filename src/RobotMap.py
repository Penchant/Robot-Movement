from lib.Maestro.py import Controller

# Define port mappings and create all hardware references, such as Maestro here

class RobotMap

	controller = None
	drivetrainLeftChannel = -1
	drivetrainRightChannel = -2
	waistChannel = -3
	headHorizontalChannel = -4
	headVerticalChannel = -5

	@staticmethod
	def init():
		controller = Controller()

