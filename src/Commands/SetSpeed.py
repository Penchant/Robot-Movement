from src import RobotMap

class SetSpeed(TimedCommand):
	def __init__(self, channel, timeout, speed):
		super(TimedCommand, self).__init__(self, timeout)
		self.channel = -1
	def _initialize(self):
		super(TimedCommand, self)._initialize(self)
		RobotMap.controller.setTarget(self.channel, self.speed)
	def _end(self):
		RobotMap.controller.setTarget(self.channel, 6000)
