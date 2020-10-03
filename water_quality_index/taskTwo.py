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
        self.cl = "Chlorine"
        self.NO3 = "Nitrite"
        self.SO4 = "Sulphate"
        self.As = "Arsenic"
        self.F = "Flouride"
        self.hardness="Hardness"
        self.words = [self.pH, self.wind, self.color, self.tdv, self.do, self.bod,self.tc,self.cl,self.NO3,self.SO4,self.As,self.F,self.hardness]

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
        self.calculate.place(x = 350, y = 500, width = 125, height = 35)

        self.curr_value = tk.Label(self, textvariable = self.cal_value, font = Vars.LABEL_FONT)
        self.curr_value.place(x = 500, y = 500)

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
    
    def cl_norm(self,inp):
        if inp <= 150:
            return 1
        elif inp <=250:
            return (math.exp(((inp/50)-3)/1.4427))
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
            return (math.exp((inp/50)+0.375)/2.5121)
    
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
                elif i=="Total Coliform":
                    sum += (self.tc_norm(float(self.textFields[i].get())))
                elif i=="Chlorine":
                    sum += (self.cl_norm(float(self.textFields[i].get())))
                elif i=="Nitrite":
                    sum += (self.nit_norm(float(self.textFields[i].get())))
                elif i=="Sulphate":
                    sum += (self.sulp_norm(float(self.textFields[i].get())))
                elif i=="Arsenic":
                    sum += (self.as_norm(float(self.textFields[i].get())))
                elif i=="Flouride":
                    sum += (self.f_norm(float(self.textFields[i].get())))
                else:
                    sum += (self.h_norm(float(self.textFields[i].get())))
            self.cal_value.set(sum/13)
        else:
            self.cal_value.set("Enter all Inputs") 
