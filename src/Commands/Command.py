

class Command:
	def __init__(self, time=0):
		self.time = time
		self.enable = True
		pass
	# Initialization for the running of the command 
	def _initialization(self):
		pass
	# Execution of the command which repeats until isFinished
	# returns true or the command is interrupted
	def _execute(self):
		pass
	# Returns when the command should finish 
	def _isFinished(self):
		pass
	# Called once after isFinished returns true
	def _end(self):
		pass
	# Called when stop is pressed
	def _interrupted(self):
		pass
	# Runs the command
	def run(self):
		self._initialization()
		while(!self._isFinished() and self.enable):
			if(stop):
				self._interrupted()
				break
			self._execute()
		self.end()