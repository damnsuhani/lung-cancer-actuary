import tkinter as tk
import tkinter.font as tkFont
import pandas as pd

from tkinter import messagebox

data = pd.read_csv('prob.csv')

class App:

    def tkinter_input(self):
        name = self.GLineEdit_117.get()
        age = int(self.GLineEdit_274.get())
        sex = self.GLineEdit_517.get().capitalize()
        smoking = self.GLineEdit_743.get().capitalize()
        fatigue = self.GLineEdit_14.get().capitalize()
        cough = self.GLineEdit_960.get().capitalize()
        anxiety = self.GLineEdit_917.get().capitalize()
        swallow = self.GLineEdit_590.get().capitalize()
        chronic = self.GLineEdit_540.get().capitalize()

        try:
            self.process(name, age, sex, smoking, fatigue, cough, anxiety, swallow, chronic)

        except:
            tk.messagebox.showinfo("message", "Please enter correct values!")

    def process(self, name, age, sex, smoking, fatigue, cough, anxiety, swallow, chronic):
        a = 1
        v = (1 / 1.06)
        g = 0
        total = 1000000
        w = self.loading_calc(smoking, fatigue, cough, anxiety, chronic, swallow)
        output_string = ""
        print("Name:", name)
        print("Age:", age)
        print("Sex:", sex)
        for i in range(age, 45):
            row = data.loc[data['Age'] == i]
            if (sex == 'M'):
                p = row['mp'].values[0]
            if (sex == 'F'):
                p = row['fp'].values[0]
            rawpremium = ((v ** (a)) * (total) * w * p)
            rawpremium2 = rawpremium
            rawpremium3 = rawpremium2 * 1.20
            rawpremium4 = rawpremium3 * 1.04
            finalpremium = rawpremium4 * 1.18
            g = g + finalpremium
            output_string += 'Premium for year' + str(a) + 'is Rs.' + str(finalpremium) + "\n"
            a = a + 1
        g = int(g)
        output_string += 'Total premium payable is Rs.' + str(g) + "\n"

        tk.messagebox.showinfo("Output", output_string)

    def loading_calc(self, smoking, fatigue, cough, anxiety, chronic, swallow):
        ws = 0.2
        wf = 0.15
        wc = 0.1
        wa = 0.08
        wcd = 0.07
        wsd = 0.02
        w = 1
        if (smoking == 'Y'):
            w = w + ws
        if (fatigue == 'Y'):
            w = w + wf
        if (cough == 'Y'):
            w = w + wc
        if (anxiety == 'Y'):
            w = w + wa
        if (chronic == 'Y'):
            w = w + wcd
        if (swallow == 'Y'):
            w = w + wsd
        return w

    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_9 = tk.Button(root)
        GButton_9["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_9["font"] = ft
        GButton_9["fg"] = "#000000"
        GButton_9["justify"] = "center"
        GButton_9["text"] = "Submit"
        GButton_9.place(x=410,y=410,width=70,height=25)
        GButton_9["command"] = self.tkinter_input

        GLabel_443=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_443["font"] = ft
        GLabel_443["fg"] = "#333333"
        GLabel_443["justify"] = "center"
        GLabel_443["text"] = "Name"
        GLabel_443.place(x=70,y=30,width=70,height=25)

        self.GLineEdit_117=tk.Entry(root)
        self.GLineEdit_117["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_117["font"] = ft
        self.GLineEdit_117["fg"] = "#333333"
        self.GLineEdit_117["justify"] = "left"
        self.GLineEdit_117.place(x=90,y=50,width=166,height=30)

        GLabel_188=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_188["font"] = ft
        GLabel_188["fg"] = "#333333"
        GLabel_188["justify"] = "center"
        GLabel_188["text"] = "Age"
        GLabel_188.place(x=70,y=90,width=70,height=25)

        self.GLineEdit_274=tk.Entry(root)
        self.GLineEdit_274["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_274["font"] = ft
        self.GLineEdit_274["fg"] = "#333333"
        self.GLineEdit_274["justify"] = "center"
        self.GLineEdit_274.place(x=90,y=120,width=70,height=25)

        GLabel_729=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_729["font"] = ft
        GLabel_729["fg"] = "#333333"
        GLabel_729["justify"] = "center"
        GLabel_729["text"] = "Sex"
        GLabel_729.place(x=70,y=160,width=70,height=25)

        self.GLineEdit_517=tk.Entry(root)
        self.GLineEdit_517["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_517["font"] = ft
        self.GLineEdit_517["fg"] = "#333333"
        self.GLineEdit_517["justify"] = "center"
        self.GLineEdit_517.place(x=90,y=190,width=70,height=25)

        GLabel_649=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_649["font"] = ft
        GLabel_649["fg"] = "#333333"
        GLabel_649["justify"] = "center"
        GLabel_649["text"] = "Do you smoke? (Y/N)"
        GLabel_649.place(x=80,y=230,width=145,height=30)

        self.GLineEdit_743=tk.Entry(root)
        self.GLineEdit_743["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_743["font"] = ft
        self.GLineEdit_743["fg"] = "#333333"
        self.GLineEdit_743["justify"] = "center"
        self.GLineEdit_743.place(x=90,y=260,width=70,height=25)

        GLabel_515=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_515["font"] = ft
        GLabel_515["fg"] = "#333333"
        GLabel_515["justify"] = "center"
        GLabel_515["text"] = "Do you feel fatigue? (Y/N)"
        GLabel_515.place(x=70,y=290,width=185,height=30)

        self.GLineEdit_14=tk.Entry(root)
        self.GLineEdit_14["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_14["font"] = ft
        self.GLineEdit_14["fg"] = "#333333"
        self.GLineEdit_14["justify"] = "center"
        self.GLineEdit_14.place(x=90,y=320,width=70,height=25)

        GLabel_468=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_468["font"] = ft
        GLabel_468["fg"] = "#333333"
        GLabel_468["justify"] = "center"
        GLabel_468["text"] = "Have you had cough in the past month? (Y/N)"
        GLabel_468.place(x=310,y=150,width=198,height=30)

        self.GLineEdit_960=tk.Entry(root)
        self.GLineEdit_960["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_960["font"] = ft
        self.GLineEdit_960["fg"] = "#333333"
        self.GLineEdit_960["justify"] = "center"
        self.GLineEdit_960.place(x=310,y=190,width=70,height=25)

        GLabel_75=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_75["font"] = ft
        GLabel_75["fg"] = "#333333"
        GLabel_75["justify"] = "center"
        GLabel_75["text"] = "Do you have anxiety? (Y/N)"
        GLabel_75.place(x=310,y=220,width=155,height=30)

        self.GLineEdit_917=tk.Entry(root)
        self.GLineEdit_917["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_917["font"] = ft
        self.GLineEdit_917["fg"] = "#333333"
        self.GLineEdit_917["justify"] = "center"
        self.GLineEdit_917.place(x=310,y=250,width=70,height=25)

        GLabel_202=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_202["font"] = ft
        GLabel_202["fg"] = "#333333"
        GLabel_202["justify"] = "center"
        GLabel_202["text"] = "Do you have swallowing difficulty? (Y/N)"
        GLabel_202.place(x=310,y=280,width=230,height=30)

        self.GLineEdit_590=tk.Entry(root)
        self.GLineEdit_590["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_590["font"] = ft
        self.GLineEdit_590["fg"] = "#333333"
        self.GLineEdit_590["justify"] = "center"
        self.GLineEdit_590.place(x=310,y=320,width=70,height=25)


        GLabel_820=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_820["font"] = ft
        GLabel_820["fg"] = "#333333"
        GLabel_820["justify"] = "center"
        GLabel_820["text"] = "Do you have a chronic disease? (Y/N)"
        GLabel_820.place(x=280,y=90,width=265,height=30)

        self.GLineEdit_540=tk.Entry(root)
        self.GLineEdit_540["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_540["font"] = ft
        self.GLineEdit_540["fg"] = "#333333"
        self.GLineEdit_540["justify"] = "center"
        self.GLineEdit_540["text"] = "Entry"
        self.GLineEdit_540.place(x=310,y=120,width=70,height=25)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
