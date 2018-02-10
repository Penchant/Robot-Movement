from src.RobotMap import RobotMap
from src.Subsystems.Drivetrain import Drivetrain
from src.Subsystems.Head import Head 
from src.Subsystem.Waist import Waist

# Robot is the main file that instantiantes all subsystems of the robot 
# and controls the functioning of overall

class Robot
	def __init__(self)
		RobotMap.init()
		
		self.subsystems = []

		self.drivetrain = Drivetrain(
			RobotMap.drivetrainLeftChannel, RobotMap.drivetrainRightChannel, RobotMap.Controller)
		self.head = Head(
			RobotMap.headHorizontalChannel, RobotMap.headVerticalChannel, RobotMap.Controller)
		self.waist = Waist(RobotMap.waistChannel, RobotMap.Controller)
		
		self.subsystems.append(self.drivetrain)
		self.subsystems.append(self.head)
		self.subsystems.append(self.waist)

		self.robotInit = true

	def Teleop(self)
		self.teleop = True
		
		self.drivetrain.enable = True
		self.head.enable = True

		while(self.teleop):
			pass
		
		self.teleop = false
		# Disable subsytems when teleop is disabled
		self.drivetrain.enable = False
		self.head.enable = False

	def disable(self):
		self.teleop = false

		# Look at killing teleop thread here

		# Disable each subsystem
		for subsystem in subsystems:
			if(subsystem.enable is True):
				subsystem.enable = False


def main():
	robot = Robot()

	# Create thread eventually that can then be killed 
	robot.Teleop()

if __name__ == "__main__" :
	main()



