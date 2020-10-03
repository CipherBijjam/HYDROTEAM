import tkinter as tk

from selectPage import SelectPage
from vars import Vars

class TaskTwo(SelectPage):

    def __init__(self, parent, controller):
        self.pH = "pH"
        self.wind = "Turbidity"
        self.color= "Color"
        self.tdv = "TDS"
        self.do = "DO"
        self.bod = "BOD"
        self.tc = "Total Coliform"

        self.words = [self.pH, self.wind, self.color, self.tdv, self.do, self.bod,self.tc]

        self.textFields = {}
        self.labelFields = {}

        self.cal_value = tk.StringVar()
        self.cal_value.set("Not Calculated")

        SelectPage.__init__(self, parent, controller)
 
        for idx, i in enumerate(self.words):
            self.labelFields[i] = tk.Label(self, text = i, font = LABEL_FONT)
            self.textFields[i] = tk.Entry(self, validate='key', 
                                                vcmd=(controller.register(self.validate_float), '%P'))
            self.labelFields[i].place(x = 50, y = 200 + (50 * idx))
            self.textFields[i].place(x = 50, y = 225 + (50 * idx))


        self.calculate = tk.Button(self, text = "Calculate", 
        command =  lambda: self._calculate_oip(), 
        padx = 10,
        pady = 10)
        self.calculate.place(x = 50, y = 550, width = 125, height = 35)

        self.curr_value = tk.Label(self, textvariable = self.cal_value, font = LABEL_FONT)
        self.curr_value.place(x = 400, y = 250)

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
            return (math.exp((inp)/1.082))
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
            return (inp-500)/721
        elif inp <= 3000:
            return ((inp-1000)/125)
        else:
            return (inp/375)
    
    def do_norm(self,inp):
        if inp < 50:
            return(math.exp(-(inp-98.33)/36.067))
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
        if inp < 50:
            return 1
        elif inp < 5000:
            return(math.pow(inp,0.3010))
        elif inp < 15000:
            return(((inp/50)-50)/16.071)
        else:
            return((inp/15000)+16)


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
                else:
                    sum += (self.tc_norm(float(self.textFields[i].get())))

            self.cal_value.set(sum/7)
        else:
            self.cal_value.set("Enter all Inputs")
