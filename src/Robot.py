
import threading
import time

import os, sys
sys.path.insert(0, os.getcwd())

from RobotMap import RobotMap
from OI import OI
from Subsystems.Drivetrain import Drivetrain
from Subsystems.Head import Head 
from Subsystems.Waist import Waist
from Subsystems.Network import Network
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

		#host = raw_input('Enter the hostname:')
		#host = '192.168.42.129'
		host = '100.66.20.27'
                #host = '10.152.130.25'
                #host = '10.152.227.236'
		#host = '100.82.220.120'
		#port = int(raw_input('Enter the port number: '))
		port = 6000		

		self.network = Network(host, port, self)
		self.oi = OI(self)

		self.subsystems.append(self.drivetrain)
		self.subsystems.append(self.head)
		self.subsystems.append(self.waist)
		self.subsystems.append(self.network)

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
		self.network.run()
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



