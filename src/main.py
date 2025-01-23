import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Custom_Buttons as cb


ROMS = {"NES": {"Title": [], "File": []},
        "SNES": {"Title": [], "File": []},
        "GB": {"Title": [], "File": []},
        "GBC": {"Title": [], "File": []},
        "GBA": {"Title": [], "File": []},
        "NDS": {"Title": [], "File": []}}

ROOT_PATH = r"C:\Users\tanne\OneDrive\Desktop\School2024\Python Stuff\EmulatorController"
# ROOT_PATH = r"/home/zekrom2378/"

GAME_COUNT = 0

def title_grabber(title):
    if len(title.split('.')) > 2:
        temp = title.split('.')
        temp = temp[:-1]
        title = ''.join(temp)

    if '(' in title:
        temp = title.split('(')
        title = temp[0]

    if '[' in title:
        temp = title.split('[')
        title = temp[0]

    if ' - ' in title:
        temp = title.split(' - ')
        if temp[0].isnumeric():
            title = temp[1:]
            title = ''.join(title)
        elif temp[0].isalpha():
            title = ' '.join(temp)

    title = title.strip()
    return title


for key in ROMS:
    files = os.listdir(ROOT_PATH + '\\' + key.lower())
    # files = os.listdir(ROOT_PATH + '/' + key.lower())
    for file in files:
        ROMS[key]["File"].append(file)
        GAME_COUNT += 1
        ROMS[key]["Title"].append(title_grabber(file))


def selection_button(rom_dict, row_num):
    for key in rom_dict:
        for name in rom_dict[key]["Title"].value():
            selection = cb.Selection_Button(frm, text=name, command=root.destroy, anchor="w")
            selection.grid(row=row_num, column=0, columnspan=2, sticky="ew")


# def selection_button(text, game, row):
#     selection = cb.Selection_Button(frm, text=text, command=game, anchor="w")
#     selection.grid(row=row, column=0, columnspan=2, sticky="ew")
#     return selection

root = Tk()
root.geometry("800x480")
root.configure(bg="#515b79", relief="raised")


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frm = tk.Frame(root, bg="#515b79")
frm.grid(row=0, column=0, sticky="nsew")

frm.columnconfigure(0, weight=1)
frm.rowconfigure(1, weight=1)

entry = tk.Entry(frm)
entry.grid(row=0, column=0, sticky="ew")

header = tk.Label(frm, text="Select A Game", font="System", foreground="black", anchor="w")
header.grid(row=0, column=0, columnspan=2, sticky="new")

# selection1 = selection_button("First Item", root.destroy, 1)
# selection2 = selection_button("Second Item", root.destroy, 2)
# selection3 = selection_button("Third Item", root.destroy, 3)
# selection4 = selection_button("Fourth Item", root.destroy, 4)
# selection5 = selection_button("Fifth Item", root.destroy, 5)
# selection6 = selection_button("Sixth Item", root.destroy, 6)
# selection7 = selection_button("Seventh Item", root.destroy, 7)
# selection8 = selection_button("Eighth Item", root.destroy, 8)

PAGE_COUNT = GAME_COUNT // 8
if GAME_COUNT % 8 > 0:
    PAGE_COUNT += 1

for i in range(PAGE_COUNT):
    selection_button(ROMS, )


forward_button = cb.Menu_Button(frm, text=">", command=root.destroy)
forward_button.grid(row=10, column=1, sticky="e")

back_button = cb.Menu_Button(frm, text="<", command=root.destroy)
back_button.grid(row=10, column=0, sticky="e")


if __name__ == '__main__':
    root.mainloop()


