# Make a python program to automatically send messages to people in a ".txt" file.
import pywhatkit as whats
from datetime import datetime

def scheduleWhatsapp():
    # Finding out the current time
    now = datetime.now()
    # Formatting the current time so that there is only hours and minutes
    currTime = now.strftime('%H:%M')
    lstTime = currTime.split(':')
    dictTime = {'H': int(lstTime[0]), 'M': int(lstTime[1]) + 1}
    return dictTime


lstPhNums = []
fh = open('phNums.txt')
for line in fh:
    lstPhNums.append(line)

dictT = scheduleWhatsapp()

for phNum in lstPhNums:
    whats.sendwhatmsg(phNum, "This is from Python", dictT["H"], dictT["M"])
