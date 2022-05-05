from datetime import datetime
import pywhatkit as what

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

def sendMsg(lst_given, content_given, waiting_time=15):
    for name, phNum in lst_given:
        dictTime = scheduleWhatsapp()
        try:
            what.sendwhatmsg(
                phNum,
                content_given.format(name),
                dictTime["H"],
                dictTime["M"],
                wait_time=waiting_time,
                tab_close=True,
                close_time=10,
            )
        except what.core.exceptions.CallTimeException:
            print("Error on phone number {}\nError: {}".format(phNum, f"If we wait for {waiting_time} seconds on this phone number, it won't send the phone number on time. Try again."))

def sendGroupMsg(lst_given, content, waiting_time=15):
    for groupID, greeting in lst_given:
        dictTime = scheduleWhatsapp()
        try:
            print(dictTime)
            what.sendwhatmsg_to_group(
                groupID,
                content.format(greeting),
                dictTime["H"],
                dictTime["M"],
                wait_time=waiting_time,
                tab_close=True
            )
        except what.core.exceptions.CallTimeException:
            print("Error on group id {}\nError: {}".format(groupID, f"If we wait for {waiting_time} seconds on this group, it won't send the phone number on time. Try again."))
            print(dictTime)

def sendAllMessages(lst_phone, lst_group, content, wait_time):
    sendMsg(lst_phone, content, wait_time)
    sendGroupMsg(lst_group, content, wait_time)
