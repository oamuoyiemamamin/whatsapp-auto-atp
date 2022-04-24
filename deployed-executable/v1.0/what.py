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
    lstTimeTemp = currTime.split(":")
    for thing in lstTimeTemp:
        thing = int(thing)
        lstTime.append(thing)
    dictTime = {"H": lstTime[0], "M": lstTime[1] + 1}
    return dictTime


lstPhNum = []


# def sendDummyMsg():
#     for phNum in lstPhNum:
#         dictTime = scheduleWhatsapp()
#         what.sendwhatmsg(
#             phNum, "This is from Python", dictTime["H"], dictTime["M"] + 1
#         )
#         time.sleep(10)
#         pg.hotkey("ctrl", "w")


def sendMsg(lst_given, content_given, waiting_time):
    for phNum in lst_given:
        dictTime = scheduleWhatsapp()
        what.sendwhatmsg(
            phNum,
            content_given,
            dictTime["H"],
            dictTime["M"],
            wait_time=waiting_time,
            tab_close=True,
            close_time=10,
        )


f = "message.txt"
fh = open(f, "r")
msg = "".join(fh.readlines()[1:])
fh.close()

with open("phNums.txt") as fh:
    for line in fh:
        lstPhNum.append(line)

with open(f) as fh:
    waiting_seconds_raw = fh.readlines()[0]
    waiting_seconds_index = waiting_seconds_raw.find(": ")
    waiting_seconds = int(waiting_seconds_raw[waiting_seconds_index + 2 :])
    # print(waiting_seconds, type(waiting_seconds))

sendMsg(lstPhNum, msg, waiting_seconds)
# print(msg)
