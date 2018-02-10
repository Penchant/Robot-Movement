# Head is the subsystem focused on the movement of the "head" of the robot, aka the LCD screen

class Head

	maxVerticalUp = 120
	minVerticalDown = -120
	maxHorizontal = 120
	minHorizontal = -120


	verticalUp = 60
	verticalMid = 0
	verticalDown = -60

	horizontalLeft = 60
	horizontalMid = 0
	horizontalRight = -60

	def __init__(self, horizontalChannel, verticalChannel, controller):
		self.horizontalChannel = horizontalChannel
		self.verticalChannel = verticalChannel
		self.controller = controller
		self.horizontalAngle = 0
		self.verticalAngle = 0
		self.enable = False

	def _execute(self, horizontalAngle = None, verticalAngle = None):
		if horizontalAngle is not None:
			self.horizontalAngle = horizontalAngle
		if verticalAngle is not None:
			self.verticalAngle = verticalAngle
		self.controller.setTarget(self.horizontalChannel, self.angleToPWM(self.horizontalAngle, False))
		self.controller.setTarget(self.verticalChannel, self.angleToPWM(self.verticalAngle, True))

	def run(self):

		# Create thread here
		while(enable):
			self._execute()

	def _angleToPWM(self, angle, isVertical):
		while(angle > 180):
			angle -= 360
		while(angle < -180):
			angle += 360

		if (isVertical):
			if (angle > maxVerticalUp):
				angle = maxVerticalUp
			elif (angle < minVerticalDown):
				angle = minVerticalDown
		else:
			if (angle > maxHorizontal):
				angle = maxHorizontal
			elif (angle < minHorizontal):
				angle = minHorizontal
