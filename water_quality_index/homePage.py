import tkinter as tk

from selectPage import SelectPage
from vars import Vars

class HomePage(SelectPage):

    def __init__(self, parent, controller):
        SelectPage.__init__(self, parent, controller)
        label = tk.Label(self, text = "Water Quality Estimation Tool", font = Vars.LARGE_FONT)
        label.place(x = 160, y = 100)
        label = tk.Label(self, text = "Triple I T Presents", font = Vars.LABEL_FONT)
        label.place(x = 160, y = 80)
        instructions = []
        instructions.append(tk.Label(self, text = "TaskOne calculates the Water Quality Index using the weighted mean strategy.", font = ("Verdana", 15)))
        instructions[0].place(x = 10, y = 190)

        instructions.append(tk.Label(self, text = "TaskTwo calculates the Overall Index of Pollution in Indian Context.", font = ("Verdana", 15)))
        instructions[1].place(x = 10, y = 220)

        instructions.append(tk.Label(self, text = "TaskThree calculates the Water Quality Index using ML given input as a time series", font = ("Verdana", 15)))
        instructions[2].place(x = 10, y = 250)

