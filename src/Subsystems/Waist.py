# Waist is the subsystem focused on the control of the
# mid section of the robot that rotates horizontally

class Waist:

	maxLeft = 45
	maxRight = -45

	def __init__(self, channel, controller):
		self.channel = channel
		self.controller = controller
		self.angle = 0
		self.enable = False

	def _execute(self, angle = None):
		if angle is not None:
			self.angle = angle
		self.controller.setTarget(self.channel, self.angle)
	def run(self):

		# Create thread here
		while(enable):
			self._execute()

	def _angleToPWM(self, angle):
		while(angle > 180):
			angle -= 360
		while(angle < -180):
			angle += 360

		if (angle > maxLeft):
			angle = maxLeft
		elif (angle < maxRight):
			angle = maxRight
		