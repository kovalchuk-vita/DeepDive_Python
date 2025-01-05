"""
Write a Python program to display the dates in the following formats.
Sample format :
Default format of LocalDate=2016-09-16 16::Sep::2016
Default format of LocalDateTime=2016-09-16T11:46:01.455 16::Sep::2016 11::46::01
Default format of Instant=2016-09-16T06:16:01.456Z
Default format after parsing = 2014-04-27T21:39:48
"""
import time
from time import gmtime
from time import strftime
from time import strptime
from datetime import datetime

print(time.time()) #1727893129.827253 - UTC current local time
print(gmtime(1727893129.827253))
print(gmtime(0)) # system date/time

#human format
now = gmtime(time.time())
#LocalDate=2016-09-16 16::Sep::2016
print(strftime('%Y %m %d', now))
print(strftime('%d %b %Y', now))

#2016-09-16T11:46:01.455 16::Sep::2016 11::46::01
now = "2016-09-16T11:46:01.455"
dt = datetime.strptime(now, '%Y-%m-%dT%H:%M:%S.%f')
formatted_date = dt.strftime("%Y %m %d %H:%M:%S.%f")
print("Formatted Date:", formatted_date)

now= "16::Sep::2016 11::46::01"
dt1 = datetime.strptime(now, '%d::%b::%Y %H::%M::%S')
formatted_date = dt.strftime("%d %b %Y, %H:%M:%S %p")
print("Formatted Date:", formatted_date)

#Default format of Instant=2016-09-16T06:16:01.456Z
now = "2016-09-16T06:16:01.456Z"
dt = datetime.strptime(now[:-1], '%Y-%m-%dT%H:%M:%S.%f')
formatted_date = dt.strftime("%Y %m %d, %H:%M:%S.%f %p")
print("Formatted Date:", formatted_date)

#Default format after parsing = 2014-04-27T21:39:48
now = "2014-04-27T21:39:48"
dt = datetime.strptime(now, '%Y-%m-%dT%H:%M:%S')
formatted_date = dt.strftime("%Y %m %d, %I:%M:%S %p")
print("Formatted Date:", formatted_date)
