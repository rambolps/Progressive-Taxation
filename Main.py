import Graph as G
import TaxCalculator as TC
import Canada as C

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

