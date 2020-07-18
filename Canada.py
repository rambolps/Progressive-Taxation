class Canada():
    class FederalIncome():
        f1 = [48535,0.15]
        f2 = [48534,0.205]
        f3 = [53404,0.26]
        f4 = [63895,0.29]
        f5 = [-1,0.33]

        def fcalculate(self,amount):
            tax = 0

            if amount <= f1[0]:
                tax += amount*f1[1]
                return tax
            elif amount <= (f1[0]+f2[0]):
                tax += f1[0]*f1[1]
                amount -= f1[0]
                tax += amount*f2[1]
                return tax
            elif amount <= (f1[0]+f2[0]+f3[0]):
                tax += f1[0]*f1[1]
                tax += f2[0]*f2[1]
                amount -= (f1[0]+f2[0])
                tax += amount*f3[1]
                return tax
            elif amount <= (f1[0]+f2[0]+f3[0]+f4[0]):
                tax += f1[0]*f1[1]
                tax += f2[0]*f2[1]
                tax += f3[0]*f3[1]
                amount -= (f1[0]+f2[0]+f3[0])
                tax += amount*f4[1]
                return tax
            elif amount > (f1[0]+f2[0]+f3[0]+f4[0]):
                tax += f1[0]*f1[1]
                tax += f2[0]*f2[1]
                tax += f3[0]*f3[1]
                tax += f4[0]*f4[1]
                amount -= (f1[0]+f2[0]+f3[0]+f4[0])
                tax += amount*f5[1]
                return tax
            else:
                return -1                
            

                

    class OntarioIncome():
        o1 = [44740,0.0505]
        o2 = [44742,0.0915]
        o3 = [60518,0.1116]
        o4 = [70000,0.1216]
        o5 = [-1,0.1316]
        
        def ocalculate(self,amount):
            tax = 0

            if amount <= o1[0]:
                tax += amount*o1[1]
                return tax
            elif amount <= (o1[0]+o2[0]):
                tax += o1[0]*o1[1]
                amount -= o1[0]
                tax += amount*o2[1]
                return tax
            elif amount <= (o1[0]+o2[0]+o3[0]):
                tax += o1[0]*o1[1]
                tax += o2[0]*o2[1]
                amount -= (o1[0]+o2[0])
                tax += amount*o3[1]
                return tax
            elif amount <= (o1[0]+o2[0]+o3[0]+o4[0]):
                tax += o1[0]*o1[1]
                tax += o2[0]*o2[1]
                tax += o3[0]*o3[1]
                amount -= (o1[0]+o2[0]+o3[0])
                tax += amount*o4[1]
                return tax
            elif amount > (o1[0]+o2[0]+o3[0]+o4[0]):
                tax += o1[0]*o1[1]
                tax += o2[0]*o2[1]
                tax += o3[0]*o3[1]
                tax += o4[0]*o4[1]
                amount -= (o1[0]+o2[0]+o3[0]+o4[0])
                tax += amount*o5[1]
                return tax
            else:
                return -1

