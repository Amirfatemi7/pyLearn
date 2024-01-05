import datetime

class myTime:
#propertice
    def __init__(self,h,m,s):
        self.miliSecond = None
        self.second = s
        self.minutes = m
        self.hour = h
        self.unixTimeStamp = None
#methods
    def change_second(self,s):
        self.second = s
    
    def change_minute(self,m):
        self.minutes = m

    def change_hour(self,h):
        self.hour = h

    def get_second(self):
        return self.second 
    
    def get_minute(self):
        return self.minutes 

    def get_hour(self):
        return self.hour 

    def get_unixTime(self):
        return self.unixTimeStamp
    
    def set_unixTime(self,t):
        self.unixTimeStamp = t
    
    def unixTime_to_time(self):
        t = datetime.datetime.fromtimestamp(self.unixTimeStamp)
        self.second = datetime.datetime.second
        self.minute = datetime.datetime.minute
        self.hour = datetime.datetime.hour

