import Queue
import TimedCommand
import threading

class Scheduler:
	def __init__(self):
		self.current_command = None
		self.schedule = Queue()
		self.enable = False
		pass
	def addSequentialCommand(self, command):
		if not isinstance(command, TimedCommand):
			self.schedule.put(command)
			self.schedule.put(TimedCommand(command.time))
		else:
			self.schedule.put(command)
	def addParallelCommand(self, command):
		self.schedule.put(command)
	def execute(self):
		if (self.current_command == None or self.current_command.isFinished()):
				try:
					self.current_command = self.schedule.get(True, None)
					self.current_command_thread = threading.thread(None, self.current_command.run)
					self.current_command_thread.start()
				except Empty:
					pass
	def loop(self):
		while(self.enable):
			self.execute()
		if (not self.current_command == None) and (not self.current_command.isFinished)
			self.current_command.enable = False
	def run(self):
		self.enable = True
		self.thread = threading.Thread(None, self.loop)
		self.thread.start()
		
		
