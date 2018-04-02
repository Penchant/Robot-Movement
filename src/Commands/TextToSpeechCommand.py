
from Command import Command

class TextToSpeechCommand(Command):
	def __init__(self, text, robot):
		super(TextToSpeechCommand, self).__init__(2)
		self.text = text
		self.parallel = False
		self.robot = robot

	def _initialization(self):
		self.robot.network.send = self.text + '\n'

	def _isFinished(self):
		return "continue" in self.robot.network.receive.lower() 