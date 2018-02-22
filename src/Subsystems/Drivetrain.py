import threading
import time
#from src.RobotMap import RobotMap
from Maestro import Controller
# Drivetrain is the subsystem focused on movement on the drivetrain
class Drivetrain:
        Fast = 1500
        Medium = 950
        Slow = 650

        def __init__(self, rotateChannel, forwardChannel, controller):
		self._rotateChannel = rotateChannel
		self._forwardChannel = forwardChannel
		self.controller = controller
                self.controller = Controller()
		self.rotate = 0
		self.forward = 0
		self.enable = False
                self.moveForward = False
                self.moveBackward = False
                self.rotateLeft = False
                self.rotateRight = False
                self.speed = Drivetrain.Slow
                self.stop = False
	def loop(self):
		while(self.enable):
			self.execute()
                        time.sleep(.02)
	def execute(self, rotation = None, forward = None):
		if rotation is not None:
			self.rotate = rotation
		if forward is not None:
			self.forward = forward
                tempForward = 6000
                tempRotate = 6000
                if self.moveForward:
                        tempForward += self.speed
                        print(str(tempForward))
                if self.moveBackward:
                        tempForward -= self.speed
                if self.rotateLeft:
                        tempRotate += self.speed
                if self.rotateRight:
                        tempRotate -= self.speed

                if self.stop:
                        print("Stopping drivetrain")
                        tempForward = 6000
                        tempRotate = 6000

                self.forward = tempForward
                self.rotate = tempRotate
                        
		self.controller.setSpeed(self._rotateChannel, self.rotate)
		self.controller.setSpeed(self._forwardChannel, self.forward)
	def run(self):
                self.enable = True
                # Create new thread here
		self.thread = threading.Thread(None, self.loop)
		self.thread.start()
                print("Drivetrain running")
		
	def disable(self):
		self.enable = False

		# When disabled, set movement values to 0 and update	
		self.controller.setSpeed(self._rotateChannel, 0)
		self.controller.setSpeed(self._forwardChannel, 0)
