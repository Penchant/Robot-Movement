
import Command

class TestCommand(Command):
	count = 0
	def __init__(self, timeout=0):
		super(Command, self).__init__(self, timeout)
		count +=1
	def _initialization(self):
		print("TestCommand" + str(count))
		print("Timeout is" + str(self.time))
	def _isFinished(self):
		return true