#!/user/bin/python
# Python Ver:     2.7
#
# Author:	      Terri Hall
#
# Purpose:	       To get time from New York and London office and see if that current time
#                  shows if those offices are open or not. Compare to current time in Portland office.
#
# Tested OS:       This code was written and tested to work with Windows 10.
 
from datetime import datetime
from pytz import timezone

pdx = datetime.now() 
print("Current time in Portland is :")
stringPDX = (pdx.strftime("%H:%M:%S"))
print stringPDX

newYork = datetime.now(timezone("America/New_York"))
print("The current time in New York is:")
stringNewYork = (newYork.strftime("%H:%M:%S"))
print stringNewYork

if ("09:00:00") < stringNewYork and stringNewYork < ("17:00:00"):
    print "New York Office Is Open"
else:
    print "New York Office Is Closed"

london = datetime.now(timezone("Europe/London"))
print("The current time in London is:")
stringLondon = (london.strftime("%H:%M:%S"))
print stringLondon

if ("09:00:00") < stringLondon and stringLondon < ("17:00:00"):
    print "The London Office Is Open"
else:
    print "The London Office Is Closed"





