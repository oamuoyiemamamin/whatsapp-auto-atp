import pywhatkit as what
from datetime import datetime

def scheduleWhat():
    now = datetime.now()
    currTime = now.strftime("%H:%M")
    lstTime = currTime.split(':')
    dictTime = {'H': int(lstTime[0]), 'M': int(lstTime[1]) + 1}
    return dictTime

fh = open("phNums.txt")
lstPhNums = []

for line in fh:
    line = line.strip()
    lstPhNums.append(line)

for phNum in lstPhNums:
    dictHourMinute = scheduleWhat()
    what.sendwhatmsg(phNum, "This is the advertisement", dictHourMinute['H'], dictHourMinute['M'])


