import threading
import time
from random import randint


# Head is the subsystem focused on the movement of the "head" of the robot, aka the LCD screen

class LifeEssence:

    def __init__(self, robot, health):
        self.robot = robot
        self.minDam = 2
        self.maxDam = 5
        self.HP = health
        self.enable = False

    def combat(self, enemy_minDam, enemy_maxDam, enemy_HP, has_key):
        self.enemy_minDam = enemy_minDam
        self.enemy_maxDam = enemy_maxDam
        self.enemy_HP = enemy_HP

        while ((self.enemy_HP > 0) and (self.HP > 0)):
            #Our robot attacks
            self.robot.network.send = "I am being attacked\n"
            time.sleep(3)
            self.attack = randint(enemy_minDam, enemy_maxDam)
            self.HP = self.HP - self.attack
            self.robot.network.send = "The enemy did " + str(self.attack) + " damage, I have " + str(self.HP) + " health remaining.\n"
            time.sleep(6)

            self.robot.network.send = "I am being attacked\n"
            time.sleep(3)
            self.attack = randint(self.minDam, self.maxDam)
            self.enemy_HP = self.enemy_HP - self.attack
            self.robot.network.send = "I did " + str(self.attack) + " damage, the enemy has " + str(self.enemy_HP) + " health remaining.\n"
            time.sleep(6)

        print("Attacking is over")
        if (self.HP >0 and has_key == True):
            self.robot.network.send = "I defeated the enemy and took his key\n"
            time.sleep(4)
            self.robot.navigation.location.hasEnemy = False
            self.robot.navigation.location.hasKey = False
            self.robot.key_obtained = True
        elif(self.HP > 0 and has_key == False):
            self.robot.network.send =  "I defeated the enemy but he had no key\n"
            self.robot.navigation.location.hasEnemy = False
            time.sleep(4)
            pass
        else:
            self.robot.network.send= "The enemy defeated me. Game Over\n"
            time.sleep(4)
            self.robot.disable()
            pass

    def loop(self):
        while (self.enable):
            self._execute()
            time.sleep(.02)

    def run(self):
        self.enable = True
        self.thread = threading.Thread(None, self.combat)
        self.thread.start()

    def disable(self):
        self.enable = False

