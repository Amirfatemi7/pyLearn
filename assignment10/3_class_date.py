import datetime
class myDate:
#propertice
    def __init__(self,y,mo,d):
        self.day = d
        self.month = mo
        self.year = y
        self.unixDateTimeStamp = None
#methods
    def change_day(self,d):
        self.second = d
    
    def change_month(self,mo):
        self.month = mo

    def change_year(self,y):
        self.year = y

    def get_day(self):
        return self.day
    
    def get_month(self):
        return self.month 

    def get_year(self):
        return self.year 

    def get_unixDate(self):
        return self.unixDateTimeStamp
    
    def set_unixDate(self,d):
        self.unixDateTimeStamp = d
    
    def unixDate_to_date(self):
        d = datetime.datetime.fromtimestamp(self.unixDateTimeStamp)
        self.day = datetime.datetime.day
        self.month = datetime.datetime.month
        self.year = datetime.datetime.year

