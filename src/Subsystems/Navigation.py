import time
import threading
from collections import namedtuple

class Navigation():

    def __init__(self, robot):
        self.robot = robot
        self.enable = False

        Node = namedtuple('Node', ['options', 'hasRestore', 'hasGold',
            'hasKey', 'hasEnemy', 'enemyHealth', 'enemyMinDamage', 'enemyMaxDamage'])
        intersection1 = Node ({}, False, False, False, False, 0, 0, 0)
        intersection2 = Node ({}, False, True, False, False, 0, 0, 0)
        intersection3 = Node ({}, False, False, False, True, 5, 1, 3)
        intersection4 = Node ({}, False, False, True, True, 8, 2, 4)
        intersection5 = Node ({}, True, False, False, False, 0, 0, 0)

        intersection1.options['south'] = intersection3
        intersection2.options['east'] = intersection3
        intersection3.options['north'] = intersection1
        intersection3.options['east'] = intersection4
        intersection3.options['west'] = intersection2
        intersection3.options['south'] = intersection5
        intersection4.options['west'] = intersection3
        intersection5.options['north'] = intersection3

        self.location = intersection1

        pass

    def _loop(self):
        while(self.enable):
            if(self.location.hasRestore == True):
                message = "I have found a recharging station, hit points back to 10\n"
                self.robot.network.send = message
                self.robot.lifeEssence.HP = 10

            if(self.location.hasGold == True and self.robot.key_obtained == True):
                message = "I have found a box and my key opens it\n"
                self.robot.network.send = message
                self.time.sleep(.1)
                self.robot.disable()

            if(self.location.hasGold == True and self.robot.key_obtained == False):
                message = "I have found a box but the box is locked. Maybe we can find a key elsewhere.\n"
                self.robot.network.send = message

            if(self.location.hasEnemy == True):
                self.robot.lifeEssence.combat(self.location.enemyMinDamage, self.location.enemyMaxDamage, self.enemyMaxDamage, self.location.hasKey)

            message = "I see a path to the" + self.optionsToString() + "which way do you want to go\n?"
            self.robot.network.send =  message
            while(self.robot.network.receive == ""):
                time.sleep(.1)
                pass


    def optionsToString(self):
        s_options = ""
        for key in self.location.options.keys():
            s_options = " " + key + ", "
        return s_options

    def run(self):
        self.enable = True
        self._loop()
        pass
    def disable(self):
        self.enable = False
