#Write a Python program to calculate the number of days between two date times.
import datetime
#print(dir(datetime))
now = datetime.datetime.now()
delta = datetime.timedelta(days =2, hours= 3)


fdate = datetime.datetime(year = 2022,month = 10, day = 1, hour= 3)

sdate = datetime.datetime(year = 2024,month = 9, day = 10)
tdelta = sdate - fdate

print(delta)
print(tdelta)