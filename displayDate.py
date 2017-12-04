#Max Low
#11-16-17
#display Date.py

from datetime import date
from calendar import weekday

# set todays date, to then pull out various peices from it
today = date.today()

# list of the months and days of the week to convert the numerical value to text
dayOfWeek = ["Monday","Tuesday","Wenesday","Thursday","Friday","Saterday","Sunday"]
monthOfYear = ["January","Febuary","March","April","May","June","July","Auguest","September","October","November","December"]

# the numerial day of the week function acounts for programs starting counting on 0, the months of the year do not
weeks = dayOfWeek[today.weekday()]
months = monthOfYear[today.month-1]

print("Today is",weeks,months,today.day,today.year)
