class FederalIncome():
    f1 = [48535,0.15]
    f2 = [48534,0.205]
    f3 = [53404,0.26]
    f4 = [63895,0.29]
    f5 = [-1,0.33]

    def fcalculate(self,amount):
        tax = 0
        amount = int(amount)

        if amount <= self.f1[0]:
            tax += amount*self.f1[1]
            return tax
        elif amount <= (self.f1[0]+self.f2[0]):
            tax += self.f1[0]*self.f1[1]
            amount -= self.f1[0]
            tax += amount*self.f2[1]
            return tax
        elif amount <= (self.f1[0]+self.f2[0]+self.f3[0]):
            tax += self.f1[0]*self.f1[1]
            tax += self.f2[0]*self.f2[1]
            amount -= (self.f1[0]+self.f2[0])
            tax += amount*self.f3[1]
            return tax
        elif amount <= (self.f1[0]+self.f2[0]+self.f3[0]+self.f4[0]):
            tax += self.f1[0]*self.f1[1]
            tax += self.f2[0]*self.f2[1]
            tax += self.f3[0]*self.f3[1]
            amount -= (self.f1[0]+self.f2[0]+self.f3[0])
            tax += amount*self.f4[1]
            return tax
        elif amount > (self.f1[0]+self.f2[0]+self.f3[0]+self.f4[0]):
            tax += self.f1[0]*self.f1[1]
            tax += self.f2[0]*self.f2[1]
            tax += self.f3[0]*self.f3[1]
            tax += self.f4[0]*self.f4[1]
            amount -= (self.f1[0]+self.f2[0]+self.f3[0]+self.f4[0])
            tax += amount*self.f5[1]
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
        amount = int(amount)
        
        if amount <= self.o1[0]:
            tax += amount*self.o1[1]
            return tax
        elif amount <= (self.o1[0]+self.o2[0]):
            tax += self.o1[0]*self.o1[1]
            amount -= self.o1[0]
            tax += amount*self.o2[1]
            return tax
        elif amount <= (self.o1[0]+self.o2[0]+self.o3[0]):
            tax += self.o1[0]*self.o1[1]
            tax += self.o2[0]*self.o2[1]
            amount -= (self.o1[0]+self.o2[0])
            tax += amount*self.o3[1]
            return tax
        elif amount <= (self.o1[0]+self.o2[0]+self.o3[0]+self.o4[0]):
            tax += self.o1[0]*self.o1[1]
            tax += self.o2[0]*self.o2[1]
            tax += self.o3[0]*self.o3[1]
            amount -= (self.o1[0]+self.o2[0]+self.o3[0])
            tax += amount*self.o4[1]
            return tax
        elif amount > (self.o1[0]+self.o2[0]+self.o3[0]+self.o4[0]):
            tax += self.o1[0]*self.o1[1]
            tax += self.o2[0]*self.o2[1]
            tax += self.o3[0]*self.o3[1]
            tax += self.o4[0]*self.o4[1]
            amount -= (self.o1[0]+self.o2[0]+self.o3[0]+self.o4[0])
            tax += amount*self.o5[1]
            return tax
        else:
            return -1