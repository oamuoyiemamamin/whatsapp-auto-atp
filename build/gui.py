
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#445768")


canvas = Canvas(
    window,
    bg = "#445768",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    8.0,
    10.0,
    991.0,
    119.0,
    fill="#1D2424",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg="#1D2424"
)
button_1.place(
    x=551.0,
    y=36.0,
    width=398.0,
    height=58.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    bg="#1D2424"
)
button_2.place(
    x=51.0,
    y=36.0,
    width=398.0,
    height=58.0
)

canvas.create_rectangle(
    9.0,
    123.0,
    497.0,
    595.0,
    fill="#DCDCDD",
    outline="")

canvas.create_rectangle(
    503.0,
    123.0,
    991.0,
    595.0,
    fill="#DCDCDD",
    outline="")

canvas.create_rectangle(
    111.0,
    146.0,
    395.0,
    196.0,
    fill="#69849B",
    outline="")

canvas.create_rectangle(
    605.0,
    146.0,
    889.0,
    196.0,
    fill="#69849B",
    outline="")

canvas.create_text(
    172.0,
    156.0,
    anchor="nw",
    text="Edit Message",
    fill="#FFFFFF",
    font=("Inter ExtraLight", 25 * -1)
)

canvas.create_text(
    683.0,
    156.0,
    anchor="nw",
    text="Select Data",
    fill="#FFFFFF",
    font=("Inter ExtraLight", 25 * -1)
)

canvas.create_text(
    122.0,
    216.0,
    anchor="nw",
    text="Waiting Time:",
    fill="#000000",
    font=("Inter Light", 20 * -1)
)

canvas.create_text(
    38.0,
    270.0,
    anchor="nw",
    text="Message",
    fill="#000000",
    font=("Inter Medium", 23 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    328.0,
    227.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#A8D4D0",
    highlightthickness=0
)
entry_1.place(
    x=268.0,
    y=209.0,
    width=120.0,
    height=34.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    250.0,
    446.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#A8D4D0",
    highlightthickness=0
)
entry_2.place(
    x=49.0,
    y=307.0,
    width=402.0,
    height=277.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    bg="#CDCDCD"
)
button_3.place(
    x=649.0,
    y=510.0,
    width=201.0,
    height=53.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
    bg="#CDCDCD"
)
button_4.place(
    x=326.0,
    y=268.0,
    width=137.0,
    height=40.0
)

canvas.create_rectangle(
    535.0,
    219.0,
    965.0,
    487.0,
    fill="#D0C3BD",
    outline="")

canvas.create_rectangle(
    728.0,
    287.0,
    730.0,
    473.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    552.0,
    332.0,
    952.0,
    334.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    552.0,
    379.0,
    952.0,
    381.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    552.0,
    428.0,
    952.0,
    430.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    570.0,
    239.0,
    684.0,
    277.0,
    fill="#3D6A66",
    outline="")

canvas.create_text(
    604.0,
    246.0,
    anchor="nw",
    text="Data",
    fill="#FFFFFF",
    font=("Inter Light", 20 * -1)
)

canvas.create_text(
    660.0,
    301.0,
    anchor="nw",
    text="Name:",
    fill="#000000",
    font=("Inter Light", 20 * -1)
)

canvas.create_text(
    580.0,
    345.0,
    anchor="nw",
    text="Phone Number:",
    fill="#000000",
    font=("Inter Light", 20 * -1)
)

canvas.create_text(
    629.0,
    394.0,
    anchor="nw",
    text="Group ID:",
    fill="#000000",
    font=("Inter Light", 20 * -1)
)

canvas.create_text(
    572.0,
    440.0,
    anchor="nw",
    text="Group Greeting:",
    fill="#000000",
    font=("Inter Light", 20 * -1)
)

canvas.create_rectangle(
    753.0,
    238.0,
    927.0,
    276.0,
    fill="#3D6A66",
    outline="")

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
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
entry_bg_4 = canvas.create_image(
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
entry_bg_5 = canvas.create_image(
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
entry_bg_6 = canvas.create_image(
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

canvas.create_text(
    777.0,
    245.0,
    anchor="nw",
    text="Select Column",
    fill="#FFFFFF",
    font=("Inter Light", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
