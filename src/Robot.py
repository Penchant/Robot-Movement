
import threading
import time

import os, sys
sys.path.insert(0, os.getcwd())

from RobotMap import RobotMap
from OI import OI
from Subsystems.Drivetrain import Drivetrain
from Subsystems.Head import Head 
from Subsystems.Waist import Waist
from Commands.Scheduler import Scheduler
from Commands.TestCommand import TestCommand
from Commands.SetSpeed import SetSpeed
from Commands.SetPosition import SetPosition

# Robot is the main file that instantiantes all subsystems of the robot 
# and controls the functioning of overall

class Robot:
	def __init__(self):
		RobotMap.init()
		self.scheduler = Scheduler()
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

                #self.drivetrain.run()
                #self.head.run()
               # self.waist.run()

		#self.scheduler.addSequentialCommand(SetSpeed(1,3000, 8000))
		#self.scheduler.addSequentialCommand(SetSpeed(2, 1000, 8000))
		#self.scheduler.addSequentialCommand(TestCommand(7000))
		#self.scheduler.addSequentialCommand(TestCommand(5000))
		#self.scheduler.addSequentialCommand(SetSpeed(1,1000, 6000))
		#self.scheduler.addSequentialCommand(SetSpeed(2, 1000, 6000))
		self.scheduler.run()
		self.oi.run()
                
		#self.drivetrain.thread.join()
		#self.head.thread.join()
		#self.waist.thread.join()
		
		self.teleop = False

	def disable(self):
		self.teleop = False

		self.scheduler.disable()
		#self.scheduler.join()

		# Disable each subsystem
		for subsystem in self.subsystems:
			if(subsystem.enable is True):
				subsystem.disable()
		self.oi.disable()
		print("All systems disabled")

def main():
	robot = Robot()

	# Create thread eventually that can then be killed 
	robot.Teleop()
        #robot.oi.disable()
        print("Program is done")
        
if __name__ == "__main__" :
	main()



