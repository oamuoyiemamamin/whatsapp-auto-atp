from tokenize import group
import pywhatkit as what
import time
import pyautogui as pg
from datetime import datetime
import pandas as pd
from tkinter import *

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

raw_df = pd.read_excel('./recepient_db.xlsx', converters={"phone": str})
recepients = raw_df.fillna("null")

lstRecepients = []
lstPhoneGroup = []
lstGroupSendGroup = []

for index, value in recepients.iterrows():
    lstRecepients.append((value["name"], value["email"], value["phone"], value["package"], value["group_id"], value["greeting"]))

tempDictGroupIDs = {}
for recepient in lstRecepients:
    name, email, phone, package, group_id, greeting = recepient[0], recepient[1], recepient[2], recepient[3], recepient[4], recepient[5]
    
    if phone != "null" and group_id == "null":
        lstPhoneGroup.append((name, phone))
    elif phone == "null" and group_id != "null":
        if not group_id in tempDictGroupIDs.keys():
            tempDictGroupIDs[group_id] = name
            if greeting != "null":
                tempDictGroupIDs[group_id] = greeting
        else:
            if greeting == "null":
                print(f'Error on person {name}.\nError: Greeting must be present if sending through group for multiple people.')
                break
            tempDictGroupIDs[group_id] = greeting
    
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
    
    elif phone == "null" and group_id == "null":
        print(f"The phone number or WhatsApp group id of {name} must be present.")

for id, greeting in tempDictGroupIDs.items():
    lstGroupSendGroup.append((id, greeting))

print(lstPhoneGroup, lstGroupSendGroup, tempDictGroupIDs, sep='\n')

msg_f = "message.txt"

with open(msg_f, 'r') as fh:
    msg = "".join(fh.readlines()[1:])

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
