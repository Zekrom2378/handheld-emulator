import os
import tkinter as tk
from tkinter import *
import Custom_Buttons as cb
from game import Game
# import navigation as nv

Emulators = {"nes": "nes file location",
             "snes": "snes file location",
             "gb": "gb file location",
             "gbc": "gbc file location",
             "gba": "gba file location",
             "nds": "nds file location"}

ROOT_PATH = os.path.join(os.getcwd(), "roms")

GAME_COUNT = 0
BOOK = [[]]
PAGE = 0
BUTTONS = []
PAGE_NUMBER = 0
DIR_NAV = []


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


def focus_next(left, right):
    # global BUTTONS
    global PAGE_NUMBER
    if PAGE_NUMBER == 7:
        if right.focus_get() == '.!frame.!menubutton':
            if left.focus_get() == '.!frame.!menubutton2':
                BUTTONS[PAGE_NUMBER].focus_set()
            else:
                left.focus_set()
        else:
            right.focus_set()
    else:
        PAGE_NUMBER += 1
        BUTTONS[PAGE_NUMBER].focus_set()


def focus_previous(left, right):
    # global BUTTONS
    global PAGE_NUMBER
    if PAGE_NUMBER == 0:
        if left.focus_get() == '.!frame.!menubutton2':
            if right.focus_get() == '.!frame.!menubutton':
                PAGE_NUMBER = 7
                BUTTONS[PAGE_NUMBER].focus_set()
            else:
                PAGE_NUMBER = 0
                right.focus_set()
        else:
            right.focus_set()
    else:
        PAGE_NUMBER -= 1
        BUTTONS[PAGE_NUMBER].focus_set()


def select_direction_button(button):
    button.focus_set()


for rom_type in Emulators.keys():
    files = os.listdir(os.path.join(ROOT_PATH, rom_type))
    for file in files:
        if len(BOOK[len(BOOK)-1]) >= 8:
            BOOK.append([])
        BOOK[len(BOOK)-1].append(Game(title_grabber(file), file, rom_type))


def play_game(num):
    BOOK[PAGE][num].launch(ROOT_PATH, Emulators[BOOK[PAGE][num].type])


def selection_button(frm, title, row_num):
    selection = cb.SelectionButton(frm, text=title, command=lambda: play_game(row_num - 1), anchor="w")
    selection.grid(row=row_num, column=1, columnspan=2, sticky="ew")
    BUTTONS.append(selection)


def next_page():
    global PAGE
    PAGE += 1
    if PAGE >= len(BOOK):
        PAGE = 0
    game_display_page(PAGE)


def last_page():
    global PAGE
    PAGE -= 1
    if abs(PAGE) >= len(BOOK):
        PAGE = 0
    game_display_page(PAGE)


def shutdown():
    # os.system('shutdown -P now')
    root.destroy()


def home_to_game_page():
    game_display_page(PAGE)


def back_to_home_page():
    home_display_page()


def home_to_settings_page():
    pass


def game_display_page(page_num):
    frm = tk.Frame(root, bg="#515b79")
    frm.grid(row=0, column=0, sticky="nsew")

    frm.columnconfigure(0, weight=0)
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
    BUTTONS.clear()
    for game in BOOK[page_num]:
        selection_button(frm, game.name, game_counter)
        if game_counter == 1:
            BUTTONS[0].focus_set()
        game_counter += 1

    forward_button = cb.MenuButton(frm, text=">", command=next_page)
    forward_button.grid(row=9, column=2, sticky="sw", pady=3)
    DIR_NAV.append(forward_button)

    back_button = cb.MenuButton(frm, text="<", command=last_page)
    back_button.grid(row=9, column=1, sticky="se", pady=3)
    DIR_NAV.append(back_button)

    home_button = cb.MenuButton(frm, text="[<-", font=("System", 10), command=back_to_home_page, padx=1)
    home_button.grid(row=9, column=0, sticky="sw", pady=1, padx=1)


def home_display_page():
    frm = tk.Frame(root, bg="#515b79")
    frm.grid(row=0, column=0, sticky="nsew")
    frm.columnconfigure(1, weight=1)
    frm.rowconfigure(0, weight=1)
    frm.rowconfigure(4, weight=1)

    home_button = cb.MenuButton(frm, text="View Games", font="System", command=home_to_game_page)
    home_button.grid(row=1, column=1, pady=5)

    settings_button = cb.MenuButton(frm, text="Settings", command=home_to_settings_page)
    settings_button.grid(row=2, column=1, pady=5)

    exit_button = cb.MenuButton(frm, text="Shutdown", command=shutdown)
    exit_button.grid(row=3, column=1, pady=5)
    pass


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x480")
    # root.attributes('-fullscreen', True)   # Disable while testing, Enable while on actual 800x480 screen.
    root.configure(bg="#515b79")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    home_display_page()

    print(BUTTONS)
    print(PAGE_NUMBER)
    root.bind("<Right>", lambda event: select_direction_button(DIR_NAV[0]))
    root.bind("<Left>", lambda event: select_direction_button(DIR_NAV[1]))
    root.bind("<Down>", lambda event: focus_next(DIR_NAV[1], DIR_NAV[0]))
    root.bind("<Up>", lambda event: focus_previous(DIR_NAV[1], DIR_NAV[0]))

    root.mainloop()
