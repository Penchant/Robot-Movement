
from Command import Command

class TestCommand(Command):
	count = 0
	def __init__(self, timeout=0):
		super(TestCommand, self).__init__(timeout)
                self.count = TestCommand.count
                TestCommand.count +=1
	def _initialization(self):
		print("TestCommand" + str(self.count))
		print("Timeout is" + str(self.time))
	def _isFinished(self):
		return True
