from datetime import datetime, date
from dateutil.rrule import rrule, MONTHLY

class Consultor(object):
    def __init__(self, initial_date='1901-01-01', final_date='2000-12-31', nds = "Sunday"):
        fi = tuple(initial_date.split('-'))
        ff = tuple(final_date.split('-'))
        self.initial_date = date(int(fi[0]),int(fi[1]),int(fi[2]))
        self.final_date = date(int(ff[0]),int(ff[1]),int(ff[2]))
        self.ndw = nds
        # self.created = created or datetime.now()

    def domingos(self):
        """Obtiene la cantidad de domingos, dado un rango de fechas"""

        nd = 0
        # nds = "Sunday"

        #Se usa rrule para obtener una lista iterable de fechas. MONTLY para extraer el primer día del mes.
        
        for date in rrule(MONTHLY, dtstart=self.initial_date, until=self.final_date):
            # print (fecha)
            ds = date.strftime("%A")
            if ds == self.ndw:
                nd += 1
        mensaje = "From {0} to {1}, {2} months have started a {3}".format(
                self.initial_date.strftime("%Y-%m-%d"),
                self.final_date.strftime("%Y-%m-%d"),
                nd, self.ndw)
        
        return mensaje, self.initial_date.strftime("%Y-%m-%d"), self.final_date.strftime("%Y-%m-%d"), nd, self.ndw
