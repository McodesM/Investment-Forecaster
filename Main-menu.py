from tkinter import *
from tkinter.ttk import *
from Foreign_Exchange_back_tester import backtester
from Foreign_Exchange_prediction_software import Forex_Pred
from CryptoGauger import CryptoGauge

def main():
    window = Tk()
    window.title("Forex Pred software")
    window.geometry("450x200")
    lbl = Label(window, text = "Investment Forecaster", font = ("Century Gothic", 10))
    lbl.pack()
    lbl.place(x = 150, y = 0)
    btn1 = Button(window, text = "Forex Forecaster", command = Forex_Pred, style = "TButton")
    btn1.pack()
    btn1.place(x = 173 , y = 30)

    btn2 = Button(window, text = "Forex Back Tester", command = backtester, style = "TButton")
    btn2.pack()
    btn2.place(x = 173 , y = 70)
    style = Style()

    btn3 = Button(window, text = "Crypto Currency Gauger", command = CryptoGauge, style = "TButton")
    btn3.pack()
    btn3.place(x = 155 , y = 110)
    style = Style()
    style.configure("TButton",foreground = "black", background = "blue")
    window.mainloop()
main()