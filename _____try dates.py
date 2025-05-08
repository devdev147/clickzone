import pandas as pd
import datetime 
from datetime import date
from datetime import timedelta
def numOfDays(date1, date2):
        #check which date is greater to avoid days output in -ve number
        if date2 > date1:
                return (date2-date1).days
        else:
                return (date1-date2).days 
# Driver program
#date1 = date(2023, 12, 15)
#date2 = date(2023, 12, 18)

#date1 = date(20231215).strftime("%Y%m%d")
#date2 = date(20231219).strftime("%Y%m%d")

# convert from string format to datetime format
d1 = '20231215'
d2 = '20240115'
format = '%Y%m%d'
date1 = datetime.datetime.strptime(d1, format)
date2 = datetime.datetime.strptime(d2, format)
'''
# convert from int format to datetime format
d1 = 20231215
d2 = 20231219
format = '%Y%m%d'
date1 = datetime.datetime.intptime(d1, format)
date2 = datetime.datetime.intptime(d2, format)
'''
print(numOfDays(date1, date2), "days")
dates = pd.date_range(date1,date2-timedelta(days=1),freq='d').strftime('%Y%m%d').tolist()
print(dates)
print(','.join(dates))
print("XYZ"+','.join(dates))

#datesbooked = pd.date_range(roombookingdateend.get(), roombookingdatestart.get()-timedelta(days=1),freq='d').strftime('%Y%m%d').tolist()
#staynumofdays = datetime.strptime(roombookingdateend.get(),"%Y%m%d") - datetime.strptime(roombookingdatestart.get(),"%Y%m%d")',

print((date2-date1).days)

#datestobebooked = ",".join(pd.date_range(datetime.strptime(roombookingdateend.get(),"%Y%m%d"), datetime.strptime(roombookingdatestart.get(),"%Y%m%d")).strftime("%Y%m%d").tolist())',
datestobebooked = ",".join(pd.date_range('20231215', '20231219').strftime("%Y%m%d").tolist())
print(datestobebooked)
                           

#print(pd.explode(pd.date_range(date1, date2).strftime("%Y%m%d").tolist()))

