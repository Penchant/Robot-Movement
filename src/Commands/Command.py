import os, sys

sys.path.insert(0, os.getcwd())

class Command(object):
	def __init__(self, time=0):
		self.time = time
		self.enable = False
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
                self.enable = True
		self._initialization()
		while(not self._isFinished() and self.enable == True):
                        self._execute()
		self._end()
