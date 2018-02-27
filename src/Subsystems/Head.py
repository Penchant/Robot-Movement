import threading
import time

# Head is the subsystem focused on the movement of the "head" of the robot, aka the LCD screen

class Head:

	maxVerticalUp = 60
	minVerticalDown = -60
	maxHorizontal = 60
	minHorizontal = -60


	verticalUp = 7000
	verticalMid = 5600
	verticalDown = 3000

	horizontalLeft = 7000
	horizontalMid = 5600
	horizontalRight = 3000

	def __init__(self, horizontalChannel, verticalChannel, controller):
		self.horizontalChannel = horizontalChannel
		self.verticalChannel = verticalChannel
		self.controller = controller
		self.horizontalAngle = Head.horizontalMid
		self.verticalAngle = Head.verticalMid
		self.enable = False

	def _execute(self, horizontalAngle = None, verticalAngle = None):
		if horizontalAngle is not None:
			self.horizontalAngle = horizontalAngle
		if verticalAngle is not None:
			self.verticalAngle = verticalAngle
		self.controller.setTarget(self.horizontalChannel, self.horizontalAngle)
		self.controller.setTarget(self.verticalChannel, self.verticalAngle)

	def loop(self):
		while(self.enable):
			self._execute()
			time.sleep(.02)
    def run(self):
                self.enable = True
                self.thread = threading.Thread(None, self.loop)
                self.thread.start()
	def disable(self):
		self.enable = False

		self.controller.setSpeed(self.horizontalChannel, 0)
		self.controller.setSpeed(self.verticalChannel, 0)

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
