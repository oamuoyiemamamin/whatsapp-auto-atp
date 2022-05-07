import time
import os
import threading
import whatsATP

from pathlib import Path
import pandas as pd
import phonenumbers

from pystray import MenuItem as item, Menu
import pystray
from PIL import Image
import tkinter as tk
from tkinter import Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog


"""
We will get the name, email, phone, package (free or paid), group_id (whatsapp group id) and greeting seperately from the excel file

name: is used to greet the person with the name
email: is not being used currently
phone: is used to send a private message if there is no group
package: free or paid, not being used currently
group_id: is used to send messages to a group, is prioritised if both phone and group id are present
greeting: is used for the greeting in groups, if absent when sending a group message, "name" will be used
"""


def sendAllMessagesThread(lst_phone, lst_group, content, wait_time):
    sendMsgThread = threading.Thread(target=whatsATP.sendAllMessages, args=[lst_phone, lst_group, content, wait_time])
    sendMsgThread.start()
    # sendMsgThread.join()


# Window Setup
root = tk.Tk()
root.geometry("1000x600")
root.title("WhatsApp Automation - AI Tech Park Sdn. Bhd.")
root.resizable(False, False)
root.configure(bg="#445768")
root.configure(bg="#445768")
logo = tk.PhotoImage(file="../media/AITECHPARK-logo.png")
root.iconphoto(False, logo)

logo_tray = Image.open("../media/AITECHPARK-logo.ico")

lstPhoneGroup = []
lstGroupSendGroup = []


def quit_window(icon, item):
    icon.stop()
    root.destroy()

def show_window(icon, item):
    icon.stop()
    root.after(0, root.deiconify)

def withdraw_window():
    root.withdraw()
    menu = Menu(item('Show', show_window, default=True), item('Quit', quit_window))
    icon = pystray.Icon("WhatsApp Automation", logo_tray, "WhatsApp Automation - AI Tech Park", menu)
    icon.run()

def importExcelData():
    global lstPhoneGroup
    global lstGroupSendGroup
    global excel_file_path

    excel_file_path = filedialog.askopenfilename(initialdir="/Documents", title="Select an Excel File to Import", filetypes=(("MS Excel", "*.xlsx"),))
    excel_file_path = excel_file_path.replace("\\", "/")

    raw_df = pd.read_excel(excel_file_path, converters={"phone": str})
    recipients = raw_df.fillna("null")

    lstRecipients = []

    recipients.columns = [column.lower() for column in recipients.columns]

    for index, value in recipients.iterrows():
        lstRecipients.append((value["name"], value["phone"], value["group_id"], value["greeting"]))

    tempDictGroupIDs = {}
    for recipient in lstRecipients:
        name, phone, group_id, greeting = recipient[0], recipient[1], recipient[2], recipient[3]

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

def editExcelData():
    # subprocess.run(['start', f'"{excel_file_path}"'], check=True)
    # import subprocess, os, platform
    # if platform.system() == 'Darwin':  # macOS
    #     subprocess.call(('open', filepath))
    # elif platform.system() == 'Windows':  # Windows
    #     os.startfile(filepath)
    # else:  # linux variants
    #     subprocess.call(('xdg-open', filepath))

    os.startfile(excel_file_path)


msg_f = r"./message.txt"

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

######## Testing Code ########
# sendGroupMsg(lstGroupID, msg)
# sendMsg(lstPhNum, msg, waiting_seconds)
# print(msg)
#################################


################## UI Components ##################


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../main-program/assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


mainCanvas = Canvas(
    root,
    bg="#445768",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

mainCanvas.place(x=0, y=0)
mainCanvas.create_rectangle(
    8.0,
    10.0,
    991.0,
    119.0,
    fill="#1D2424",
    outline="")

btnSendMessages_image = PhotoImage(
    file=relative_to_assets("button_1.png"))
btnSendMessages = Button(
    image=btnSendMessages_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: sendAllMessagesThread(lstPhoneGroup, lstGroupSendGroup, msg, waiting_seconds),
    relief="flat",
    bg="#1D2424"
)
btnSendMessages.place(
    x=551.0,
    y=36.0,
    width=398.0,
    height=58.0
)

popup = tk.Menu(root, tearoff=0)
popup.add_command(label="Quit", command=root.destroy)

def popupm(bt):
    try:
        x = bt.winfo_rootx()
        y = bt.winfo_rooty()
        popup.tk_popup(x-63, y+20, 0)
    finally:
        popup.grab_release()

btnSettings_image = PhotoImage(file=relative_to_assets("settings-gear_40x40.png"))
btnSettings = Button(
    image=btnSettings_image,
    borderwidth=3,
    highlightthickness=0,
    relief="flat",
    bg="#1D2424"
)
btnSettings.configure(command=lambda: popupm(btnSettings))
btnSettings.place(
    x=950.0,
    y=10.0,
    width=40.0,
    height=40.0
)

btnImport_image = PhotoImage(
    file=relative_to_assets("button_2.png"))
btnImport = Button(
    image=btnImport_image,
    borderwidth=0,
    highlightthickness=0,
    command=importExcelData,
    relief="flat",
    bg="#1D2424"
)
btnImport.place(
    x=51.0,
    y=36.0,
    width=398.0,
    height=58.0
)

mainCanvas.create_rectangle(
    9.0,
    123.0,
    497.0,
    595.0,
    fill="#DCDCDD",
    outline="")

mainCanvas.create_rectangle(
    503.0,
    123.0,
    991.0,
    595.0,
    fill="#DCDCDD",
    outline="")

mainCanvas.create_rectangle(
    111.0,
    146.0,
    395.0,
    196.0,
    fill="#69849B",
    outline="")

mainCanvas.create_rectangle(
    605.0,
    146.0,
    889.0,
    196.0,
    fill="#69849B",
    outline="")

mainCanvas.create_text(
    172.0,
    156.0,
    anchor="nw",
    text="Edit Message",
    fill="#FFFFFF",
    font=("Inter ExtraLight", 25 * -1)
)

mainCanvas.create_text(
    683.0,
    156.0,
    anchor="nw",
    text="Select Data",
    fill="#FFFFFF",
    font=("Inter ExtraLight", 25 * -1)
)

mainCanvas.create_text(
    122.0,
    216.0,
    anchor="nw",
    text="Waiting Time:",
    fill="#000000",
    font=("Inter Light", 20 * -1)
)

mainCanvas.create_text(
    38.0,
    270.0,
    anchor="nw",
    text="Message",
    fill="#000000",
    font=("Inter Medium", 23 * -1)
)

entryWaitSec_image = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entryWaitSec_bg = mainCanvas.create_image(
    328.0,
    227.0,
    image=entryWaitSec_image
)
entryWaitSec = Entry(
    bd=0,
    bg="#A8D4D0",
    highlightthickness=0
)
entryWaitSec.place(
    x=268.0,
    y=209.0,
    width=120.0,
    height=34.0
)

textareaContent_image = PhotoImage(
    file=relative_to_assets("entry_2.png"))
textareaContent_bg = mainCanvas.create_image(
    250.0,
    446.5,
    image=textareaContent_image
)
textareaContent = Text(
    bd=0,
    bg="#A8D4D0",
    highlightthickness=0
)
textareaContent.place(
    x=49.0,
    y=307.0,
    width=402.0,
    height=277.0
)

btnEditData_image = PhotoImage(
    file=relative_to_assets("button_3.png"))
btnEditData = Button(
    image=btnEditData_image,
    borderwidth=0,
    highlightthickness=0,
    command=editExcelData,
    relief="flat",
    bg="#CDCDCD"
)
btnEditData.place(
    x=649.0,
    y=510.0,
    width=201.0,
    height=53.0
)

btnInsertGreeting_image = PhotoImage(
    file=relative_to_assets("button_4.png"))
btnInsertGreeting = Button(
    image=btnInsertGreeting_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
    bg="#CDCDCD"
)
btnInsertGreeting.place(
    x=326.0,
    y=268.0,
    width=137.0,
    height=40.0
)

mainCanvas.create_rectangle(
    535.0,
    219.0,
    965.0,
    487.0,
    fill="#D0C3BD",
    outline="")

mainCanvas.create_rectangle(
    728.0,
    287.0,
    730.0,
    473.0,
    fill="#FFFFFF",
    outline="")

mainCanvas.create_rectangle(
    552.0,
    332.0,
    952.0,
    334.0,
    fill="#FFFFFF",
    outline="")

mainCanvas.create_rectangle(
    552.0,
    379.0,
    952.0,
    381.0,
    fill="#FFFFFF",
    outline="")

mainCanvas.create_rectangle(
    552.0,
    428.0,
    952.0,
    430.0,
    fill="#FFFFFF",
    outline="")

mainCanvas.create_rectangle(
    570.0,
    239.0,
    684.0,
    277.0,
    fill="#3D6A66",
    outline="")

mainCanvas.create_text(
    604.0,
    246.0,
    anchor="nw",
    text="Data",
    fill="#FFFFFF",
    font=("Inter Light", 20 * -1)
)

mainCanvas.create_text(
    660.0,
    301.0,
    anchor="nw",
    text="Name:",
    fill="#000000",
    font=("Inter Light", 20 * -1)
)

mainCanvas.create_text(
    580.0,
    345.0,
    anchor="nw",
    text="Phone Number:",
    fill="#000000",
    font=("Inter Light", 20 * -1)
)

mainCanvas.create_text(
    629.0,
    394.0,
    anchor="nw",
    text="Group ID:",
    fill="#000000",
    font=("Inter Light", 20 * -1)
)

mainCanvas.create_text(
    572.0,
    440.0,
    anchor="nw",
    text="Group Greeting:",
    fill="#000000",
    font=("Inter Light", 20 * -1)
)

mainCanvas.create_rectangle(
    753.0,
    238.0,
    927.0,
    276.0,
    fill="#3D6A66",
    outline="")

# !!! Change all these entries into dropdowns to select the column names
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = mainCanvas.create_image(
    840.0,
    308.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D5E2EC",
    highlightthickness=0
)
entry_3.place(
    x=757.0,
    y=288.0,
    width=166.0,
    height=39.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = mainCanvas.create_image(
    840.0,
    356.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D5E2EC",
    highlightthickness=0
)
entry_4.place(
    x=757.0,
    y=336.0,
    width=166.0,
    height=39.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = mainCanvas.create_image(
    840.0,
    404.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D5E2EC",
    highlightthickness=0
)
entry_5.place(
    x=757.0,
    y=384.0,
    width=166.0,
    height=39.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = mainCanvas.create_image(
    840.0,
    453.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D5E2EC",
    highlightthickness=0
)
entry_6.place(
    x=757.0,
    y=433.0,
    width=166.0,
    height=39.0
)

mainCanvas.create_text(
    777.0,
    245.0,
    anchor="nw",
    text="Select Column",
    fill="#FFFFFF",
    font=("Inter Light", 20 * -1)
)

###################################################


root.protocol('WM_DELETE_WINDOW', withdraw_window)

root.mainloop()
