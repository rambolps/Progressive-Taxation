def calcIncome(amount, r):
        tax = 0
        amount = int(amount)

        for x in r:

            if x[0] == -1:
                tax += amount*x[1]
                break 
            
            if amount >= x[0]:
                tax += (x[0]*x[1])
                amount -= x[0]
            else:
                tax += amount*x[1]
                break 
        
        return tax
