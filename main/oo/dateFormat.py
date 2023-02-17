#This class gets a USA format date(mm-dd-yyyy) and convert it to brazilian date format (dd/mm/yyyy) 

class DateFormat:
    def __init__(self, date):
        self.__date = date
        self.__formatDate = ''
    
    @staticmethod
    def format(self):
        self.formatDate = self.date.replace('-', '/')
        self.formatDate = self.formatDate[3:6]+self.formatDate[0:3]+self.formatDate[6:]
        print(self.formatDate)


