
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        self.show()
    
    def show(self):
        print(self.real, '+', self.img, 'i')

    def sum(self, c):
        new_r = self.real + c.real
        new_i = self.img + c.img
        return Complex(new_r, new_i)
    
    def sub(self, c):
        new_r = self.real - c.real
        new_i = self.img - c.img
        return Complex(new_r, new_i)
        
    def mul(self, c):
        new_r = self.real * c.real - self.img * c.img
        new_i = self.real * c.img + self.img * c.real
        return Complex(new_r, new_i)

c1 = Complex(2, 3)
c2 = Complex(4, 5)
c3 = c1.mul(c2)