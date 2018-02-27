from tkinter import *


class GUI:
    WIDTH = 800
    HEIGHT = 450
    POP_WIDTH = 500
    POP_HEIGHT = 300

    def __init__(self, tkinter_ref = None):
        if tkinter_ref == None:
            tkinter_ref = Tk()
        self.speed = "slow"
        self.angle = 0
        self.head_pos = "middle"
        self.window = tkinter_ref
        self.fb = StringVar(self.window)
        self.fb.set("Forward")
        self.lr = StringVar(self.window)
        self.lr.set("Right")

    def set_slow(self):
        self.speed = "slow"

    def set_medium(self):
        self.speed = "medium"

    def set_fast(self):
        self.speed = "fast"

    def add_command(self):
        print("Command Added")

    def cancel(self):
        self.popup.destroy()
        print("canceling")

    def set_L45(self):
        self.angle = 45

    def set_L90(self):
        self.angle = 90

    def set_L135(self):
        self.angle = 135

    def set_L180(self):
        self.angle = 180

    def set_R45(self):
        self.angle = 45

    def set_R90(self):
        self.angle = 90

    def set_R135(self):
        self.angle = 135

    def set_R180(self):
        self.angle = 180

    def set_fl_head_pos(self):
        self.head_pos = "Full left"

    def set_ml_head_pos(self):
        self.head_pos = "Middle Left"

    def set_m_head_pos(self):
        self.head_pos = "Middle"

    def set_mr_head_pos(self):
        self.head_pos = "Middle Right"

    def set_fr_head_pos(self):
        self.head_pos = "Full Right"

    def f_button_clicked(self):
        self.popup = Toplevel(self.window)
        self.popup.configure(background='White')

        # Make frames
        speed_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        duration_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        option_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        parallel_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        button_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=3, padx=3)

        # Configure Layout
        self.popup.grid_rowconfigure(1, weight=1)
        self.popup.grid_columnconfigure(0, weight=1)

        speed_frame.grid(row=0, column=0, sticky="w")
        duration_frame.grid(row=1, column=0, sticky="w")
        option_frame.grid(row = 2, column = 0, sticky = "w")
        parallel_frame.grid(row=3, column=0, sticky="w")
        button_frame.grid(row=4, column=0, sticky="w")

        # make buttons
        slow_button = Button(speed_frame, width=23, text="Slow", bg="white", fg="Black",
                             command=self.set_slow)
        med_button = Button(speed_frame, width=23, text="Medium", bg="white", fg="Black",
                            command=self.set_medium)
        fast_button = Button(speed_frame, width=23, text="Fast", bg="white", fg="Black",
                             command=self.set_fast)
        add_button = Button(button_frame, width=15, height=1, text="Add", bg="white", fg="Black",
                            command=self.add_command)
        cancel_button = Button(button_frame, width=15, height=1, text="Cancel", bg="white", fg="Black",
                               command=self.cancel)
        # make spinbox
        duration_spinbox = Spinbox(duration_frame, bg='White', from_=0.1, to=10.0, width=20, format='%2.1f',
                                   increment='0.1', font='Helvetica 36', )
        # Make option meny
        fb_option = OptionMenu(option_frame, self.fb, "Forward", "Backward")

        # make checkbutton
        parallel_check = Checkbutton(parallel_frame, bg='White')

        # Make Labels
        speed_label = Label(speed_frame, bg="white", text="Choose speed:")
        duration_label = Label(duration_frame, bg="white", text="Enter duration in seconds:")
        option_label = Label(option_frame, bg="white", text = "Choose direction:")
        parallel_label = Label(parallel_frame, bg="White", text="Make this action run in parallel?")

        # Add buttons and labels
        speed_label.grid(row=0, column=1, sticky='w')
        slow_button.grid(row=1, column=1, sticky="senw")
        med_button.grid(row=1, column=2, sticky="senw")
        fast_button.grid(row=1, column=3, sticky="senw")

        duration_label.grid(row=0, sticky='w')
        duration_spinbox.grid(row=1, sticky='w')

        option_label.grid(row = 0, column = 0, sticky = 'w')
        fb_option.grid(row = 0 , column =1, sticky = 'w')

        parallel_label.grid(row=0, sticky='w')
        parallel_check.grid(row=0, column=1, sticky='e')

        add_button.grid(row=0, column=3, sticky='w')
        cancel_button.grid(row=0, column=4, sticky='e')

    def l_button_clicked(self):
        self.popup = Toplevel(self.window)
        self.popup.configure(background='White')

        # Make frames
        speed_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        duration_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        option_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        parallel_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=5, padx=3)
        button_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.20 * GUI.POP_WIDTH, pady=3, padx=3)

        # Configure Layout
        self.popup.grid_rowconfigure(1, weight=1)
        self.popup.grid_columnconfigure(0, weight=1)

        speed_frame.grid(row=0, column=0, sticky="w")
        duration_frame.grid(row=1, column=0, sticky="w")
        option_frame.grid(row = 2, column = 0, sticky = "w")
        parallel_frame.grid(row=3, column=0, sticky="w")
        button_frame.grid(row=4, column=0, sticky="w")

        # make buttons
        slow_button = Button(speed_frame, width=23, text="Slow", bg="white", fg="Black",
                             command=self.set_slow)
        med_button = Button(speed_frame, width=23, text="Medium", bg="white", fg="Black",
                            command=self.set_medium)
        fast_button = Button(speed_frame, width=23, text="Fast", bg="white", fg="Black",
                             command=self.set_fast)
        add_button = Button(button_frame, width=15, height=1, text="Add", bg="white", fg="Black",
                            command=self.add_command)
        cancel_button = Button(button_frame, width=15, height=1, text="Cancel", bg="white", fg="Black",
                               command=self.cancel)
        # make spinbox
        duration_spinbox = Spinbox(duration_frame, bg='White', from_=0.1, to=10.0, width=20, format='%2.1f',
                                   increment='0.1', font='Helvetica 36', )
        # Make option meny
        fb_option = OptionMenu(option_frame, self.lr, "Right", "Left")

        # make checkbutton
        parallel_check = Checkbutton(parallel_frame, bg='White')

        # Make Labels
        speed_label = Label(speed_frame, bg="white", text="Choose speed:")
        duration_label = Label(duration_frame, bg="white", text="Enter duration in seconds:")
        option_label = Label(option_frame, bg="white", text = "Choose direction:")
        parallel_label = Label(parallel_frame, bg="White", text="Make this action run in parallel?")

        # Add buttons and labels
        speed_label.grid(row=0, column=1, sticky='w')
        slow_button.grid(row=1, column=1, sticky="senw")
        med_button.grid(row=1, column=2, sticky="senw")
        fast_button.grid(row=1, column=3, sticky="senw")

        duration_label.grid(row=0, sticky='w')
        duration_spinbox.grid(row=1, sticky='w')

        option_label.grid(row = 0, column = 0, sticky = 'w')
        fb_option.grid(row = 0 , column =1, sticky = 'w')

        parallel_label.grid(row=0, sticky='w')
        parallel_check.grid(row=0, column=1, sticky='e')

        add_button.grid(row=0, column=3, sticky='w')
        cancel_button.grid(row=0, column=4, sticky='e')

    def r_button_clicked(self):
        self.popup = Toplevel(self.window)
        self.popup.configure(background='White')

        # Make frames
        angle_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=5, padx=3)
        parallel_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=5, padx=3)
        button_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=3, padx=3)

        # Configure Layout
        self.popup.grid_rowconfigure(1, weight=1)
        self.popup.grid_columnconfigure(0, weight=1)

        angle_frame.grid(row=0, column=0, sticky="w")
        parallel_frame.grid(row=1, column=0, sticky="w")
        button_frame.grid(row=2, column=0, sticky="w")

        # make buttons
        _45_button = Button(angle_frame, width=14, text="45 degrees", bg="white", fg="Black",
                            command=self.set_R45)
        _90_button = Button(angle_frame, width=14, text="90 degrees", bg="white", fg="Black",
                            command=self.set_R90)
        _135_button = Button(angle_frame, width=14, text="135 degrees", bg="white", fg="Black",
                             command=self.set_R135)
        _180_button = Button(angle_frame, width=14, text="180 degrees", bg="white", fg="Black",
                             command=self.set_R180)
        add_button = Button(button_frame, width=15, height=1, text="Add", bg="white", fg="Black",
                            command=self.add_command)
        cancel_button = Button(button_frame, width=15, height=1, text="Cancel", bg="white", fg="Black",
                               command=self.cancel)
        # make checkbutton
        parallel_check = Checkbutton(parallel_frame, bg='White')

        # Make Labels
        angle_label = Label(angle_frame, bg="white", text="Choose angle:")
        parallel_label = Label(parallel_frame, bg="White", text="Make this action run in parallel?")

        # Add buttons and labels
        angle_label.grid(row=0, column=1, sticky='w')
        _45_button.grid(row=1, column=1, sticky="senw")
        _90_button.grid(row=1, column=2, sticky="senw")
        _135_button.grid(row=1, column=3, sticky="senw")
        _180_button.grid(row=1, column=4, sticky="senw")

        parallel_label.grid(row=0, sticky='w')
        parallel_check.grid(row=0, column=1, sticky='e')

        add_button.grid(row=0, column=3, sticky='w')
        cancel_button.grid(row=0, column=4, sticky='e')

    def h_button_clicked(self):
        self.popup = Toplevel(self.window)
        self.popup.configure(background='White')

        # Make frames
        direction_ud_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=5,
                                   padx=3)
        direction_lr_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=5,
                                   padx=3)
        duration_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=5, padx=3)
        parallel_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=5, padx=3)
        button_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=3, padx=3)

        # Configure Layout
        self.popup.grid_rowconfigure(1, weight=1)
        self.popup.grid_columnconfigure(0, weight=1)

        direction_ud_frame.grid(row=0, column=0, sticky="w")
        direction_lr_frame.grid(row=1, column=0, sticky="w")
        # duration_frame.grid(row=2, column=0, sticky="w")
        parallel_frame.grid(row=3, column=0, sticky="w")
        button_frame.grid(row=4, column=0, sticky="w")

        # make buttons
        ud_scale = Scale(direction_ud_frame, bg='White', bd=4, from_=-10, to=10, resolution=1, orient=HORIZONTAL,
                         sliderlength=30, length=400, width=30)
        lr_scale = Scale(direction_lr_frame, bg='White', bd=4, from_=-10, to=10, resolution=1, orient=HORIZONTAL,
                         sliderlength=30, length=400, width=30)
        add_button = Button(button_frame, width=15, height=1, text="Add", bg="white", fg="Black",
                            command=self.add_command)
        cancel_button = Button(button_frame, width=15, height=1, text="Cancel", bg="white", fg="Black",
                               command=self.cancel)
        # make spinbox
        # duration_spinbox = Spinbox(duration_frame, bg='White', from_=0.1, to=10.0, width=20, format='%2.1f',
        #                       increment='0.1', font='Helvetica 36', )

        # make checkbutton
        parallel_check = Checkbutton(parallel_frame, bg='White')

        # Make Labels
        ud_label = Label(direction_ud_frame, bg="white", text="Adjust slider to look up or down:")
        lr_label = Label(direction_lr_frame, bg='White', text="Adjust slider to look left or right:")
        # duration_label = Label(duration_frame, bg="white", text="Enter duration in seconds:")
        parallel_label = Label(parallel_frame, bg="White", text="Make this action run in parallel?")

        # Add buttons and labels
        ud_label.grid(row=1, column=1, sticky='w')
        ud_scale.grid(row=1, column=2, sticky='e')
        lr_label.grid(row=1, column=1, sticky="w")
        lr_scale.grid(row=1, column=2, sticky="e")

        # duration_label.grid(row=0, sticky='w')
        # duration_spinbox.grid(row=1, sticky='w')

        parallel_label.grid(row=0, sticky='w')
        parallel_check.grid(row=0, column=1, sticky='e')

        add_button.grid(row=0, column=3, sticky='w')
        cancel_button.grid(row=0, column=4, sticky='e')

    def w_button_clicked(self):
        self.popup = Toplevel(self.window)
        self.popup.configure(background='White')

        # Make frames
        direction_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=5, padx=3)
        duration_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=5, padx=3)
        parallel_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=5, padx=3)
        button_frame = Frame(self.popup, bg="white", width=GUI.POP_WIDTH, height=.25 * GUI.POP_WIDTH, pady=3, padx=3)

        # Configure Layout
        self.popup.grid_rowconfigure(1, weight=1)
        self.popup.grid_columnconfigure(0, weight=1)

        direction_frame.grid(row=0, column=0, sticky="w")
        duration_frame.grid(row=1, column=0, sticky="w")
        parallel_frame.grid(row=2, column=0, sticky="w")
        button_frame.grid(row=3, column=0, sticky="w")

        # make buttons
        fl_button = Button(direction_frame, width=15, text="Full Left", bg="white", fg="Black",
                           command=self.set_fl_head_pos)
        ml_button = Button(direction_frame, width=15, text="Middle Left", bg="white", fg="Black",
                           command=self.set_ml_head_pos)
        m_button = Button(direction_frame, width=15, text="Middle", bg="white", fg="Black",
                          command=self.set_m_head_pos)
        mr_button = Button(direction_frame, width=15, text="Middle Right", bg="white", fg="Black",
                           command=self.set_mr_head_pos)
        fr_button = Button(direction_frame, width=15, text="Full Right", bg="white", fg="Black",
                           command=self.set_fr_head_pos)
        add_button = Button(button_frame, width=15, height=1, text="Add", bg="white", fg="Black",
                            command=self.add_command)
        cancel_button = Button(button_frame, width=15, height=1, text="Cancel", bg="white", fg="Black",
                               command=self.cancel)
        # make spinbox
        duration_spinbox = Spinbox(duration_frame, bg='White', from_=0.1, to=10.0, width=20, format='%2.1f',
                                   increment='0.1', font='Helvetica 36', )

        # make checkbutton
        parallel_check = Checkbutton(parallel_frame, bg='White')

        # Make Labels
        direction_label = Label(direction_frame, bg="white", text="Choose speed:")
        duration_label = Label(duration_frame, bg="white", text="Enter duration in seconds:")
        parallel_label = Label(parallel_frame, bg="White", text="Make this action run in parallel?")

        # Add buttons and labels
        direction_label.grid(row=0, column=1, sticky='w')
        fl_button.grid(row=1, column=1, sticky="senw")
        ml_button.grid(row=1, column=2, sticky="senw")
        m_button.grid(row=1, column=3, sticky="senw")
        mr_button.grid(row=1, column=4, sticky="senw")
        fr_button.grid(row=1, column=5, sticky="senw")

        duration_label.grid(row=0, sticky='w')
        duration_spinbox.grid(row=1, sticky='w')

        parallel_label.grid(row=0, sticky='w')
        parallel_check.grid(row=0, column=1, sticky='e')

        add_button.grid(row=0, column=3, sticky='w')
        cancel_button.grid(row=0, column=4, sticky='e')

    def go_button_clicked(self):
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
        queue_frame = Frame(self.window, bg="white", width=GUI.WIDTH, height=.50 * GUI.HEIGHT, pady=0, padx=0)
        start_frame = Frame(self.window, bg="black", width=.25 * GUI.WIDTH, height=.25 * GUI.HEIGHT, pady=0, padx=0)

        # Main container layout
        self.window.grid_rowconfigure(0, weight=0)
        self.window.grid_columnconfigure(1, weight=0)

        top_button_frame.grid(row=0, column=0)
        bot_button_frame.grid(row=2, column = 0)
        queue_frame.grid(row=0, column=1, sticky = "nw")
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
        l0 = Label(queue_frame, bg="white", text="Queue:", font = 'Helvetica 14')
        l1 = Label(queue_frame, bg="white", text="Move Forward, duration = 1, medium, P", font = 'Helvetica 12')
        l2 = Label(queue_frame, bg="white", text="Move Forward, duration = 1, medium", font = 'Helvetica 12')
        l3 = Label(queue_frame, bg="white", text="Move Forward, duration = 1, medium", font = 'Helvetica 12')
        l4 = Label(queue_frame, bg="white", text="Move Forward, duration = 1", font = 'Helvetica 12')
        l5 = Label(queue_frame, bg="white", text="Move Forward, duration = 1", font = 'Helvetica 12')
        l6 = Label(queue_frame, bg="white", text="Move Forward, duration = 1", font = 'Helvetica 12')
        l7 = Label(queue_frame, bg="white", text="Move Forward, duration = 1", font = 'Helvetica 12')
        l8 = Label(queue_frame, bg="white", text="Move Forward, duration = 1", font = 'Helvetica 12')


        # Add buttons to frames
        fb_button.grid(row=0, column=0, sticky="nsew")
        lr_button.grid(row=0, column=1, sticky="nsew")
        h_button.grid(row=0, column=0, sticky="se")
        w_button.grid(row=0, column=1, sticky="SE")

        #Add_labels
        l0.grid(row = 0, column =0, sticky = 'w')
        l1.grid(row = 1, column =0, sticky = 'w')
        l2.grid(row = 2, column =0, sticky = 'w')
        l3.grid(row = 3, column =0, sticky = 'w')
        l4.grid(row = 4, column =0, sticky = 'w')
        l5.grid(row = 5, column =0, sticky = 'w')
        l6.grid(row = 6, column =0, sticky = 'w')
        l7.grid(row = 7, column =0, sticky = 'w')
        l8.grid(row = 8, column =0, sticky = 'w')


        go_button.grid(sticky="snew")

        self.window.mainloop()

if __name__ == "__main__":
    print("Test")
    gui = GUI()
    gui.main()
