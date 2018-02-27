from RobotMap import RobotMap
from TimedCommand import TimedCommand

class SetSpeed(TimedCommand):
	def __init__(self, channel, timeout, speed):
		super(SetSpeed, self).__init__(timeout)
		self.channel = -1
	def _initialize(self):
		super(TimedCommand, self)._initialize(self)
		RobotMap.controller.setTarget(self.channel, self.speed)
	def _end(self):
		RobotMap.controller.setTarget(self.channel, 6000)
