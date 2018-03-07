from tkinter import *
from collections import namedtuple
#from Scheduler import Scheduler
from Drivetrain import Drivetrain
from Waist import Waist
import threading 
import time


class GifFrame(object):
    def __init__(self):
        self.frameCount = 0
        self._window = Toplevel()
        self._window.attributes("-fullscreen", True)
        self._window.configure(background = "black")
        self.imageGIF2 = PhotoImage(file="tenor.gif", format="gif -index " + str(self.frameCount))
        self._window.grid_rowconfigure(1, weight=1)
        self._window.grid_columnconfigure(1, weight = 1)
        self.imageLabel2 = Label(self._window, image=self.imageGIF2)
        self.imageLabel2.grid(column=1,row=1)
        
        

    def update(self):
        try:
            self.imageGIF2 = PhotoImage(file="tenor.gif", format="gif -index " + str(self.frameCount))
            self.imageLabel2.configure(image=self.imageGIF2)
        except:
            self.frameCount = 0
            self.imageGIF2 = PhotoImage(file="tenor.gif", format="gif -index " + str(self.frameCount))
            self.imageLabel2.configure(image=self.imageGIF2)
        self.frameCount += 1

    def win(self):
        return self._window

    def destroy(self):
        self._window.destroy()

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
        self.row_counter = 2
        self.total_duration = 0

    def set_speed(self, speed):
        self.speed = speed

    def add_command(self):

        self.duration = self.duration_spinbox.get()
        if self.channel == 1:
            self.target = self.speed + 6000 if self.fb.get() == 'Forward' else 6000 - self.speed
        elif self.channel == 2:
            self.target = self.speed + 6000 if self.fb.get() == 'Left' else 6000 - self.speed
        elif self.channel == 3:
            self.channel = 3 if self.fb.get() == 'Horizontal' else 4
            self.target = int(self.head_scale.get() * 3000 / self.head_scale['to']) + 6000

        SetPoint = namedtuple('SetPoint', ['channel', 'timeout', 'target', 'parallel', 'index'])
        temp = SetPoint(channel = self.channel, timeout = int(float(self.duration)*1000), target = self.target, parallel = self.parallel.get(), index = len(self.queuedCommands))
        if(self.edit == True):
            self.queuedCommands[self.index] = temp
        else:
            self.queuedCommands.append(temp)
        self.add_to_queue()
        self.popup.destroy()

    def add_to_queue(self):
        check = ""
        index = self.row_counter
        if(self.parallel==True):
            check = "P"
        if self.channel == 0:
            text = "Rotate Waist " + self.pos_string + ", D= " + str(self.duration)+ ", " + check
            bcommand = lambda: w_button_clicked(self.duration, self.parallel.get(), self.pos, self.pos_string, True, index)
        elif self.channel == 1:
            text = "Move " + self.fb.get() + ", D= " + str(self.duration) + ", " + check
            bcommand = lambda: f_button_clicked(self.duration, self.parallel.get(), self.fb.get(), self.speed, True, index)
        elif self.channel == 2:
            text = "Rotate " + self.fb.get() + ", D= " + str(self.duration) +", " + str(self.target) + check
            bcommand = lambda: l_button_clicked(self.duration, self.parallel.get(), self.fb.get(), self.speed, True, index)
        elif self.channel == 3:
            text = "Rotate Head " + str(self.head_scale.get()) + ", D= " + str(self.duration) + ", " + 
            bcommand = lambda: h_button_clicked(self.duration, self.parallel.get(), self.fb.get(), self.target, True, index)
        else:
            text = "Move Head " + str(self.head_scale.get()) + ", D= " + str(self.duration) + ", " + check
            bcommand = lambda: h_button_clicked(self.duration, self.parallel.get(), self.fb.get(), self.target, True, index)
        if(self.edit)
        self.queue_button = Button(self.queue_frame, bg="white", text= text, font = 'Helvetica 12')
        if(self.edit == True):
            for button in self.queue_frame.grid_slaves():
                if int(button.grid_info()["row"]) = self.index:
                    button.grid_forget()
            self.queue_button.grid(row = self.index, sticky = "nw", command = bcommand)
            pass
        else:
            self.queue_button.grid(row = self.row_counter, sticky = "nw", command = bcommand)
            self.row_counter +=1
        self.total_duration = self.total_duration+float(self.duration)
        print(str(self.total_duration))
    def clear_queue(self):
        for button in self.queue_frame.grid_slaves():
            if int(button.grid_info()["row"]) > 1:
                button.grid_forget()
        self.row_counter = 2
        self.queuedCommands = []
    def cancel(self):
        self.popup.destroy()

    def set_angle(self, angle):
        self.target = angle

    def set_head_pos(self, pos, pos_string):
        self.target = pos
        self.pos_string = pos_string
    def initialize_popup(self, duration = 0.1, parallel = False, edit = False):
        self.popup = Toplevel(self.window)
        self.popup.configure(background='White')

        # Make frames
        parallel_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        button_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=3, padx=3)

        # Configure Layout
        self.popup.grid_rowconfigure(1, weight=1)
        self.popup.grid_columnconfigure(0, weight=1)

        duration_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        duration_frame.grid(row=1, column=0, sticky="w")
        # make spinbox
        self.duration_spinbox = Spinbox(duration_frame, bg='White', from_=0.1, to=10.0, width=20, format='%2.1f',
                                   increment='0.1', font='Helvetica 36', textvariable=)
        duration_label = Label(duration_frame, bg="white", text="Enter duration in seconds:")
        duration_label.grid(row=0, sticky='w')
        self.duration_spinbox.grid(row=1, sticky='w')

        parallel_frame.grid(row=3, column=0, sticky="w")
        # make checkbutton
        self.parallel = BooleanVar()
        self.parallel.set(False)
        parallel_check = Checkbutton(parallel_frame, bg='White', variable = self.parallel)
        parallel_label = Label(parallel_frame, bg="White", text="Make this action run in parallel?")
        parallel_label.grid(row=0, sticky='w')
        parallel_check.grid(row=0, column=1, sticky='e')

        button_frame.grid(row=4, column=0, sticky="w")
        add_button = Button(button_frame, width=15, height=1, text="Add", bg="white", fg="Black",
                        command=lambda: self.add_command(edit))
        cancel_button = Button(button_frame, width=15, height=1, text="Cancel", bg="white", fg="Black",
                        command=self.cancel)
        add_button.grid(row=0, column=3, sticky='w')
        cancel_button.grid(row=0, column=4, sticky='e')

    def speed_frame_init(self, speed):
        self.set_speed(speed)
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

    def option_init(self, option1, option2, option):
        self.fb.set(option)
        option_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        option_frame.grid(row = 2, column = 0, sticky = "w")

        # Make option menu
        fb_option = OptionMenu(option_frame, self.fb, option1, option2)
        option_label = Label(option_frame, bg="white", text = "Choose direction:")
        option_label.grid(row = 0, column = 0, sticky = 'w')
        fb_option.grid(row = 0 , column =1, sticky = 'w')

    def f_button_clicked(self, duration = 0.1, parallel = False, option = "Forward", speed = Drivetrain.Slow, edit = False, index = 0):
        if(edit == True):
            self.index = index
        self.edit = edit
        self.initialize_popup(duration, parallel, edit)
        self.speed_frame_init(speed)
        self.option_init("Forward", "Backward", option)
        self.channel = 1

    def l_button_clicked(self, duration = 0.1, parallel = False, option = "Right", speed = Drivetrain.Slow, edit = False, index = 0):
        if(edit == True):
            self.index = index
        self.edit = edit
        self.initialize_popup()
        self.speed_frame_init(speed)
        self.option_init("Right", "Left", option)
        self.channel = 2

    def h_button_clicked(self, duration = 0.1, parallel = False, option = "Vertical", scale = 0, edit = False, index = 0):
        if(edit == True):
            self.index = index
        self.edit = edit
        self.initialize_popup()
        self.option_init("Vertical", "Horizontal", option)
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
        self.head_scale.set(scale)
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

    def w_button_clicked(self, duration = 0.1, parallel = False, pos = Waist.Middle, pos_string = "Middle", edit = False, index = 0):
        if(edit == True):
            self.index = index
        self.edit = edit
        self.initialize_popup()
        self.channel = 0
        self.set_head_pos(pos, pos_string)
        # Make frames
        direction_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=5, padx=3)
        direction_frame.grid(row=0, column=0, sticky="w")

        # make buttons
        fl_button = Button(direction_frame, width=15, text="Far Left", bg="white", fg="Black",
                           command=(lambda: self.set_head_pos(Waist.FarLeft, "FL")))
        ml_button = Button(direction_frame, width=15, text="Middle Left", bg="white", fg="Black",
                           command=(lambda: self.set_head_pos(Waist.MidLeft, "ML")))
        m_button = Button(direction_frame, width=15, text="Middle", bg="white", fg="Black",
                          command=(lambda: self.set_head_pos(Waist.Middle, "M")))
        mr_button = Button(direction_frame, width=15, text="Middle Right", bg="white", fg="Black",
                           command=(lambda: self.set_head_pos(Waist.MidRight, "MR")))
        fr_button = Button(direction_frame, width=15, text="Far Right", bg="white", fg="Black",
                           command=(lambda: self.set_head_pos(Waist.FarRight, "FR")))
        # Make Labels
        direction_label = Label(direction_frame, bg="white", text="Choose speed:")

        # Add buttons and labels
        direction_label.grid(row=0, column=1, sticky='w')
        fl_button.grid(row=1, column=1, sticky="senw")
        ml_button.grid(row=1, column=2, sticky="senw")
        m_button.grid(row=1, column=3, sticky="senw")
        mr_button.grid(row=1, column=4, sticky="senw")
        fr_button.grid(row=1, column=5, sticky="senw")

    def draw_animation(self, sm, delay):
        sm.update()
        if self.gifDisplay == True:
            sm.win().after(delay, self.draw_animation, sm, delay)


    def run_animation(self):
        self.gifDisplay = True
        print("Gif displaying")
        duration = self.total_duration
        print("Duration")
        sm = GifFrame()
        print("Frame made")
        drawThread = threading.Thread(None,lambda: self.draw_animation(sm, 100))
        drawThread.start()
        print("Thread started")
        time.sleep(duration)
        print("Wait over")
        self.gifDisplay = False
        time.sleep(.1)
        print("Sleeping over")
        sm.destroy()
        

    def display_gif(self, gifName, totalFrames):
        self.gifDisplay = True
        self.init_gif(gifName, totalFrames)
        displayThread = threading.Thread(None, lambda: self.manage_gif())
        displayThread.start()
        while self.gifDisplay == True:
            time.sleep(.1)
        self.gif_popup.destroy()

    def init_gif(self, gifName, totalFrames):
        self.gif_popup = Toplevel()
        self.gif_popup.attributes("-fullscreen", True)
        print("Popup created")
        self.gif_popup.stop_button = Button(self.gif_popup, command = self.stop, bg = "Red", text="Stop")
        self.gif_popup.gifLabel = Label(self.gif_popup)
        self.gif_popup.gifLabel.grid(column=0, row=0)
        self.gif_popup.stop_button.grid(column=0, row=1)
        self.gif_popup.frameCount = 0
        self.gif_popup.gifName = gifName
        self.gif_popup.totalFrames = totalFrames

    def manage_gif(self):
        if(self.gifDisplay == True):
            self.update_gif()
            self.gif_popup.after(100, self.manage_gif, self)

    def update_gif(self):
        self.gif_popup.gif = PhotoImage(file = self.gif_popup.gifName, format = "gif -index " + str(self.gif_popup.frameCount))
        self.gif_popup.gifLabel.configure(image=self.gif_popup.gif)
        self.gif_popup.gifLabel.image = self.gif_popup.gif
        if(self.gif_popup.frameCount == (self.gif_popup.totalFrames -1)):
            self.gif_popup.frameCount = 0
        else:
            self.gif_popup.frameCount += 1

    def stop(self):
        self.scheduler.enable = False
        self.gifDisplay = False
        
    def go_button_clicked(self):
        self.scheduler.new = True
        self.scheduler.guiQueue = self.queuedCommands
        #schedulerThread =threading.Thread(None, self.scheduler.run)
        #gifthread =threading.Thread(None, lambda: self.display_gif("tenor.gif", 4))
        gifthread =threading.Thread(None, lambda: self.run_animation())
        gifthread.start()
        #schedulerThread.start()
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
        self.queue_frame = Frame(self.window, bg="white", width=.25 * GUI.WIDTH, height=.75 * GUI.HEIGHT, pady=0, padx=0)
        start_frame = Frame(self.window, bg="black", width=.25 * GUI.WIDTH, height=.25 * GUI.HEIGHT, pady=0, padx=0)

        # Main container layout
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight = 1)

        top_button_frame.grid(row=0, column=0)
        bot_button_frame.grid(row=1, column = 0)
        self.queue_frame.grid(row=0, rowspan = 2, column=1, sticky = "nw")
       # start_frame.grid(row=2, column=1)

        # Make buttons
        fb_button = Button(top_button_frame, width=30, height=15, text="FORWARD/BACKWARD", bg="cyan2", fg="Black",
                          command=self.f_button_clicked)
        lr_button = Button(top_button_frame, width=30, height=15, text="ROTATE", bg="cyan2", fg="Black",
                          command=self.l_button_clicked)
        h_button = Button(bot_button_frame, width=30, height=15, text="HEAD SWIVEL", bg="cyan2", fg="Black",
                          command=self.h_button_clicked)
        w_button = Button(bot_button_frame, width=30, height=15, text="WAIST SWIVEL", bg="cyan2", fg="Black",
                          command=self.w_button_clicked)
        go_button = Button(self.queue_frame, width=30, height=5, text="Go!", bg="green2", fg="Black",
                           command=self.go_button_clicked)
        clear_button =Button(self.queue_frame, width=30, height = 2, text = "Clear Queue", bg = "red2", command = self.clear_queue)


        #Make Labels


        # Add buttons to frames
        fb_button.grid(row=0, column=0, sticky="nsew")
        lr_button.grid(row=0, column=1, sticky="nsew")
        h_button.grid(row=0, column=0, sticky="se")
        w_button.grid(row=0, column=1, sticky="SE")
        go_button.grid(row=0, column = 0, sticky = "nw")
        clear_button.grid(row = 1, column = 0, sticky = "nw")
        go_button.grid(sticky="sw")

        self.window.mainloop()

if __name__ == "__main__":
    print("Test")
    gui = GUI()
    gui.main()
