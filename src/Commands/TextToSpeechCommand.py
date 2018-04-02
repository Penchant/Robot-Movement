
from TimedCommand import TimedCommand

class TextToSpeechCommand(TimedCommand):
	def __init__(self, text, robot):
		super(TextToSpeechCommand, self).__init__(2)
		self.text = text
		self.parallel = False
		self.robot = robot

	def _initialization(self):
		self.robot.network.send = self.text + '\n'