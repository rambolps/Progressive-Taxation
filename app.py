import graph as G
import TaxCalculator as TC

from Canada import FederalIncome as FI
from Canada import OntarioIncome as OI

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
    
    ftax = round(TC.calculate(income,FI.f1,FI.f2,FI.f3,FI.f4,FI.f5),2)
    ptax = round(TC.calculate(income,OI.o1,OI.o2,OI.o3,OI.o4,OI.o5),2)

    tax = ftax+ptax

    print("You owe $"+str(tax)+" in taxes!")

    G.fvp(ftax,ptax,"Canada","Ontario",tax)



main() 

