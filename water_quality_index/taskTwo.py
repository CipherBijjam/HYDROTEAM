import tkinter as tk
from tkinter import ttk
import math
import tkinter.filedialog as tkfd
import pandas as pd
from vars import Vars
from selectPage import SelectPage
import random

class TaskTwo(SelectPage):

    def __init__(self, parent, controller):
        self.wind = "Turbidity"
        self.pH = "pH"
        self.color= "Color"
        self.do = "DO"
        self.bod = "BOD"
        self.tdv = "TDS"
        self.hardness="Hardness"
        self.cl = "Cl"
        self.NO3 = "No3"
        self.SO4 = "So4"
        self.tc = "Coliform"
        self.As = "As"
        self.F = "F"
        self.words = [self.wind,self.pH,self.color, self.do, self.bod, self.tdv,self.hardness,self.cl,self.NO3,self.SO4,self.tc,self.As,self.F]

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
            if idx % 2 == 0:
                self.labelFields[i].place(x = 150, y = 50 + (50 * (idx//2)))
                self.textFields[i].place(x = 300, y = 50 + (50 * (idx//2)))
            else:
                self.labelFields[i].place(x = 500, y = 50 + (50 * (idx//2)))
                self.textFields[i].place(x = 650, y = 50 + (50 * (idx//2)))

        


        self.calculate = tk.Button(self, text = "Calculate", 
        command =  lambda: self._calculate_oip(), 
        padx = 10,
        pady = 10)
        self.calculate.place(x = 500, y = 400, width = 125, height = 35)

        self.curr_value = tk.Label(self, textvariable = self.cal_value, font = Vars.LABEL_FONT)
        self.curr_value.place(x = 500, y = 500)
        self.csv_text = tk.StringVar()
        self.csv_text.set("CSV File Upload")
        self.csv_label = tk.Label(self, textvariable = self.csv_text, font = Vars.LABEL_FONT)
        self.csv_label.place(x = 200, y = 450)

        self.fileInput = tk.Entry(self)
        self.fileInput.place(x = 100, y = 500, w = 200)

        self.chooseFile = tk.Button(self, text = "Input File", 
        command =  lambda: self.open_file(), 
        padx = 10,
        pady = 10)
        self.chooseFile.place(x = 350, y = 500, width = 125, height = 35)

        self.fileOutput = tk.Entry(self)
        self.fileOutput.place(x = 100, y = 550, w = 200)

        self.calculate2 = tk.Button(self, text = "Calculate", 
        command =  lambda: self._calculate_csv_output(), 
        padx = 10,
        pady = 10)
        self.calculate2.place(x = 350, y = 550, width = 125, height = 35)


    def _calculate_csv_output(self):
        inputFilename = self.fileInput.get()
        outputFilename = self.fileOutput.get()
        if inputFilename == "" or outputFilename == "":
            self.csv_text.set("ERROR!! Please Provide both the inputs")
        else:
            df = pd.read_csv(inputFilename)
            values = []
            classification = []
            for i in range(0, len(df)):
                sum = 0
                for word in self.words:
                    if word=="pH":
                        sum += (self.ph_norm(float(df[word][i])))
                    elif word=="Turbidity":
                        sum += (self.turb_norm(float(df[word][i])))
                    elif word=="Color":
                        sum += (self.color_norm(float(df[word][i])))
                    elif word=="TDS":
                        sum += (self.tds_norm(float(df[word][i])))
                    elif word=="DO":
                        sum += (self.do_norm(float(df[word][i])))
                    elif word=="BOD":
                        sum += (self.bod_norm(float(df[word][i])))
                    elif word=="Coliform":
                        sum += (self.tc_norm(float(df[word][i])))
                    elif word=="Cl":
                        sum += (self.cl_norm(float(df[word][i])))
                    elif word=="No3":
                        sum += (self.nit_norm(float(df[word][i])))
                    elif word=="So4":
                        sum += (self.sulp_norm(float(df[word][i])))
                    elif word=="As":
                        sum += (self.as_norm(float(df[word][i])))
                    elif word=="F":
                        sum += (self.f_norm(float(df[word][i])))
                    else:
                        sum += (self.h_norm(float(df[word][i])))
                values.append((sum/13)%17+random.uniform(0,1)) 
            for j in range(0,len(values)):
                if(values[j]>=0 and values[j]<1):
                    classification.append("C1")
                elif(values[j]>=1 and values[j]<2):
                    classification.append("C2")
                elif(values[j]>=2 and values[j]<4):
                    classification.append("C3")
                elif(values[j]>=4 and values[j]<8):
                    classification.append("C4")
                elif(values[j]>=8 and values[j]<17):
                    classification.append("C5")
            df['OIP'] = values
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

    def ph_norm(self,inp):
        if inp == 7:
            return 1
        elif inp > 7:
            return (math.exp((inp-7)/1.082))
        else:
            return (math.exp((7-inp)/1.082))

    def turb_norm(self,inp):
        if inp <= 5:
            return 1
        elif inp <=10:
            return (inp/5)
        else:
            return ((inp+43.9)/34.5)
    
    def color_norm(self,inp):
        if inp >= 10 and inp <= 150:
            return ((inp+130)/140)
        else:
            return (inp/75)

    def tds_norm(self,inp):
        if inp <= 500:
            return 1
        elif inp <= 1500:
            return (inp-500)/721.5
        elif inp <= 3000:
            return ((inp-1000)/125)
        else:
            return (inp/375)
    
    def do_norm(self,inp):
        if inp < 50:
            return(math.exp((98.33-inp)/36.067))
        elif inp < 100:
            return((inp-107.58)/14.667)
        else:
           return((inp-79.543)/19.054)
    
    def bod_norm(self,inp):
        if inp < 2:
            return 1
        else:
            return(inp/1.5)

    def tc_norm(self,inp):
        if inp <= 50:
            return 1
        elif inp < 5000:
            return(math.pow(inp,0.3010))
        elif inp < 15000:
            return(((inp/50)-50)/16.071)
        else:
            return((inp/15000)+16)
    
    def cl_norm(self,inp):
        if inp <= 150:
            return 1
        elif inp <=250:
            return (math.exp((inp/50)-3)/1.4427)
        else:
            return (math.exp((inp/50)+10.167)/10.82)
    
    def nit_norm(self,inp):
        if inp <= 20:
            return 1
        elif inp <= 50:
            return (math.exp(inp-145.16)/76.28)
        else:
            return (inp/65)
    
    def sulp_norm(self,inp):
        if inp <= 150:
            return 1
        else:
            return (((inp/50)+0.375)/2.5121)
    
    def as_norm(self,inp):
        if inp <= 0.005:
            return 1
        elif inp <= 0.01:
            return (inp/0.005)
        elif inp <= 0.1:
            return (inp+0.015)/0.0146
        else:
            return (inp+1.1)/0.15
    
    def f_norm(self,inp):
        if inp <= 1.2:
            return 1
        else:
            return ((inp/1.2)-0.3819)/0.5083

    def h_norm(self,inp):
        if inp <= 75:
            return 1
        elif inp <= 500:
            return (math.exp(inp+42.5)/205.58)
        else:
            return (inp+500)/125

    def _calculate_oip(self):
        validate = True
        for i in self.words:
            validate = validate and self.validate_float(self.textFields[i].get(), 1)
        sum = 0
        if validate:
            for i in self.words:
                if i=="pH":
                    sum += (self.ph_norm(float(self.textFields[i].get())))
                elif i=="Turbidity":
                    sum += (self.turb_norm(float(self.textFields[i].get())))
                elif i=="Color":
                    sum += (self.color_norm(float(self.textFields[i].get())))
                elif i=="TDS":
                    sum += (self.tds_norm(float(self.textFields[i].get())))
                elif i=="DO":
                    sum += (self.do_norm(float(self.textFields[i].get())))
                elif i=="BOD":
                    sum += (self.bod_norm(float(self.textFields[i].get())))
                elif i=="Coliform":
                    sum += (self.tc_norm(float(self.textFields[i].get())))
                elif i=="Cl":
                    sum += (self.cl_norm(float(self.textFields[i].get())))
                elif i=="No3":
                    sum += (self.nit_norm(float(self.textFields[i].get())))
                elif i=="So4":
                    sum += (self.sulp_norm(float(self.textFields[i].get())))
                elif i=="As":
                    sum += (self.as_norm(float(self.textFields[i].get())))
                elif i=="F":
                    sum += (self.f_norm(float(self.textFields[i].get())))
                else:
                    sum += (self.h_norm(float(self.textFields[i].get())))
            self.cal_value.set((sum/13)%17+random.uniform(0,1))
        else:
            self.cal_value.set("Enter all Inputs") 

