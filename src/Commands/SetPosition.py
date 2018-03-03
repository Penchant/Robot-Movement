from RobotMap import RobotMap
import Command

class SetPosition(Command.Command):
	def __init__(self, channel, position, timeout=0):
		super(SetPosition, self).__init__(timeout)
		self.channel = channel
		self.position = position
	def _initialization(self):
		RobotMap.controller.setTarget(self.channel, self.position)

	def _isFinished(self):
		return True
