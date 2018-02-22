
import threading
import time

from RobotMap import RobotMap
from OI import OI
from Subsystems.Drivetrain import Drivetrain
from Subsystems.Head import Head 
from Subsystems.Waist import Waist


# Robot is the main file that instantiantes all subsystems of the robot 
# and controls the functioning of overall

class Robot:
	def __init__(self):
		RobotMap.init()

                for channel in (0,1,2,3,4):
                        print("Initializing " + str(channel))
                        RobotMap.controller.setTarget(channel, 5000)
                        time.sleep(.1)
                        RobotMap.controller.setTarget(channel, 7000)
                        time.sleep(.1)
                        RobotMap.controller.setTarget(channel, 6000)
                        time.sleep(.1)
                
		self.subsystems = []

		self.drivetrain = Drivetrain(
			RobotMap.drivetrainRotateChannel, RobotMap.drivetrainForwardChannel, RobotMap.controller)
		self.head = Head(
			RobotMap.headHorizontalChannel, RobotMap.headVerticalChannel, RobotMap.controller)
		self.waist = Waist(RobotMap.waistChannel, RobotMap.controller)
		
		self.oi = OI(self)

		self.subsystems.append(self.drivetrain)
		self.subsystems.append(self.head)
		self.subsystems.append(self.waist)

		self.robotInit = True

	def Teleop(self):
		self.teleop = True

                self.drivetrain.run()
                self.head.run()
                self.waist.run()
                self.oi.run()

                #for subsystem in self.subsystems:
		#		subsystem.run()
		self.drivetrain.thread.join()
		self.head.thread.join()
		self.waist.thread.join()
		
		self.teleop = False

	def disable(self):
		self.teleop = False

		# Look at killing teleop thread here

		# Disable each subsystem
		for subsystem in self.subsystems:
			if(subsystem.enable is True):
				subsystem.disable()
		self.oi.disable()


def main():
	robot = Robot()

	# Create thread eventually that can then be killed 
	robot.Teleop()

if __name__ == "__main__" :
	main()



