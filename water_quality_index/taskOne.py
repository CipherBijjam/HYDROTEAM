import tkinter as tk
import tkinter.filedialog as tkfd
import pandas as pd

from selectPage import SelectPage
from vars import Vars


class TaskOne(SelectPage):

    def __init__(self, parent, controller):
        self.pH = "pH"
        self.temp = "Tempurature"
        self.wind = "Turbidity"
        self.tdv = "Total Dissolved Values"
        self.ns = "Nitrates"
        self.fc = "Fecal Coliform"
        
        self.words = [self.pH, self.wind, self.temp, self.tdv, self.ns, self.fc]

        self.weights = {
            self.pH: 0.11,
            self.temp: 0.10,
            self.wind: 0.08,
            self.tdv: 0.07,
            self.ns: 0.10,
            self.fc: 0.16
        }
        
        self.textFields = {}
        self.labelFields = {}

        self.cal_value = tk.StringVar()
        self.cal_value.set("Not Calculated")



        SelectPage.__init__(self, parent, controller)
        # self.initUI(parent, controller)

    # def initUI(self, parent, controller):

        for idx, i in enumerate(self.words):
            self.labelFields[i] = tk.Label(self, text = i, font = Vars.LABEL_FONT)
            self.textFields[i] = tk.Entry(self, validate='key', 
                                                vcmd=(controller.register(self.validate_float), '%P'))
            self.labelFields[i].place(x = 200, y = 50 + (50 * idx))
            self.textFields[i].place(x = 450, y = 50 + (50 * idx))

        self.calculate = tk.Button(self, text = "Calculate", 
        command =  lambda: self._calculate_wqi(), 
        padx = 10,
        pady = 10)
        self.calculate.place(x = 350, y = 350, width = 125, height = 35)

        self.curr_value = tk.Label(self, textvariable = self.cal_value, font = Vars.LABEL_FONT)
        self.curr_value.place(x = 500, y = 350)

        # CSV File
        self.csv_text = tk.StringVar()
        self.csv_text.set("CSV File Upload")
        self.csv_label = tk.Label(self, textvariable = self.csv_text, font = Vars.LABEL_FONT)
        self.csv_label.place(x = 200, y = 450)

        self.fileInput = tk.Entry(self)
        self.fileInput.place(x = 200, y = 500, w = 200)

        self.chooseFile = tk.Button(self, text = "Input File", 
        command =  lambda: self.open_file(), 
        padx = 10,
        pady = 10)
        self.chooseFile.place(x = 450, y = 500, width = 125, height = 35)

        self.fileOutput = tk.Entry(self)
        self.fileOutput.place(x = 200, y = 550, w = 200)

        self.calculate2 = tk.Button(self, text = "Calculate", 
        command =  lambda: self._calculate_csv_output(), 
        padx = 10,
        pady = 10)
        self.calculate2.place(x = 450, y = 550, width = 125, height = 35)


    def _calculate_csv_output(self):
        inputFilename = self.fileInput.get()
        outputFilename = self.fileOutput.get()
        if inputFilename == "" or outputFilename == "":
            self.csv_text.set("ERROR!! Plz Enter Both Fields !!RORRE")
        else:
            df = pd.read_csv(inputFilename)
            values = []
            for i in range(0, len(df)):
                sum, deno = 0, 0
                for word in self.words:
                    sum += (df[word][i] * self.weights[word])
                    deno += self.weights[word]
                sum = sum /deno
                values.append(sum)       
            df['WQI'] = values
            df.to_csv(outputFilename, index = False)
            self.csv_text.set("DONE")
            self.fileInput.delete(0, tk.END)
            self.fileOutput.delete(0, tk.END)

     

    def open_file(self):
        filename = tkfd.askopenfilename(filetypes =[('CSV Files', '*.csv')])
        if filename != () and filename != "":
            self.fileInput.delete(0, tk.END)
            self.fileInput.insert(0, filename)
        

    def validate_float(self, inp, empty = 0):
        try:
            if inp != "" or empty:
                float(inp)
        except:
            return False
        return True


    def _calculate_wqi(self):
        validate = True
        for i in self.words:
            validate = validate and self.validate_float(self.textFields[i].get(), 1)
        
        sum = 0
        if validate:
            for i in self.words:
                sum += (self.weights[i] * float(self.textFields[i].get()))
            self.cal_value.set(sum)
        else:
            self.cal_value.set("Enter all Inputs")
