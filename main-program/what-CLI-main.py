import pywhatkit as what
import time
import pyautogui as pg
from datetime import datetime
import pandas as pd
from tkinter import *
import os

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

"""
We will get the name, email, phone, package (free or paid), group_id (whatsapp group id) and greeting seperately from the excel file

name: is used to greet the person with the name
email: is not being used currently
phone: is used to send a private message if there is no group
package: free or paid, not being used currently
group_id: is used to send messages to a group, is prioritised if both phone and group id are present
greeting: is used for the greeting in groups, if absent when sending a group message, "name" will be used
"""

# print(os.path.dirname(os.path.abspath(__file__)))
directoryPath = StringVar()

raw_df = pd.read_excel(directoryPath + r'/recepient_db.xlsx', converters={"phone": str})
recepients = raw_df.fillna("null")

root = Tk()
width, height = "1000", "600"
root.geometry("{}x{}".format(width, height))
root.title("WhatsApp Automation - AI Tech Park Sdn. Bhd.")
# root.resizable(0,0)

lstRecepients = []
lstPhoneGroup = []
lstGroupSendGroup = []

for index, value in recepients.iterrows():
    lstRecepients.append((value["name"], value["email"], value["phone"], value["package"], value["group_id"], value["greeting"]))

tempDictGroupIDs = {}
for recepient in lstRecepients:
    name, email, phone, package, group_id, greeting = recepient[0], recepient[1], recepient[2], recepient[3], recepient[4], recepient[5]
    
    # If there is phone and no group_id.
    if phone != "null" and group_id == "null":
        lstPhoneGroup.append((name, phone))
    # If there is no phone and there is a group_id.
    elif phone == "null" and group_id != "null":
        # If the group_id does not exist.
        if not group_id in tempDictGroupIDs.keys():
            tempDictGroupIDs[group_id] = name
            if greeting != "null":
                tempDictGroupIDs[group_id] = greeting
        # If there is no greeting but the group_id is present, raise error
        else:
            if greeting == "null":
                print(f'Error on person {name}.\nError: Greeting must be present if sending through group for multiple people.')
                break
            tempDictGroupIDs[group_id] = greeting
    
    # If there is both phone and group_id
    elif phone != "null" and group_id != "null":
        if not group_id in tempDictGroupIDs.keys():
            tempDictGroupIDs[group_id] = name
            if greeting != "null":
                tempDictGroupIDs[group_id] = greeting
        else:
            if greeting == "null":
                print(f'Error on person {name}.\nError: Greeting must be present if sending through group for multiple people.')
                break
            tempDictGroupIDs[group_id] = greeting
    
    # If both are not present
    elif phone == "null" and group_id == "null":
        print(f"The phone number or WhatsApp group id of {name} must be present.")

for id, greeting in tempDictGroupIDs.items():
    lstGroupSendGroup.append((id, greeting))

print(lstPhoneGroup, lstGroupSendGroup, tempDictGroupIDs, sep='\n')

msg_f = directoryPath + r"/message.txt"

with open(msg_f, 'r') as fh:
    msg = "".join(fh.readlines()[1:])

# Getting the waiting seconds
with open(msg_f) as fh:
    waiting_seconds_raw = fh.readlines()[0]
    waiting_seconds_index = waiting_seconds_raw.find(":")
    waiting_seconds = int(waiting_seconds_raw[waiting_seconds_index+1:].strip())
    # print(waiting_seconds, type(waiting_seconds))

######## Deprecated Code ########
# with open("phNums.txt") as fh:
#     for line in fh:
#         lstPhNum.append(line)
#################################

sendMsg(lstPhoneGroup, msg, waiting_seconds)
sendGroupMsg(lstGroupSendGroup, msg, waiting_time=waiting_seconds)

######## Testing Code ########
# sendGroupMsg(lstGroupID, msg)
# sendMsg(lstPhNum, msg, waiting_seconds)
# print(msg)
#################################

testButton = Button(root, bg="red")
testButton.pack()
testButton.pack()

root.mainloop()
