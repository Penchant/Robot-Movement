import threading
import time
# Waist is the subsystem focused on the control of the
# mid section of the robot that rotates horizontally

class Waist:

	FarLeft = 4500
	left = 5000
	MidLeft = 5000
	center = 6000
	Middle = 6000
	MidRight = 7500
	FarRight = 8300
	right = 7500

	def __init__(self, channel, controller):
		self.channel = channel
		self.controller = controller
		self.angle = Waist.center
		self.enable = False

	def _execute(self, angle = None):
		if angle is not None:
			self.angle = angle
		self.controller.setTarget(self.channel, self.angle)
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
		self.controller.setSpeed(self.channel, 0)

	def _angleToPWM(self, angle):
		while(angle > 180):
			angle -= 360
		while(angle < -180):
			angle += 360

		if (angle > maxLeft):
			angle = maxLeft
		elif (angle < maxRight):
			angle = maxRight
		
