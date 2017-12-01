#Max Low
#11-16-17
#display Date.py

from datetime import date
from calendar import weekday

today = date.today()
day = today.day
month = today.month
year = today.year
week = today.weekday()


dayOfWeek = ["Monday","Tuesday","Wenesday","Thursday","Friday","Saterday","Sunday"]
monthOfYear = ["January","Febuary","March","April","May","June","July","Auguest","September","October","November","December"]

weeks = dayOfWeek[week]
months = monthOfYear[month]

print("Today is",weeks,months,day,year)
