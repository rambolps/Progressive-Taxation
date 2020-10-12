#Import self-made resources
import Graph as G
import TaxCalculator as TC
import Canada as C

#import tkinter and ttkthemes for GUI
from tkinter import IntVar, StringVar
import tkinter as tk
import tkinter.ttk as ttk 
from ttkthemes import ThemedStyle


#Calculate Taxes
def calcTotalIn(income,prov):
    
    ftax = 0
    ptax = 0
    tax = 0

    ftax = TC.calcIncome(income,C.Federal.income)

    provSwitch = {
        "Ontario": TC.calcIncome(income,C.Ontario.income),
        "Nova Scotia": TC.calcIncome(income,C.NovaSoctia.income),
        "Newfoundland and Labrador": TC.calcIncome(income,C.NewfoundlandAndLabrador.income),
        "Prince Edward Island": TC.calcIncome(income,C.PrinceEdwardIsland.income),
        "New Brunswick": TC.calcIncome(income,C.NewBrunswick.income),
        "Manitoba": TC.calcIncome(income,C.Manitoba.income),
        "Saskatchewan": TC.calcIncome(income,C.Saskatchewan.income),
        "Alberta": TC.calcIncome(income,C.Alberta.income),
        "British Columbia": TC.calcIncome(income,C.BritishColumbia.income),
        "Yukon": TC.calcIncome(income,C.Yukon.income),
        "Northwest Territories": TC.calcIncome(income,C.NorthwestTerritories.income),
        "Nunavut": TC.calcIncome(income,C.Nunavut.income)  
    }

    ptax = provSwitch.get(prov)

    tax = round(ftax+ptax,2)

    print("You owe $"+str(tax)+" in taxes!")

    G.fvp(ftax,ptax,"Canada",prov,tax) 

#create tkinter window
app = tk.Tk()
app.geometry("500x500")
app.title("Progressive Taxation")
app.iconbitmap("tax.ico")



#select the ttk style
style = ThemedStyle(app)
style.set_theme("breeze")

country = StringVar()
countryDrop =  ttk.OptionMenu(app, country, "Canada").pack()

province = StringVar()
provinceDrop =  ttk.OptionMenu(app, province, C.provinces[0], *C.provinces).pack()

income = StringVar()
income.set("Please Enter Income ($)")
incomeEntry = ttk.Entry(app, textvariable=income).pack()

def proxyIn():
    floatIn = float(income.get())
    calcTotalIn(floatIn,province.get())

calc = ttk.Button(app,text='Calculate', command = proxyIn)
calc.pack()


#create app main loop (goes on forever, unless interuppted)
app.mainloop()




