from Queue import *
from TimedCommand import TimedCommand
import threading
from collections import deque
from SetSpeed import SetSpeed
from SetPosition import SetPosition


class Scheduler:
    def __init__(self):
        self.current_command = None
        self.schedule = Queue()
        self.enable = False
        self.guiQueue = []
        pass

    def addSequentialCommand(self, command):
        if not isinstance(command, TimedCommand):
            self.schedule.put(command)
            self.schedule.put(TimedCommand(command.time))
        else:
            self.schedule.put(command)

    def addParallelCommand(self, command):
        self.schedule.put(command)

    def execute(self):
        if (
                self.current_command == None or self.current_command._isFinished() or self.current_command.parallel == True):
            try:
                self.current_command = self.schedule.get(True, None)
                print("Executing command " + str(self.commandNum))
                self.current_command_thread = threading.Thread(None, self.current_command.run)
                self.current_command_thread.start()
            except Empty:
            	self.enable = False
            self.commandNum +=1

    def loop(self):
    	self.running = True
        self.commandNum = 0
        while (self.enable):
            self.execute()
        complete = self.current_command._isFinished()
       	self.running = False
        if ((self.current_command != None) and (complete == False)):
            self.current_command.enable = False

    def createCommands(self):
        self.schedule = Queue()
        queue = deque(self.guiQueue)
        print("Creating commands")
        while (len(queue) != 0):
            guiCommand = queue.popleft()
            print("Creating command " + str(guiCommand.index))

            if ((guiCommand.channel == 1) or (guiCommand.channel == 2)):
                command = SetSpeed(guiCommand.channel, guiCommand.timeout, guiCommand.target, guiCommand.parallel)
                self.addSequentialCommand(command)
            else:
                command = SetPosition(guiCommand.channel, guiCommand.target, guiCommand.timeout, guiCommand.parallel)
                if guiCommand.parallel:
                    self.addParallelCommand(command)
                else:
                    self.addSequentialCommand(command)

    def run(self):
        self.enable = True
        self.createCommands()
        self.thread = threading.Thread(None, self.loop)
        self.thread.start()

    def disable(self):
        self.enable = False
