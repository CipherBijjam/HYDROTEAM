import tkinter as tk

# TODO: Remove Cyclic Dependencies
class SelectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background = '#D6E9D2')
        self.initUI(parent, controller)

    def initUI(self, parent, controller):

        from homePage import HomePage
        HomeButton = self.custom_button(text = "Home", 
        command =  lambda: controller.show_frame(HomePage))
        HomeButton.place(x = 10, y = 10, width = 125, height = 35)

        from taskOne import TaskOne
        TaskOneButton = self.custom_button(text = "TaskOne", 
        command =  lambda: controller.show_frame(TaskOne))
        TaskOneButton.place(x = 140, y = 10, width = 125, height = 35)

        from taskTwo import TaskTwo
        TaskTwoButton = self.custom_button(text = "TaskTwo", 
        command =  lambda: controller.show_frame(TaskTwo))
        TaskTwoButton.place(x = 270, y = 10, width = 125, height = 35)

        from taskThree import TaskThree
        TaskThreeButton = self.custom_button(text = "TaskThree", 
        command =  lambda: controller.show_frame(TaskThree))
        TaskThreeButton.place(x = 400, y = 10, width = 125, height = 35)

    def custom_button(self, text, command):
        return tk.Button(self, text = text, 
        command =  command, 
        padx = 10,
        pady = 10)
