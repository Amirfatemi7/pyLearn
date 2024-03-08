
class Time:
    def __init__(self,h,m,s):
        self.sec = s
        self.min = m
        self.hour = h
        self.unixTimeStamp = None
        self.fix()
        self.show()

    def show(self):
        print(self.hour, ':', self.min, ':', self.sec)

    def sum(self,t):
        s_new = self.sec + t.sec
        m_new = self.min + t.min
        h_new = self.hour + t.hour
       
        result = Time(h_new, m_new, s_new)
        result.fix()
        return result
    
    def sub(self,t):
        s_new = self.sec - t.sec
        m_new = self.min - t.min
        h_new = self.hour - t.hour
        
        result = Time(h_new, m_new, s_new)
        result.fix()
        return result
    
    def fix(self):
        while self.sec >= 60:
            self.sec -= 60
            self.min += 1
        while self.min >= 60:
            self.min -= 60
            self.hour += 1
        while self.sec < 0:
            self.sec += 60
            self.min -= 1
        while self.min < 0:
            self.min += 60
            self.hour -= 1 
        
    def get_unixTime(self):
        self.unixTimeStamp = self.sec + self.min * 60 + self.hour * 3600
        return self.unixTimeStamp
    
    def set_unixTime(self,t):
        self.unixTimeStamp = t
        self.sec = t
        self.fix()
        self.show()

    def convert_to_timeZone(self,t):
        x = self.sum(t)
        return x
        
        
        
t1 = Time(1,1,1)

print(t1.get_unixTime())

t1.set_unixTime(5000)

t2 = t1.sum(t1)

t3 = t2.sub(t1)

tehran_zone =Time(3,30,0)
t4 = t3.convert_to_timeZone(tehran_zone)