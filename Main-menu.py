from tkinter import *
from tkinter.ttk import *
from Foreign_Exchange_back_tester import  backtester
from Foreign_Exchange_prediction_software import Forex_Pred
class MainMenu:
    window = Tk()
    window.title("Forex Pred software")
    window.geometry("450x200")
    lbl = Label(window, text = "Investment Forecaster", font = ("Century Gothic", 10))
    lbl.pack()
    lbl.place(x = 170, y = 0)
    style = Style()
    style.configure("TButton",foreground = "black", background = "blue")
    btn1 = Button(window, text = "Prediction software", command = Forex_Pred, style = "TButton")
    btn1.pack()
    btn1.place(x = 0 , y = 140)
    window.mainloop()

MainMenu()