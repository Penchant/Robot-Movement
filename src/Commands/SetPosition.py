
import Command

class SetPosition(Command):
	def __init__(self, channel, position, timeout=0):
		super(Command, self).__init__(self, timeout)
		self.channel = channel
		self.position = position
	def _initialization(self):
		RobotMap.controller.setTarget(self.channel, self.position)

	def _isFinished(self):
		return true