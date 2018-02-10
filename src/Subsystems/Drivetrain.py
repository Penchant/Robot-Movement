
# Drivetrain is the subsystem focused on movement on the drivetrain
class Drivetrain
	def __init__(self, leftChannel, rightChannel, controller):
		self._leftChannel = leftChannel
		self._rightChannel = rightChannel
		self.controller = controller
		self.rotate = 0
		self.forward = 0
		self.enable = False

	def execute(self, rotation = None, forward = None):
		if rotation is not None:
			self.rotate = rotation
		if forward is not None:
			self.forward = forward
		self._left = .5 * self.rotate + .5 * self.forward
		self._right = .5 * self.rotate - .5 * self.forward 
		self.controller.setSpeed(self._leftChannel, self._left)
		self.controller.setSpeed(self._rightChannel, self._right)

	def run():
		# Create new thread here
		while(enable):
			self.execute()

		# When disabled, set movement values to 0 and update	
		self.execute(0,0)

	# Likely can be removed
	def drive(self, rotation = None, forward = None):
		if rotation is not None:
			self.rotate = rotation
		if forward is not None:
			self.forward = forward  