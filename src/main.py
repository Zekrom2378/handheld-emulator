import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Custom_Buttons as cb
from gba import GBA

ROMS = {"NES":  {"Title": [], "File": []},
        "SNES": {"Title": [], "File": []},
        "GB":   {"Title": [], "File": []},
        "GBC":  {"Title": [], "File": []},
        "GBA":  {"Title": [], "File": []},
        "NDS":  {"Title": [], "File": []}}

ROOT_PATH = os.path.join(os.getcwd(), "roms")

GAME_COUNT = 0
BOOK = [[]]
PAGE = 0

def title_grabber(title):
    if len(title.split('.')) > 2:
        temp = title.split('.')
        temp = temp[:-1]
        title = ''.join(temp)
    else:
        title = title.split('.')[0]

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
    # files = os.listdir(ROOT_PATH + '\\' + key.lower())
    files = os.listdir(os.path.join(ROOT_PATH, key.lower()))
    for file in files:
        ROMS[key]["File"].append(GBA(title_grabber(file), file))
        GAME_COUNT += 1
        ROMS[key]["Title"].append(title_grabber(file))

        if len(BOOK[len(BOOK) - 1]) >= 8:
            BOOK.append([])
        BOOK[len(BOOK) - 1].append(title_grabber(file))


# TODO : Create a function that does need parameters to launch a game specified by the text on the selection button that
#   is pressed ROM[EMULATOR][TITLE] and ROM[EMULATOR][FILE] should have all info needed
def play_game(num):
    print(BOOK[PAGE][num])
    for key in ROMS:
        for name in ROMS[key]["Title"]:
            print([i for i, x in enumerate(ROMS[key]["Title"]) if x == name])

    pass


def selection_button(frm, title, row_num):
    selection = cb.Selection_Button(frm, text=title, command=lambda: play_game(row_num), anchor="w")
    selection.grid(row=row_num, column=1, columnspan=2, sticky="ew")


def next_page():
    global PAGE
    PAGE += 1
    if PAGE >= len(BOOK):
        PAGE = 0
    display_page(PAGE)


def last_page():
    global PAGE
    PAGE -= 1
    if abs(PAGE) >= len(BOOK):
        PAGE = 0
    display_page(PAGE)


def display_page(page_num):
    frm = tk.Frame(root, bg="#515b79")
    frm.grid(row=0, column=0, sticky="nsew")

    frm.columnconfigure(1, weight=1)
    frm.columnconfigure(2, weight=1)
    frm.rowconfigure(9, weight=1)
    frm.rowconfigure(10, weight=0)

    header = tk.Label(frm, text="       Select A Game", font=("System", 16), foreground="black", anchor="w", border=5)
    header.grid(row=0, column=0, columnspan=3, sticky="new")

    for num in range(10):
        tk.Label(frm, text='_', foreground="#515b79", bg="#515b79", border=0, anchor="e").grid(row=num, column=0, sticky="nws")
        tk.Label(frm, text='_', foreground="#515b79", bg="#515b79", border=0, anchor="e").grid(row=num, column=3, sticky="nes")

    c = 1
    for game in BOOK[page_num]:
        selection_button(frm, game, c)
        c += 1

    forward_button = cb.Menu_Button(frm, text=">", command=next_page)
    forward_button.grid(row=9, column=2, sticky="sw", pady=3)

    back_button = cb.Menu_Button(frm, text="<", command=last_page)
    back_button.grid(row=9, column=1, sticky="se", pady=3)


root = Tk()
root.geometry("800x480")
# root.attributes('-fullscreen', True)   # Disable while testing, Enable while on actual 800x480 screen.
root.configure(bg="#515b79")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

display_page(PAGE)




if __name__ == '__main__':
    root.mainloop()



