from tkinter import *
from collections import namedtuple
#from Scheduler import Scheduler
from Drivetrain import Drivetrain
from Waist import Waist
import threading 
class GUI:
    WIDTH = 800
    HEIGHT = 450
    POP_WIDTH = 500
    POP_HEIGHT = 300

    def __init__(self, tkinter_ref = None, scheduler = None):
        if tkinter_ref == None:
            tkinter_ref = Tk()
        self.speed = "slow"
        self.angle = 0
        self.head_pos = "middle"
        self.window = tkinter_ref
        self.fb = StringVar(self.window)
        self.scheduler = scheduler
        self.queuedCommands = []
        self.target = 0
        self.row_counter = 0

    def set_speed(self, speed):
        self.target = speed

    def add_command(self):

        self.duration = self.duration_spinbox.get()
        if self.channel == 1:
            self.target = self.target + 6000 if self.fb.get() == 'Forward' else 6000 - self.target
        elif self.channel == 2:
            self.target = self.target + 6000 if self.fb.get() == 'Left' else 6000 - self.target
        elif self.channel == 3:
            self.channel = 4 if self.fb.get() == 'Horizontal' else 3
            self.target = self.head_scale.get() * 3000 / self.head_scale['to'] + 6000

        SetPoint = namedtuple('SetPoint', ['channel', 'timeout', 'target', 'parallel', 'index'])
        temp = SetPoint(channel = self.channel, timeout = int(float(self.duration)*1000), target = self.target, parallel = self.parallel.get(), index = len(self.queuedCommands))
        self.queuedCommands.append(temp)
        self.add_to_queue(self)
        self.popup.destroy()

    def add_to_queue(self):
        check = ""
        if(self.parallel):
            check = "P"
        if self.channel == 0:
            text = "Rotate Waist " + self.pos_string + ", Duration = " + check
        elif self.channel == 1:
            text = "Move " + self.fb.get() + ", Duration = " + str(self.duration) + str(self.target) + check
        elif self.channel == 2:
            text = "Rotate " + self.fb.get() + ", Duration = " + str(self.duration) + str(self.target) + check
        elif self.channel == 3:
            text = "Rotate Head " + str(self.head_scale.get()) + ", Duration = " + check
        else:
            text = "Move Head " + str(self.head_scale.get()) + ", Duration = " + check
        queue_button = Button(self.queue_frame, bg="white", text= text, font = 'Helvetica 12')
        queue_button.grid(row = self.row_cntr, sticky = "nw")
        self.row_cntr +=1

    def cancel(self):
        self.popup.destroy()

    def set_angle(self, angle):
        self.target = angle

    def set_head_pos(self, pos, pos_string):
        self.target = pos
        self.pos_string = pos_string
    def initialize_popup(self, adjustment = 0):
        self.popup = Toplevel(self.window)
        self.popup.configure(background='White')

        # Make frames
        parallel_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        button_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=3, padx=3)

        # Configure Layout
        self.popup.grid_rowconfigure(1, weight=1)
        self.popup.grid_columnconfigure(0, weight=1)

        duration_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        duration_frame.grid(row=(1 + adjustment), column=0, sticky="w")
        # make spinbox
        self.duration_spinbox = Spinbox(duration_frame, bg='White', from_=0.1, to=10.0, width=20, format='%2.1f',
                                   increment='0.1', font='Helvetica 36', )
        duration_label = Label(duration_frame, bg="white", text="Enter duration in seconds:")
        duration_label.grid(row=(0 + adjustment), sticky='w')
        self.duration_spinbox.grid(row=(1 + adjustment), sticky='w')

        parallel_frame.grid(row=3, column=0, sticky="w")
        # make checkbutton
        self.parallel = BooleanVar()
        parallel_check = Checkbutton(parallel_frame, bg='White', variable = self.parallel)
        parallel_label = Label(parallel_frame, bg="White", text="Make this action run in parallel?")
        parallel_label.grid(row=0, sticky='w')
        parallel_check.grid(row=0, column=1, sticky='e')

        button_frame.grid(row=4, column=0, sticky="w")
        add_button = Button(button_frame, width=15, height=1, text="Add", bg="white", fg="Black",
                        command=self.add_command)
        cancel_button = Button(button_frame, width=15, height=1, text="Cancel", bg="white", fg="Black",
                        command=self.cancel)
        add_button.grid(row=0, column=3, sticky='w')
        cancel_button.grid(row=0, column=4, sticky='e')

    def speed_frame_init(self):
        self.set_speed(Drivetrain.Slow)
        speed_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        speed_frame.grid(row=0, column=0, sticky="w")
        # make buttons
        slow_button = Button(speed_frame, width=23, text="Slow", bg="white", fg="Black",
                             command=(lambda: self.set_speed(Drivetrain.Slow)))
        med_button = Button(speed_frame, width=23, text="Medium", bg="white", fg="Black",
                            command=(lambda: self.set_speed(Drivetrain.Medium)))
        fast_button = Button(speed_frame, width=23, text="Fast", bg="white", fg="Black",
                             command=(lambda: self.set_speed(Drivetrain.Fast)))
        # Make Labels
        speed_label = Label(speed_frame, bg="white", text="Choose speed:")
        # Add buttons and labels
        speed_label.grid(row=0, column=1, sticky='w')
        slow_button.grid(row=1, column=1, sticky="senw")
        med_button.grid(row=1, column=2, sticky="senw")
        fast_button.grid(row=1, column=3, sticky="senw")

    def option_init(self, option1, option2):
        self.fb.set(option1)
        option_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        option_frame.grid(row = 2, column = 0, sticky = "w")

        # Make option menu
        fb_option = OptionMenu(option_frame, self.fb, option1, option2)
        option_label = Label(option_frame, bg="white", text = "Choose direction:")
        option_label.grid(row = 0, column = 0, sticky = 'w')
        fb_option.grid(row = 0 , column =1, sticky = 'w')

    def f_button_clicked(self):
        self.initialize_popup()
        self.speed_frame_init()
        self.option_init("Forward", "Backward")
        self.channel = 1

    def l_button_clicked(self):
        self.initialize_popup()
        self.speed_frame_init()
        self.option_init("Right", "Left")
        self.channel = 2

    def h_button_clicked(self):
        self.initialize_popup()
        self.option_init("Vertical", "Horizontal")
        self.channel = 3
        # Make frames
        direction_ud_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=5,
                                   padx=3)
        #direction_lr_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=5,
        #                            padx=3)
        direction_ud_frame.grid(row=0, column=0, sticky="w")
        #direction_lr_frame.grid(row=1, column=0, sticky="w")

        # make buttons
        self.head_scale = Scale(direction_ud_frame, bg='White', bd=4, from_=-10, to=10, resolution=1, orient=HORIZONTAL,
                        sliderlength=30, length=400, width=30)
        #self.lr_scale = Scale(direction_lr_frame, bg='White', bd=4, from_=-10, to=10, resolution=1, orient=HORIZONTAL,
        #                  sliderlength=30, length=400, width=30)
        # Make Labels
        ud_label = Label(direction_ud_frame, bg="white", text="Adjust slider to look up/down or left/right:")
        #lr_label = Label(direction_lr_frame, bg='White', text="Adjust slider to look left or right:")

        #Add buttons and labels
        ud_label.grid(row=1, column=1, sticky='w')
        self.head_scale.grid(row=1, column=2, sticky='e')
        #lr_label.grid(row=1, column=1, sticky="w")
        #lr_scale.grid(row=1, column=2, sticky="e")

    def w_button_clicked(self):
        self.initialize_popup()
        self.channel = 0
        self.set_head_pos(Waist.Middle)
        # Make frames
        direction_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=5, padx=3)
        direction_frame.grid(row=0, column=0, sticky="w")

        # make buttons
        fl_button = Button(direction_frame, width=15, text="Far Left", bg="white", fg="Black",
                           command=(lambda: self.set_head_pos(Waist.FarLeft, "Far Left")))
        ml_button = Button(direction_frame, width=15, text="Middle Left", bg="white", fg="Black",
                           command=(lambda: self.set_head_pos(Waist.MidLeft, "Middle Left")))
        m_button = Button(direction_frame, width=15, text="Middle", bg="white", fg="Black",
                          command=(lambda: self.set_head_pos(Waist.Middle, "Middle")))
        mr_button = Button(direction_frame, width=15, text="Middle Right", bg="white", fg="Black",
                           command=(lambda: self.set_head_pos(Waist.MidRight, "Middle Right")))
        fr_button = Button(direction_frame, width=15, text="Far Right", bg="white", fg="Black",
                           command=(lambda: self.set_head_pos(Waist.FarRight, "Far Right")))
        # Make Labels
        direction_label = Label(direction_frame, bg="white", text="Choose speed:")

        # Add buttons and labels
        direction_label.grid(row=0, column=1, sticky='w')
        fl_button.grid(row=1, column=1, sticky="senw")
        ml_button.grid(row=1, column=2, sticky="senw")
        m_button.grid(row=1, column=3, sticky="senw")
        mr_button.grid(row=1, column=4, sticky="senw")
        fr_button.grid(row=1, column=5, sticky="senw")

    def display_gif(self, gifName, totalFrames):
        popup = Toplevel()
        print("Popup created")
        frameCount = 0
        i = 0
        while(self.scheduler.running == True):
            gif = PhotoImage(file = gifName, format = "gif -index" + str(frameCount))
            stop_button = Button(popup, command = self.stop, image = gif)
            stop_button.image = gif
            stop_button.grid(column ="0", row ="0")
            time.sleep(.02)
            i +=1
            if(i > 50):
                if(frameCount == (totalFrames -1)):
                    frameCount = 0
                else:
                    print("Updating frames")
                    frameCount += 1

        popup.destroy()

    def stop(self):
        self.scheduler.enable = False

    def go_button_clicked(self):
        self.scheduler.guiQueue = self.queuedCommands
        self.scheduler.run()
        gifthread =threading.Thread(None, lambda: self.display_gif("caution.gif", 5))
        gifthread.start()
        print("The milk done poured")

    def main(self):
        # create main window
        self.window.title("ROBO_GUI")
        self.window.geometry('{}x{}'.format(GUI.WIDTH, GUI.HEIGHT))
        self.window.configure(background='white')

        # Make Containers
        top_button_frame = Frame(self.window, bg="black", width=.75 * GUI.WIDTH, height=.50 * GUI.HEIGHT, pady=0,
                                 padx=0)
        bot_button_frame = Frame(self.window, bg="black", width=.75 * GUI.WIDTH, height=.50 * GUI.HEIGHT, pady=0,
                                 padx=0)
        self.queue_frame = Frame(self.window, bg="white", width=GUI.WIDTH, height=.50 * GUI.HEIGHT, pady=0, padx=0)
        start_frame = Frame(self.window, bg="black", width=.25 * GUI.WIDTH, height=.25 * GUI.HEIGHT, pady=0, padx=0)

        # Main container layout
        self.window.grid_rowconfigure(0, weight=0)
        self.window.grid_columnconfigure(1, weight=0)

        top_button_frame.grid(row=0, column=0)
        bot_button_frame.grid(row=2, column = 0)
        self.queue_frame.grid(row=0, column=1, sticky = "nw")
        start_frame.grid(row=2, column=1)

        # Make buttons
        fb_button = Button(top_button_frame, width=35, height=13, text="FORWARD/BACKWARD", bg="white", fg="Black",
                          command=self.f_button_clicked)
        lr_button = Button(top_button_frame, width=35, height=13, text="ROTATE", bg="white", fg="Black",
                          command=self.l_button_clicked)
        h_button = Button(bot_button_frame, width=35, height=13, text="HEAD SWIVEL", bg="white", fg="Black",
                          command=self.h_button_clicked)
        w_button = Button(bot_button_frame, width=35, height=13, text="WAIST SWIVEL", bg="white", fg="Black",
                          command=self.w_button_clicked)
        go_button = Button(start_frame, width=40, height=5, text="Go!", bg="green2", fg="Black",
                           command=self.go_button_clicked)


        #Make Labels


        # Add buttons to frames
        fb_button.grid(row=0, column=0, sticky="nsew")
        lr_button.grid(row=0, column=1, sticky="nsew")
        h_button.grid(row=0, column=0, sticky="se")
        w_button.grid(row=0, column=1, sticky="SE")

        #Add_labels
        #l0.grid(row = 0, column =0, sticky = 'w')
        #l1.grid(row = 1, column =0, sticky = 'w')
        #l2.grid(row = 2, column =0, sticky = 'w')
        #l3.grid(row = 3, column =0, sticky = 'w')
        #l4.grid(row = 4, column =0, sticky = 'w')
        #l5.grid(row = 5, column =0, sticky = 'w')
        #l6.grid(row = 6, column =0, sticky = 'w')
        #l7.grid(row = 7, column =0, sticky = 'w')
        #l8.grid(row = 8, column =0, sticky = 'w')

        go_button.grid(sticky="snew")

        self.window.mainloop()

if __name__ == "__main__":
    print("Test")
    gui = GUI()
    gui.main()
