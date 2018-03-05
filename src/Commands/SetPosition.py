from RobotMap import RobotMap
import Command

class SetPosition(Command.Command):
	def __init__(self, channel, position, timeout=0, parallel = False):
		super(SetPosition, self).__init__(timeout)
		self.channel = channel
		self.position = position
		self.parallel = parallel
		self.isFinished = False
	def _initialization(self):
		RobotMap.controller.setTarget(self.channel, self.position)
		self.isFinished = True

	def _isFinished(self):
		return self.isFinished
