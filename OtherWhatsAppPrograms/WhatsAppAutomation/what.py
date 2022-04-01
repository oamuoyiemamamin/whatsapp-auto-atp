import pywhatkit as what
import time
import pyautogui as pg
from datetime import datetime

def scheduleWhatsapp():
    """This function is for simplifying the sendwhatmsg() from the pywhatkit library"""
    # Current time
    now = datetime.now()
    currTime = now.strftime("%H:%M")
    lstTime = list()
    lstTimeTemp = currTime.split(':')
    for thing in lstTimeTemp:
        thing = int(thing)
        lstTime.append(thing)
    dictTime = {'H': lstTime[0], 'M': lstTime[1] + 1}
    return dictTime

lstPhNum = ['+60174045322']

content = '''
Hello everyone,
Our 👨‍🏫 Intro to Computers and Python 👨‍🏫 class is going to start today (16 Aug 2021)! You can attend free if you are an alumnus of this course or a YEC member!

✨ Timings ⌛
  == 🇲🇾 7:00 PM - 8:30 PM 🇲🇾 ==
  == 🇮🇳 4:30 PM - 6:00 PM 🇮🇳 ==
  == Every Mon - Wed - Fri ==

🤓 New thins we added 📚:
  == File Handling ==
  == Exception Handling ==

🔗 Link to meeting: https://tinyurl.com/ATP-Room1

📢Please join the course using a 💻 laptop or a PC 🖥️ with a strong 🌐internet connection 🌐 for the best experience!📢

Thank you,
AI Tech Park Sdn. Bhd.
'''

def sendMultipleMsg(lst_phonenumbers, message):
    for phNum in lst_phonenumbers:
        dictTime = scheduleWhatsapp()
        what.sendwhatmsg(phNum, message, dictTime['H'], dictTime['M'] + 1)
        time.sleep(10)
        pg.hotkey('ctrl', 'w')

with open('phNums.txt') as fh:
    for line in fh:
        line = line.strip()
        lstPhNum.append(line)
        print(line)

# sendMultipleMsg(lstPhNum, content)

what.sendwhats_image()
