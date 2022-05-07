from datetime import datetime
import pywhatkit as what
import tkinter as tk
from tkinter import ttk


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
            print("Error on phone number {}\nError: {}".format(phNum,
                                                               f"If we wait for {waiting_time} seconds on this phone number, it won't send the phone number on time. Try again."))


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
            print("Error on group id {}\nError: {}".format(groupID,
                                                           f"If we wait for {waiting_time} seconds on this group, it won't send the phone number on time. Try again."))
            print(dictTime)


def sendAllMessages(lst_phone, lst_group, content, wait_time):
    sendMsg(lst_phone, content, wait_time)
    sendGroupMsg(lst_group, content, wait_time)


class ToastContainer(tk.Toplevel):
    """
            -----DESCRIPTION-----
    A template for new widgets.
            -----USAGE-----
    toasterbox = ToasterBox(parent)
    toasterbox.create_popup(title=[string], image=[photoimage]/[string], message=[string], life=[integer])
            -----PARAMETERS-----
    parent = The parent of the widget.
            -----CONTENTS-----
    ---VARIABLES---
    parent         = The parent of the widget.
    _width         = The width of the widget.
    _padx          = The horizontal padding of the widget.
    _pady          = The vertical padding of the widget.
    _popup_fit     = The amount of popups to fit into the widget.
    _popup_pad     = The padding of the popups.
    _popup_ipad    = The internal padding of the popups.
    _popup_height  = The height of each popup.
    ---TKINTER VARIABLES---
    None
    ---WIDGETS---
    self
    ---FUNCTIONS---
    create_popup() = Creates a new popup.
    remove_toasterbox() = Removes the instance of Toaster Box.
    """

    def __init__(self, parent, width=350, padx=5, pady=45, popup_pad=5, popup_ipad=3, popup_height=100,
                 *args):
        tk.Toplevel.__init__(self, parent, *args)
        self.parent = parent
        self._width = width
        self._padx = padx
        self._pady = pady
        # self._popup_fit = popup_fit # Replaced by _popup_count
        self._popup_pad = popup_pad
        self._popup_ipad = popup_ipad
        self._popup_height = popup_height
        self._popup_count = 0

        self.attributes("-toolwindow", True, "-topmost", True)
        self.overrideredirect(True)

        self.refresh_size()

        ttk.Style().configure("Popup.TFrame", borderwidth=10, relief="raised")
        ttk.Style().configure("Close.Popup.TButton")
        ttk.Style().configure("Image.Popup.TLabel")
        ttk.Style().configure("Title.Popup.TLabel")
        ttk.Style().configure("Message.Popup.TLabel")

    def create_popup(self, title="", image=None, message="", life=0):
        """Creates a new popup."""
        popup = Popup(self, title=title, image=image, message=message, life=life, height=self._popup_height,
                      ipad=self._popup_ipad)
        popup.pack(side="bottom", fill="x", pady=self._popup_pad)
        self._popup_count += 1
        self.refresh_size()

        return popup

    def refresh_size(self):
        if self._popup_count < 1:
            self.withdraw()
        else:
            self.deiconify()

        self.geometry("{}x{}".format(self._width, self._popup_count * (self._popup_height + (self._popup_pad * 2))))
        self.update()
        self.geometry("+{}+{}".format((self.winfo_screenwidth() - self.winfo_width()) - self._padx,
                                      (self.winfo_screenheight() - self.winfo_height()) - self._pady))


class Popup(ttk.Frame):
    def __init__(self, parent, title, image, message, life, height, ipad, *args):
        ttk.Frame.__init__(self, parent, height=height, style="Popup.TFrame", *args)
        self.parent = parent
        self._title = title
        self._image = image
        self._life = life
        self._message = message
        self._ipad = ipad

        self.grid_propagate(False)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        image = ttk.Label(self, image=self._image, style="Image.Popup.TLabel")
        image.grid(row=0, column=0, rowspan=2, sticky="nesw", padx=self._ipad, pady=self._ipad)

        title_frame = ttk.Frame(self)
        title_frame.grid(row=0, column=1, sticky="we", padx=self._ipad, pady=self._ipad)

        label = ttk.Label(title_frame, text=self._title, style="Title.Popup.TLabel")
        label.pack(side="left", fill="both", expand=True)

        close = ttk.Button(title_frame, text="X", width=3, command=self.remove, style="Close.Popup.TButton")
        close.pack(side="right")

        message = ttk.Label(self, text=self._message, style="Message.Popup.TLabel")
        message.grid(row=1, column=1, sticky="nw", padx=self._ipad, pady=self._ipad)

        if self._life > 0:
            self.after(self._life, self.remove)

    def remove(self, event=None):
        self.pack_forget()
        self.parent._popup_count -= 1
        self.parent.refresh_size()


# Testing toasbox
# import time
# import threading
# def delayed_popup():
#     time.sleep(5)
#     tbox.create_popup(title="Popup 7", message="Hello!")
# if __name__ == "__main__":
#     root = tk.Tk()
#     tbox = ToasterBox(root)
#     tbox.create_popup(title="Popup 1", message="Hello!")
#     tbox.create_popup(title="Popup 2", message="Hello!")
#     tbox.create_popup(title="Popup 3", message="Hello!")
#     tbox.create_popup(title="Popup 4", message="Hello!")
#     tbox.create_popup(title="Popup 5", message="Hello!")
#     tbox.create_popup(title="Popup 6", message="Hello!")
#     tbox.create_popup(title="Popup 7", message="Hello!")
#
#     t = threading.Thread(target=delayed_popup)
#     t.start()
#     root.mainloop()
