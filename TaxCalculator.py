def calculate(amount, r1, r2, r3, r4, r5):
        tax = 0
        amount = int(amount)

        if amount <= r1[0]:
            tax += amount*r1[1]
            return tax
        elif amount <= (r1[0]+r2[0]):
            tax += r1[0]*r1[1]
            amount -= r1[0]
            tax += amount*r2[1]
            return tax
        elif amount <= (r1[0]+r2[0]+r3[0]):
            tax += r1[0]*r1[1]
            tax += r2[0]*r2[1]
            amount -= (r1[0]+r2[0])
            tax += amount*r3[1]
            return tax
        elif amount <= (r1[0]+r2[0]+r3[0]+r4[0]):
            tax += r1[0]*r1[1]
            tax += r2[0]*r2[1]
            tax += r3[0]*r3[1]
            amount -= (r1[0]+r2[0]+r3[0])
            tax += amount*r4[1]
            return tax
        elif amount > (r1[0]+r2[0]+r3[0]+r4[0]):
            tax += r1[0]*r1[1]
            tax += r2[0]*r2[1]
            tax += r3[0]*r3[1]
            tax += r4[0]*r4[1]
            amount -= (r1[0]+r2[0]+r3[0]+r4[0])
            tax += amount*r5[1]
            return tax
        else:
            return -1                
        