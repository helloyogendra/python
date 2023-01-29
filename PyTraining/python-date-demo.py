# Python Dates

import datetime

now = datetime.datetime.now()   #get the current date and time from system

print(now)

print(now.day)
print(now.year)
print(now.month)

print(now.strftime("%A"))   #format the current-date-time result to get the name of the day

print(now.strftime("%B"))   #get month name, full-name

print(now.strftime("%z"))   #get timezone

# print(datetime.datetime.strptime(str(now), "%Z"))   #get timezone

my_date = datetime.datetime(1995, 8, 25)

rs = now - my_date
print(rs)