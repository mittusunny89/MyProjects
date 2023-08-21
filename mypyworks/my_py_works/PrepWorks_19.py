#Write a Python program to get the current time in Python.
#Sample Format :  13:19:49.078205
import datetime

now = datetime.datetime.now()
fnow = now.strftime(" %H:%M:%S%f")
print(now.strftime("%Y-%m-%d %H:%M:%S%f").rstrip("0")) 
print(fnow)