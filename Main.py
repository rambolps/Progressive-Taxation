#Import self-made resources
import Graph as G
import TaxCalculator as TC
import Canada as C

#import tkinter and ttkthemes for GUI
import tkinter as tk
import tkinter.ttk as ttk 
from ttkthemes import ThemedStyle

#create tkinter window
app = tk.Tk()
app.geometry("500x500")
app.title("Progressive Taxation")

#select the ttk style
style = ThemedStyle(app)
style.set_theme("breeze")

Themed_Btn = ttk.Button(app,text='Themed button')
Themed_Btn.pack()

Themed_Scrollbar = ttk.Scrollbar(app,orient='vertical')
Themed_Scrollbar.pack(side='right',fill='y')

Themed_Entry = ttk.Entry(app)
Themed_Entry.pack()

#create app main loop (goes on forever, unless interuppted)
app.mainloop()

income = 0
ftax = 0
ptax = 0
tax = 0

def getAmount():
    x = input("Please enter the amount of income you made: $")
    return x
    
def main():
    print("Welcome to the Progressive Tax Calculator\n")
    
    income = getAmount()
    
    ftax = TC.calcIncome(income,C.Federal.income)
    ptax = TC.calcIncome(income,C.Ontario.income)

    tax = round(ftax+ptax,2)

    print("You owe $"+str(tax)+" in taxes!")

    G.fvp(ftax,ptax,"Canada","Ontario",tax)



main() 

