from RobotMap import RobotMap
from TimedCommand import TimedCommand
from Maestro import Controller

class SetSpeed(TimedCommand):
	def __init__(self, channel, timeout, speed, parallel = False):
                self.channel = channel
                self.controller = Controller()
                self.speed = speed
                self.controller.setTarget(1, 6000)
                self.controller.setTarget(2, 6000)
                super(SetSpeed, self).__init__(timeout)
                self.parallel = parallel
                return
                
        def _execute(self):
                self.controller.setTarget(self.channel, self.speed)

        def _end(self):
		self.controller.setTarget(self.channel, 6000)
