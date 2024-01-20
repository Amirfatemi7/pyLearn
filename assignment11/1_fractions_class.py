

class Fraction:
    def __init__(self,s,m):
        self.s = s
        self.m = m

    def sum(self, f2):
        s = self.s * f2.m + self.m * f2.s
        m = self.m * f2.m
        x = Fraction(s,m)
        return x
    
    def mul(self, f2):
        s = self.s * f2.s
        m = self.m * f2.m
        x = Fraction(s,m)
        return x
    
    def sub(self, f2):
        s = self.s * f2.m - self.m * f2.s
        m = self.m * f2.m
        x = Fraction(s,m)
        return x

    def div(self, f2):
        s = self.s * f2.m
        m = self.m * f2.s
        x = Fraction(s,m)
        return x
    
    def fraction_to_number(self):
        return self.s / self.m


    def simplifying(self):
        for i in range(1,self.m+1):
            if self.s % i == 0 and self.m % i == 0:
                bmm = i
        self.s = self.s/bmm
        self.m = self.m/bmm
        self.show()
    
    def show(self):
        print(self.s, '/', self.m)



k1 = Fraction(5, 10)
k1.show()
k2 = Fraction(9,3)
k2.show()
x = k1.sum(k2)
x.show()
k1.simplifying()