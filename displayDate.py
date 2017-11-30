#Max Low
#11-16-17
#display Date.py

from datetime import date
from calendar import weekday

today = date.today()

day = today.weekday()
month = int(today.month)
year = int(today.year)


dayOfWeek = ["Monday","Tuesday","Wenesday","Thursday","Friday","Saterday","Sunday"]
monthOfYear = ["January","Febuary","March","April","May","June","July","Auguest","September","October","November","December"]

print("Today is",dayOfWeek[today],monthOfYear[month],day,year)
