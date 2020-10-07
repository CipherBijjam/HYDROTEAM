import tkinter as tk

from selectPage import SelectPage
from vars import Vars
import tkinter.filedialog as tkfd
from inferThree import findWQI

class TaskThree(SelectPage):

    def __init__(self, parent, controller):
        SelectPage.__init__(self, parent, controller)
        # label = tk.Label(self, text = "Task Three", font = Vars.LARGE_FONT)
        # label.place(x = 450, y = 300)
                # CSV File
        self.csv_text = tk.StringVar()
        self.csv_text.set("CSV File Upload")
        self.csv_label = tk.Label(self, textvariable = self.csv_text, font = Vars.LABEL_FONT)
        self.csv_label.place(x = 200, y = 150)

        self.fileInput = tk.Entry(self)
        self.fileInput.place(x = 200, y = 200, w = 200)

        self.chooseFile = tk.Button(self, text = "Input File", 
        command =  lambda: self.open_file(), 
        padx = 10,
        pady = 10)
        self.chooseFile.place(x = 450, y = 200, width = 125, height = 35)

        self.fileOutput = tk.Entry(self)
        self.fileOutput.place(x = 200, y = 250, w = 200)

        self.calculate2 = tk.Button(self, text = "Calculate", 
        command =  lambda: self._calculate_csv_output(), 
        padx = 10,
        pady = 10)
        self.calculate2.place(x = 200, y = 300, width = 125, height = 35)

        self.visualize = tk.Button(self, text = "Visualization", 
        command =  lambda: self._calculate_csv_output(), 
        padx = 10,
        pady = 10)
        self.visualize.place(x = 200, y = 350, width = 125, height = 35)

    def open_file(self):
        filename = tkfd.askopenfilename(filetypes =[('CSV Files', '*.csv')])
        if filename != () and filename != "":
            self.fileInput.delete(0, tk.END)
            self.fileInput.insert(0, filename)

    def _calculate_csv_output(self):
        inputFilename = self.fileInput.get()
        outputFilename = self.fileOutput.get()
        if inputFilename == "" or outputFilename == "":
            self.csv_text.set("ERROR!! Plz Enter Both Fields !!RORRE")
        else:
            findWQI(inputFilename, outputFilename)
