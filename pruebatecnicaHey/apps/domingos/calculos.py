from datetime import datetime, date
from dateutil.rrule import rrule, MONTHLY

class Consultor(object):
    def __init__(self, initial_date='1901-01-01', final_date='2000-12-31', nds = "Sunday"):
        self.initial_date = date.fromisoformat(initial_date)
        self.final_date = date.fromisoformat(final_date)
        self.ndw = nds

    def domingos(self):
        nd = 0
        for date in rrule(MONTHLY, dtstart=self.initial_date, until=self.final_date):
            ds = date.strftime("%A")
            if ds == self.ndw:
                nd += 1
        mensaje = "From {0} to {1}, {2} months have started a {3}".format(
                self.initial_date.strftime("%Y-%m-%d"),
                self.final_date.strftime("%Y-%m-%d"),
                nd, self.ndw)
        
        return mensaje, self.initial_date.strftime("%Y-%m-%d"), self.final_date.strftime("%Y-%m-%d"), nd, self.ndw

