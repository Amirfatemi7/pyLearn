
class kasr:
#propertice
    def __init__(self):
        self.sorat = None
        self.makhraj = None
  
#methods
    def set_sorat(self,s):
        self.sorat = s
    
    def set_makhraj(self,m):
        self.makhraj = m

    def get_sorat(self):
        return self.sorat

    def get_makhraj(self):
        return self.makhraj
    
    def get_kasr(self):
        return str(self.sorat)+'/'+str(self.makhraj)+'='+ str(self.sorat/self.makhraj)


k = kasr()

k.set_sorat(2)
k.set_makhraj(4)

print(k.get_kasr())