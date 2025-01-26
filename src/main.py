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
ROW_NUMBER = 0
DIR_NAV = []
DISPLAY_STATE = 0                                                    # 0 - Home, 1 - View Games, 2 - Settings, 3 -TBD


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


def row_global_reset():
    global ROW_NUMBER
    ROW_NUMBER = 0


def number_of_rows_on_page():
    global DISPLAY_STATE
    rows = 0
    if DISPLAY_STATE == 0:
        rows = 3
    if DISPLAY_STATE == 1:
        rows = len(BOOK[PAGE])
    if DISPLAY_STATE == 2:
        pass
    return rows


def focus_next():
    global PAGE
    global ROW_NUMBER
    global DISPLAY_STATE
    max_rows = number_of_rows_on_page()

    if ROW_NUMBER == max_rows - 1:
        ROW_NUMBER = 0
    else:
        ROW_NUMBER += 1
    BUTTONS[ROW_NUMBER].focus_set()


def focus_previous():
    global PAGE
    global ROW_NUMBER
    global DISPLAY_STATE
    max_rows = number_of_rows_on_page()

    if ROW_NUMBER == 0:
        ROW_NUMBER = max_rows - 1
    else:
        ROW_NUMBER -= 1
    BUTTONS[ROW_NUMBER].focus_set()


def quick_select_button(button):
    global ROW_NUMBER
    if button.focus:

        button.invoke()
        return
    button.focus_set()
    ROW_NUMBER = number_of_rows_on_page() - 1


def select_game():
    for game in BUTTONS:
        if game.focus:
            game.config(activebackground="#3366cc",  activeforeground="white")
            game.invoke()


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


def goto_games():
    game_display_page(PAGE)


def goto_home():
    home_display_page()


def goto_settings():
    settings_display_page()


def game_display_page(page_num):
    global DISPLAY_STATE
    DISPLAY_STATE = 1
    row_global_reset()
    root.unbind("<Right>")
    root.unbind("<Left>")
    root.unbind("<b>")

    root.bind("<Right>", lambda event: next_page())
    root.bind("<Left>", lambda event: last_page())

    frm = tk.Frame(root, bg="#515b79")
    frm.grid(row=0, column=0, sticky="nsew")

    frm.columnconfigure(0, weight=0)
    frm.columnconfigure(1, weight=5)
    frm.columnconfigure(2, weight=5)
    frm.rowconfigure(9, weight=1)
    frm.rowconfigure(10, weight=0)

    header = tk.Label(frm, text="System  |  Select A Game", font=("System", 16), foreground="black", anchor="w", border=5)
    header.grid(row=0, column=0, columnspan=3, sticky="new")

    for num in range(10):
        tk.Label(frm, text='_', foreground="#515b79", bg="#515b79", border=0, anchor="e").grid(row=num, column=3, sticky="nes")

    game_counter = 1
    BUTTONS.clear()
    for game in BOOK[page_num]:
        tk.Label(frm, text='  ' + game.type.upper() + ' ', font=("System", 12), foreground=game.colorized(), bg="#515b79", border=1, anchor="center").grid(row=game_counter, column=0, sticky="nws")
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

    home_button = cb.MenuButton(frm, text="[<-", command=goto_home, padx=2, pady=2)
    home_button.config(padx=0, font=("System", 18))
    home_button.grid(row=9, column=0, sticky="sw", padx=3, pady=3)

    root.bind("<b>", lambda event: quick_select_button(home_button))


def home_display_page():
    global DISPLAY_STATE
    DISPLAY_STATE = 0
    row_global_reset()
    root.unbind("<b>")
    frm = tk.Frame(root, bg="#515b79")
    frm.grid(row=0, column=0, sticky="nsew")
    frm.columnconfigure(1, weight=1)
    frm.rowconfigure(0, weight=1)
    frm.rowconfigure(4, weight=1)
    BUTTONS.clear()

    home_button = cb.MenuButton(frm, text="    View Games    ", font="System", command=goto_games)
    home_button.grid(row=1, column=1, pady=5)
    BUTTONS.append(home_button)

    settings_button = cb.MenuButton(frm, text="    Settings    ", command=goto_settings)
    settings_button.grid(row=2, column=1, pady=5)
    BUTTONS.append(settings_button)

    exit_button = cb.MenuButton(frm, text="Shutdown", command=shutdown)
    exit_button.grid(row=3, column=1, pady=5)
    BUTTONS.append(exit_button)

    BUTTONS[0].focus_set()

    root.bind("<b>", lambda event: quick_select_button(exit_button))


def settings_display_page():
    global DISPLAY_STATE
    DISPLAY_STATE = 2
    row_global_reset()
    pass


if __name__ == '__main__':
    for rom_type in Emulators.keys():
        files = os.listdir(os.path.join(ROOT_PATH, rom_type))
        for file in files:
            if len(BOOK[len(BOOK) - 1]) >= 8:
                BOOK.append([])
            BOOK[len(BOOK) - 1].append(Game(title_grabber(file), file, rom_type))

    root = Tk()
    root.geometry("800x480")
    # root.attributes('-fullscreen', True)   # Disable while testing, Enable while on actual 800x480 screen.
    root.configure(bg="#515b79")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    home_display_page()

    # root.bind("<Right>", lambda event: next_page())
    # root.bind("<Left>", lambda event: last_page())
    root.bind("<Down>", lambda event: focus_next())
    root.bind("<Up>", lambda event: focus_previous())
    root.bind("<a>", lambda event: select_game())

    root.mainloop()
