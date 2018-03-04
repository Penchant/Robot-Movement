import threading

# OI (Operator Interface) is dedicated to matching interactions with the operator interface to actions
# such as if spacebar is pressed, disable the robot

from Subsystems.Waist import Waist
from Subsystems.Head import Head

import os
import Tkinter
from Tkinter import *
import time

from Subsystems.Drivetrain import Drivetrain
from RobotMap import RobotMap
from Subsystems.RoboGUI import GUI

class OI:
	def __init__(self, Robot):
		self.robot = Robot
		os.system('xset r off')
		self.tk = Tk()
		frame = Frame(self.tk)
		frame.bind("<KeyPress>", self.keydown)
		frame.bind("<KeyRelease>", self.keyup)
		frame.focus_set()
                #frame.pack()

                self.speed = Drivetrain.Slow
		self.gui = GUI(self.tk, self.robot.scheduler)
                
	def run(self):
		self.gui.main()
	def disable(self):
		print("Destroying tk")
		self.tk.destroy()
		os.system('xset r on')
	def keydown(self,event):
		print("Key pressed")	
		if(' ' == event.char):
                        print("Disabling")
                        RobotMap.controller.setTarget(2, 6000)
                        RobotMap.controller.setTarget(1, 6000)
                        self.robot.disable()
		elif('1' == event.char):
			if (self.robot.head.horizontalAngle + 200 > 7000):
				self.robot.head.horizontalAngle = 7000
			else:
				self.robot.head.horizontalAngle += 200
		elif('2' == event.char):
			if (self.robot.head.horizontalAngle - 200 < 3000):
				self.robot.head.horizontalAngle = 3000
			else:
				self.robot.head.horizontalAngle -= 200
		elif('3' == event.char):
			if (self.robot.head.verticalAngle + 200 > 7000):
				self.robot.head.verticalAngle = 7000
			else:
				self.robot.head.verticalAngle += 200
		elif('4' == event.char):
			if (self.robot.head.verticalAngle - 200 < 3000):
				self.robot.head.verticalAngle = 3000
			else:
				self.robot.head.verticalAngle -= 200
		elif('q' == event.char):
			self.robot.waist.angle = Waist.left
		elif('e' == event.char):
			self.robot.waist.angle = Waist.right
		elif('r' == event.char):
			self.robot.waist.angle = Waist.center
		elif('w' == event.char):
			self.robot.drivetrain.moveForward = True
			RobotMap.controller.setTarget(1, 6000 - self.speed)
		elif('s' == event.char):
                        RobotMap.controller.setTarget(1, 6000 + self.speed)
                        self.robot.drivetrain.moveBackward = True
		elif('a' == event.char):
                        RobotMap.controller.setTarget(2, 6000 + 200 + self.speed)
			self.robot.drivetrain.rotateLeft = True
		elif('d' == event.char):
                        RobotMap.controller.setTarget(2, 6000 - 200 - self.speed)
			self.robot.drivetrain.rotateRight = True
		elif('i' == event.char):
			self.speed = Drivetrain.Fast
		elif('k' == event.char):
			self.speed = Drivetrain.Medium
		elif('m' == event.char):
			self.speed = Drivetrain.Slow
                elif('\r' == event.char):
                        print("Sending stop signal to drivetrain")
                        RobotMap.controller.setTarget(1, 6000)
                        RobotMap.controller.setTarget(2, 6000)
                        self.robot.drivetrain.stop = not self.robot.drivetrain.stop
		else:
                        print(event.char)
			pass
			
	def keyup(self,event):
                if (event.char == 'w'):
                        RobotMap.controller.setTarget(1, 6000)
                        self.robot.drivetrain.moveForward = False
                elif (event.char == 's'):
                        RobotMap.controller.setTarget(1, 6000)
                        self.robot.drivetrain.moveBackward = False
                elif (event.char == 'a'):
                        RobotMap.controller.setTarget(2, 6000)
                        self.robot.drivetrain.rotateLeft = False
                elif (event.char == 'd'):
                        RobotMap.controller.setTarget(2, 6000)
                        self.robot.drivetrain.rotateRight = False
                pass

	def moveWheelsForward():
		print("WheelF Call")

	def moveWheelsBackwards():
		print("WheelB Call")
		
	def turnWheelsLeft():
		print("WheelL Call")

	def turnWheelsRight():
		print("WheelR Call")

	def stop():
		print("Stop Call")

	def setSlow():
		print("Slow Speed")

	def setMed():
		print("Med Speed")

	def setFast():
		print("Fast Speed")
