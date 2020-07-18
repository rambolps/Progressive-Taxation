import graph as g
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
    
    ftax = round(C.FederalIncome.fcalculate(C.FederalIncome,income),2)
    ptax = round(C.OntarioIncome.ocalculate(C.OntarioIncome,income),2)

    tax = ftax+ptax

    print("You owe $"+str(tax)+" in taxes!")

    g.fvp(ftax,ptax,"Canada","Ontario",tax)



main() 

