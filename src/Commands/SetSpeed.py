from RobotMap import RobotMap
from TimedCommand import TimedCommand
from Maestro import Controller

class SetSpeed(TimedCommand):
	def __init__(self, channel, timeout, speed):
                self.channel = channel
                self.controller = Controller()
                self.speed = speed
                self.controller.setTarget(1, 6000)
                self.controller.setTarget(2, 6000)
                print("Constructing a SetSpeed command")
		super(SetSpeed, self).__init__(timeout)
                
	def _initialization(self):
                print("Initializing SetSpeed")
                print(str(self.controller))
                self.controller.setTarget(3, 7000)
                self.controller.setTarget(self.channel, self.speed)
		super(SetSpeed, self)._initialization()
                
        def _end(self):
                print("Channel is: " + str(self.channel))
		self.controller.setTarget(self.channel, 6000)
