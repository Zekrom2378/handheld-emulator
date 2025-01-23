import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Custom_Buttons as cb
from game import Game

Emulators = {"nes": "nes file location",
             "snes": "snes file location",
             "gb": "gb file location",
             "gbc": "gbc file location",
             "gba": "gba file location",
             "nds": "nds file location" }

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


for rom_type in Emulators.keys():
    files = os.listdir(os.path.join(ROOT_PATH, rom_type))
    for file in files:
        if len(BOOK[len(BOOK)-1]) >= 8:
            BOOK.append([])
        BOOK[len(BOOK)-1].append(Game(title_grabber(file), file, rom_type))


def play_game(num):
    BOOK[PAGE][num].launch(ROOT_PATH, Emulators[BOOK[PAGE][num].type])


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

    game_counter = 1
    for game in BOOK[page_num]:
        selection_button(frm, game.name, game_counter)
        game_counter += 1

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



