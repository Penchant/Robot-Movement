import time
from Command import Command

# Command thats finishes execution based on a given timeout
class TimedCommand(Command):
	def __init__(self, timeout):
                self.startTime = -1
		self.time = timeout
                self.parallel = False
        def _initialization(self):
                self.startTime = int(round(time.time() * 1000))
        def _isFinished(self):
                if self.startTime == -1:
                        self.startTime = int(round(time.time()*1000))
                return int(round(time.time() * 1000)) > self.startTime + self.time
