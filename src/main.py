import os
import tkinter as tk
from tkinter import *
import Custom_Buttons as cb
from game import Game
# import navigation as nv

"""
THESE ARE GLOBAL VARIABLES MADE FOR STORING INFORMATION DURING THE PROGRAM
"""
Emulators = {"nes": "nes file location",
             "snes": "snes file location",
             "gb": "gb file location",
             "gbc": "gbc file location",
             "gba": "gba file location",
             "nds": "nds file location"}
ROOT_PATH = os.path.join(os.getcwd())
ROM_PATH = os.path.join(ROOT_PATH, "roms")
RESOURCE_PATH = os.path.join(ROOT_PATH, "resources")
GAME_COUNT = 0
BOOK = [[]]
PAGE = 0
BUTTONS = []
ROW_NUMBER = 0
DIR_NAV = []
DISPLAY_STATE = 0       # 0 - Home, 1 - View Games, 2 - Settings, 3 -Themes, 4 - Date/Time, 5 - TBD
#         [ Theme Name    | Background | Game Sel Text | Game Sel Button | Game Sel HiLi | Menu Text | Menu Button | Menu HiLi]
THEMES = [["Samurott",      "#0F3057",     "#FFD166",       "#3A5F78",       "#A88F32",    "#FFD166",  "#005F73",   "#007EA7"],
          ["Emboar",        "#5E120D",     "#FFEB3B",       "#212121",       "#EE8700",    "#FFC400",  "#B71C1C",   "#e65100"],
          ["Serperior",     "#184A27",     "#F9A825",       "#5B7553",       "#FFD700",    "#F9A825",  "#2E7D32",   "#4CAF50"],
          ["Haxorus",       "#2E3B3A",     "#F5F5F5",       "#5B734D",       "#99D6A1",    "#F5F5F5",  "#801f12",   "#6F35FC"],
          ["Altaria",       "#A0C8E5",     "#FFFFFF",       "#4F9CB9",       "#7EC8D3",    "#FFFFFF",  "#3A8FBF",   "#5DA9D7"],
          ["Gengar",        "#3A3A3D",     "#E9E9E9",       "#7A4E8D",       "#B799E6",    "#E9E9E9",  "#6A4C9C",   "#8E62B3"],
          ["Zoroark",       "#2A2A2A",     "#F0F0F0",       "#5E5E5E",       "#9E2A2A",    "#D1D1D1",  "#7C2B2B",   "#9E4A4A"],
          ["Diglett",       "#5D3D2E",     "#F0E8C0",       "#6B4A2D",       "#B48433",    "#F0E8C0",  "#7A5C41",   "#9E7B54"],
          ["Zekrom",        "#0D0D0D",     "#E0E0E0",       "#1F2833",       "#0B8FAC",    "#76D7EA",  "#292929",   "#3D3D3D"],
          ["Reshiram",      "#F8F8F8",     "#3B1C14",       "#FAE6C8",       "#FF9F33",    "#D96629",  "#E3E3E3",   "#CFCFCF"],
          ["Galvantula",    "#2A2D45",     "#F8F8F8",       "#3B3E5E",       "#FFA500",    "#1B1B1B",  "#FFD200",   "#FFEE70"],
          ["Druddigon",     "#263F58",     "#F1F1F1",       "#2F3F56",       "#D2504E",    "#F8F8F8",  "#9A1F26",   "#B04D4F"]
          ]


def theme_writer(number):
    global THEME_NUMBER
    with open(os.path.join(RESOURCE_PATH, "THEME#.txt"), 'w') as file:
        file.write(str(number))
    THEME_NUMBER = theme_reader()


def theme_reader():
    with open(os.path.join(RESOURCE_PATH, "THEME#.txt"), 'r') as file:
        return int(file.readline()) % len(THEMES)


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
        rows = 3
    if DISPLAY_STATE == 3:
        rows = 12
    if DISPLAY_STATE == 4:
        pass
    if DISPLAY_STATE == 5:
        pass
    return rows


def focus_next():
    global ROW_NUMBER
    max_rows = number_of_rows_on_page()

    if ROW_NUMBER == max_rows - 1:
        ROW_NUMBER = 0
    else:
        ROW_NUMBER += 1
    BUTTONS[ROW_NUMBER].focus_set()


def focus_previous():
    global ROW_NUMBER
    max_rows = number_of_rows_on_page()

    if ROW_NUMBER == 0:
        ROW_NUMBER = max_rows - 1
    else:
        ROW_NUMBER -= 1
    if not BUTTONS[ROW_NUMBER].focus_get() in BUTTONS:
        ROW_NUMBER = max_rows - 1
    BUTTONS[ROW_NUMBER].focus_set()


def focus_left():
    global ROW_NUMBER
    max = number_of_rows_on_page()
    if ROW_NUMBER < 2:
        ROW_NUMBER += max - 2
    else:
        ROW_NUMBER -= 2
    focus_previous()


def focus_right():
    global ROW_NUMBER
    max = number_of_rows_on_page()
    if ROW_NUMBER >= max - 2:
        ROW_NUMBER -= max - 2
    else:
        ROW_NUMBER += 2
    focus_next()


def quick_select_button(button):
    global ROW_NUMBER
    if button.focus:

        button.invoke()
        return
    button.focus_set()
    ROW_NUMBER = number_of_rows_on_page() - 1


def select_game():
    BUTTONS[ROW_NUMBER].focus_get().invoke()


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


def goto_time():
    pass


def goto_themes():
    theme_setting_page()


def goto_calibrate():
    pass


def set_theme():
    thing = BUTTONS[0].focus_get()
    for i in range(len(BUTTONS)):
        if BUTTONS[i] == thing:
            theme_writer(i)
            theme_setting_page()


def game_display_page(page_num):
    global DISPLAY_STATE
    DISPLAY_STATE = 1
    row_global_reset()
    root.unbind("<Right>")
    root.unbind("<Left>")
    root.unbind("<Up>")
    root.unbind("<Down>")
    root.unbind("<b>")

    root.bind("<Right>", lambda event: next_page())
    root.bind("<Left>", lambda event: last_page())

    frm = tk.Frame(root, bg=THEMES[THEME_NUMBER][1])
    frm.grid(row=0, column=0, sticky="nsew")

    frm.columnconfigure(0, weight=0)
    frm.columnconfigure(1, weight=5)
    frm.columnconfigure(2, weight=5)
    frm.rowconfigure(9, weight=1)
    frm.rowconfigure(10, weight=0)

    header = tk.Label(frm, text="System  |  Select A Game", font=("System", 16), foreground="black", anchor="w", border=5)
    header.grid(row=0, column=0, columnspan=3, sticky="new")

    for num in range(10):
        tk.Label(frm, text='_', foreground=THEMES[THEME_NUMBER][1], bg=THEMES[THEME_NUMBER][1], border=0, anchor="e").grid(row=num, column=3, sticky="nes")

    game_counter = 1
    BUTTONS.clear()
    for game in BOOK[page_num]:
        tk.Label(frm, text='  ' + game.type.upper() + ' ', font=("System", 12), foreground=game.colorized(), bg=THEMES[THEME_NUMBER][1], border=1, anchor="center").grid(row=game_counter, column=0, sticky="nws")
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
    home_button.config(padx=0, pady=0, font=("System", 18))
    home_button.grid(row=9, column=0, sticky="sw", padx=3, pady=3)

    root.bind("<Down>", lambda event: focus_next())
    root.bind("<Up>", lambda event: focus_previous())

    root.bind("<b>", lambda event: quick_select_button(home_button))


def home_display_page():
    global DISPLAY_STATE
    DISPLAY_STATE = 0
    row_global_reset()
    root.unbind("<b>")
    root.unbind("<Right>")
    root.unbind("<Left>")
    root.unbind("<Up>")
    root.unbind("<Down>")
    frm = tk.Frame(root, bg=THEMES[THEME_NUMBER][1])
    frm.grid(row=0, column=0, sticky="nsew")
    frm.columnconfigure(1, weight=1)
    frm.rowconfigure(0, weight=1)
    frm.rowconfigure(4, weight=1)
    BUTTONS.clear()

    home_button = cb.MenuButton(frm, text="    View Games    ", command=goto_games)
    home_button.grid(row=1, column=1, pady=5)
    BUTTONS.append(home_button)

    settings_button = cb.MenuButton(frm, text="    Settings    ", command=goto_settings)
    settings_button.grid(row=2, column=1, pady=5)
    BUTTONS.append(settings_button)

    exit_button = cb.MenuButton(frm, text="Shutdown", command=shutdown)
    exit_button.grid(row=3, column=1, pady=5)
    BUTTONS.append(exit_button)

    BUTTONS[0].focus_set()
    root.bind("<Down>", lambda event: focus_next())
    root.bind("<Up>", lambda event: focus_previous())

    root.bind("<b>", lambda event: quick_select_button(exit_button))


def settings_display_page():
    global DISPLAY_STATE
    DISPLAY_STATE = 2
    row_global_reset()
    root.unbind("<b>")
    root.unbind("<Right>")
    root.unbind("<Left>")
    root.unbind("<Up>")
    root.unbind("<Down>")
    frm = tk.Frame(root, bg=THEMES[THEME_NUMBER][1])
    frm.grid(row=0, column=0, sticky="nsew")
    frm.columnconfigure(0, weight=1)
    frm.columnconfigure(1, weight=1)
    frm.columnconfigure(2, weight=1)
    frm.columnconfigure(3, weight=1)
    frm.columnconfigure(4, weight=1)
    frm.rowconfigure(0, weight=1)
    frm.rowconfigure(4, weight=1)
    BUTTONS.clear()

    header = tk.Label(frm, text="System Settings", font=("System", 16), foreground="black", anchor="n", border=5)
    header.grid(row=0, column=0, columnspan=7, sticky="new")

    time_button = cb.MenuButton(frm, text="   Time   ", command=goto_time)
    time_button.grid(row=3, column=1, pady=3, padx=5)
    time_button.focus_set()
    BUTTONS.append(time_button)

    theme_button = cb.MenuButton(frm, text="  Colors  ", command=goto_themes)
    theme_button.grid(row=3, column=2, pady=3, padx=5)
    BUTTONS.append(theme_button)

    calibration_button = cb.MenuButton(frm, text="Calibrate", anchor="center", command=goto_calibrate)
    calibration_button.grid(row=3, column=3, pady=3, padx=5)
    BUTTONS.append(calibration_button)

    home_button = cb.MenuButton(frm, text="[<-", command=goto_home, padx=2, pady=2)
    home_button.config(padx=0, pady=0, font=("System", 18))
    home_button.grid(row=4, column=0, sticky="sw", padx=3, pady=1)

    invis_button = cb.MenuButton(frm, text="[<-", command=None, padx=2, pady=2)
    invis_button.config(padx=0, pady=0, relief=tk.FLAT, background=THEMES[THEME_NUMBER][1], font=("System", 18),
                        activebackground=THEMES[THEME_NUMBER][1], foreground=THEMES[THEME_NUMBER][1],
                        activeforeground=THEMES[THEME_NUMBER][1])
    invis_button.grid(row=4, column=4, sticky="se", padx=3, pady=1)

    root.bind("<b>", lambda event: quick_select_button(home_button))
    root.bind("<Right>", lambda event: focus_next())
    root.bind("<Left>", lambda event: focus_previous())

    pass


def theme_setting_page():
    global DISPLAY_STATE
    DISPLAY_STATE = 3
    row_global_reset()
    root.unbind("<b>")
    root.unbind("<Right>")
    root.unbind("<Left>")
    root.unbind("<Up>")
    root.unbind("<Down>")
    frm = tk.Frame(root, bg=THEMES[THEME_NUMBER][1])
    frm.grid(row=0, column=0, sticky="nsew")
    frm.columnconfigure(0, weight=1)
    frm.columnconfigure(2, weight=1)
    frm.columnconfigure(4, weight=1)
    frm.columnconfigure(6, weight=1)
    frm.columnconfigure(8, weight=1)
    frm.rowconfigure(0, weight=1)
    frm.rowconfigure(8, weight=1)

    BUTTONS.clear()

    # SPACERS
    for i in range(9):
        if i % 2 == 0:
            tk.Label(frm, text='___', foreground=THEMES[THEME_NUMBER][1], background=THEMES[THEME_NUMBER][1]).grid(row=3, column=i)
            tk.Label(frm, text='___', foreground=THEMES[THEME_NUMBER][1], background=THEMES[THEME_NUMBER][1]).grid(row=5, column=i)
            tk.Label(frm, text='___', foreground=THEMES[THEME_NUMBER][1], background=THEMES[THEME_NUMBER][1]).grid(row=7, column=i)
    tk.Label(frm, text="_", foreground=THEMES[THEME_NUMBER][1], background=THEMES[THEME_NUMBER][1]).grid(row=2, columnspan=9)
    tk.Label(frm, text="_", foreground=THEMES[THEME_NUMBER][1], background=THEMES[THEME_NUMBER][1]).grid(row=4, columnspan=9)
    tk.Label(frm, text="_", foreground=THEMES[THEME_NUMBER][1], background=THEMES[THEME_NUMBER][1]).grid(row=6, columnspan=9)
    tk.Label(frm, text="_", foreground=THEMES[THEME_NUMBER][1], background=THEMES[THEME_NUMBER][1]).grid(row=8, columnspan=9)

    for i in range(number_of_rows_on_page()):
        butt = cb.SelectionButton(frm, text=THEMES[i][0], font=("Terminal", 10), command=set_theme, anchor="center")
        butt.grid(row=((i % 3) * 2) + 3, column=((i // 3) * 2) + 1, sticky="ew")
        BUTTONS.append(butt)

    home_button = cb.MenuButton(frm, text="[<-", command=goto_settings, padx=2, pady=2)
    home_button.config(padx=0, pady=0, font=("System", 18))
    home_button.grid(row=8, column=0, sticky="sw", padx=3, pady=1)

    invis_button = cb.MenuButton(frm, text="[<-", command=None, padx=2, pady=2)
    invis_button.config(padx=0, pady=0, relief=tk.FLAT, background=THEMES[THEME_NUMBER][1], font=("System", 18),
                        activebackground=THEMES[THEME_NUMBER][1], foreground=THEMES[THEME_NUMBER][1],
                        activeforeground=THEMES[THEME_NUMBER][1])
    invis_button.grid(row=8, column=8, sticky="se", padx=3, pady=1)

    root.bind("<Left>", lambda event: focus_left())
    root.bind("<Right>", lambda event: focus_right())
    root.bind("<Up>", lambda event: focus_previous())
    root.bind("<Down>", lambda event: focus_next())
    root.bind("<b>", lambda event: goto_settings())

    BUTTONS[0].focus_set()


def time_setting_page():
    global DISPLAY_STATE
    DISPLAY_STATE = 4
    row_global_reset()
    root.unbind("<b>")
    root.unbind("<Right>")
    root.unbind("<Left>")
    root.unbind("<Up>")
    root.unbind("<Down>")
    frm = tk.Frame(root, bg=THEMES[THEME_NUMBER][1])
    frm.grid(row=0, column=0, sticky="nsew")


if __name__ == '__main__':
    THEME_NUMBER = theme_reader()

    for rom_type in Emulators.keys():
        files = os.listdir(os.path.join(ROM_PATH, rom_type))
        for file in files:
            if len(BOOK[len(BOOK) - 1]) >= 8:
                BOOK.append([])
            BOOK[len(BOOK) - 1].append(Game(title_grabber(file), file, rom_type))

    root = Tk()
    root.geometry("800x480")
    # root.attributes('-fullscreen', True)   # Disable while testing, Enable while on actual 800x480 screen.
    root.configure(bg=THEMES[THEME_NUMBER][1])
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    home_display_page()

    # root.bind("<Right>", lambda event: next_page())
    # root.bind("<Left>", lambda event: last_page())
    root.bind("<Down>", lambda event: focus_next())
    root.bind("<Up>", lambda event: focus_previous())
    root.bind("<a>", lambda event: select_game())
    root.bind("<f>", lambda event: theme_writer(6))
    # theme_writer(8)

    root.mainloop()
